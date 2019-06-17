import matplotlib
from jedi.refactoring import inline
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import os

NUM_FOLDS = 5
solvers = ["lbfgs", "sgd", "adam"]

tipo_classificacao = ["genero", "faixa", "faixa_genero"]
diretorio_resultados = "resultados/"


def classificar(tipo, descritor, solver, fold_test, x_train, y_train, x_test, y_test):
    #print("iniciando a classificacao ...")

    clf = MLPClassifier(hidden_layer_sizes=(100, 100, 100), max_iter=500, alpha=0.0001, solver=solver, verbose=0, random_state=21, tol=0.000000001)

    x_train = x_train.astype(np.float)
    y_train = y_train.astype(np.float)
    x_test = x_test.astype(np.float)
    y_test = y_test.astype(np.float)

    clf.fit(x_train, y_train)
    #y_pred = clf.predict(x_test)
    y_pred = clf.predict_proba(x_test)

    #print(y_pred)

    path = diretorio_resultados + descritor + "/" + solver + "/" + tipo + "/"
    if not os.path.exists(path):
        os.makedirs(path)

    arq = open(path + "fold_" + str(fold_test) + ".csv", 'w')

    arq.write("classe_esperada, classe_predida, probabilidades\n")

    total = 0
    acerto = 0

    for i in range(len(y_pred)):
        y_esperado = int(y_test[i])
        y_predito = 0
        maior_p = y_pred[i][0]
        for p in range(len(y_pred[i])):
            if(y_pred[i][p] > maior_p):
                y_predito = p
                maior_p = y_pred[i][p]
        arq.write(str(y_esperado) + "," + str(y_predito))
        for p in range(len(y_pred[i])):
            arq.write("," + '{:.20f}'.format(y_pred[i][p]))
        arq.write("\n")
        total = total + 1
        if y_predito == y_esperado:
            acerto = acerto + 1

    print("Acerto: " + str(acerto/total))
    arq.write(str(total) + "," + str(acerto) + "," + str(acerto/total))
    arq.close()

    with open(diretorio_resultados + "resultados.csv", "a") as resultados:
        resultados.write(descritor + "," + solver + "," + str(fold_test) + "," + str(acerto/total) + "\n")




        #score = accuracy_score(y_test, y_pred)
    #print(score)
    #cm = confusion_matrix(y_test, y_pr ed)
    #print(cm)


def getValores(lines):
    for l in range(lines.shape[0]):
        ret = lines[l].split(":")
        lines[l] = ret[-1]

    return lines

def getFolders(dir, descritor, fold):
    f = open(dir + descritor + "/fold" + str(fold) + ".svm")
    num_lines = sum(1 for line in open(dir + descritor + "/fold" + str(fold) + ".svm"))
    lines = np.asarray(f.read().rstrip('\n').split())
    lines = getValores(lines)
    num_columns = int(lines.shape[0]/num_lines)
    lines = lines.reshape(num_lines, num_columns)
    x = lines[:, 1:]
    y = lines[:, 0]
    return x, y

def init_classificacao():
    #print("iniciando a pre classificacao ...")
    for tipo in range(len(tipo_classificacao)):
        diretorio_folds = "folds_" + tipo_classificacao[tipo] + "/"
        descritores = os.listdir(diretorio_folds)
        #print(descritores)

        for d in range(len(descritores)):
            print("Inicializando execucao de cross-fold validation...")
            x0, y0 = getFolders(diretorio_folds, descritores[d], 0)
            x1, y1 = getFolders(diretorio_folds, descritores[d], 1)
            x2, y2 = getFolders(diretorio_folds, descritores[d], 2)
            x3, y3 = getFolders(diretorio_folds, descritores[d], 3)
            x4, y4 = getFolders(diretorio_folds, descritores[d], 4)

            for s in range(len(solvers)):
                print("Descritor: " + descritores[d] + "\t -- \tSolver: " + solvers[s])
                for fold in range(NUM_FOLDS):
                    print("Execucao de cross-fold n. " + str(fold), end="\t")

                    if fold == 0:
                        x_train = np.concatenate((x1, x2, x3, x4), axis=0)
                        y_train = np.concatenate((y1, y2, y3, y4), axis=0)
                        x_test = x0
                        y_test = y0

                    if fold == 1:
                        x_train = np.concatenate((x0, x2, x3, x4), axis=0)
                        y_train = np.concatenate((y0, y2, y3, y4), axis=0)
                        x_test = x1
                        y_test = y1

                    if fold == 2:
                        x_train = np.concatenate((x0, x1, x3, x4), axis=0)
                        y_train = np.concatenate((y0, y1, y3, y4), axis=0)
                        x_test = x2
                        y_test = y2

                    if fold == 3:
                        x_train = np.concatenate((x0, x1, x2, x4), axis=0)
                        y_train = np.concatenate((y0, y1, y2, y4), axis=0)
                        x_test = x3
                        y_test = y3

                    if fold == 4:
                        x_train = np.concatenate((x0, x1, x2, x3), axis=0)
                        y_train = np.concatenate((y0, y1, y2, y3), axis=0)
                        x_test = x4
                        y_test = y4


                    classificar(tipo_classificacao[tipo], descritores[d], solvers[s], fold, x_train, y_train, x_test, y_test)
                    #print("Execucao de cross-fold n.{} finalizada.\n".format(fold))
    print("Gerando analise dos resultados...")


init_classificacao()