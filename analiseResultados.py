import os
import numpy as np

DIR_RESULTADOS = "resultados/"
TIPOS = ["genero", "faixa", "faixa_genero"]


def getMelhoresFolds(medias, melhorAcc):
    melhores = []
    for m in range(len(medias)):
        if(medias[m] == melhorAcc):
            melhores.append(m)

    return melhores


def calcularPredRec(matriz_confusao, classes):
    precisao = [0]*classes
    recall = [0]*classes
    sum_columns = np.sum(matriz_confusao, axis=0)
    sum_lines = np.sum(matriz_confusao, axis=1)
    for c in range(classes):
        recall[c] = matriz_confusao[c][c] / sum_lines[c]
        #precisao[c] = matriz_confusao[c][c] / sum_columns[c]
        precisao[c] = (0 if sum_columns[c] == 0 else matriz_confusao[c][c] / sum_columns[c])

    return precisao, recall


def calcularFmeasures(precisions, recalls, classes):
    fMeasures = [0]*classes
    for c in range(classes):
        fMeasures[c] = 0 if precisions[c] + recalls[c] == 0 else (2 * precisions[c] * recalls[c]) / (precisions[c] + recalls[c])
    return fMeasures


def calcular(diretorio, descritor, solver, tipo, arq_folds, arq):

    folds = []

    classes = 8
    if(tipo == "faixa"):
        classes = 4
    if(tipo == "genero"):
        classes = 2

    totais = [0]*classes
    acertos = [0]*classes
    medias = [0]*classes
    matriz_confusao = [[0 for x in range(classes)] for y in range(classes)]
    acertos_fold = [0] * 5
    total_fold = [0] * 5
    media_fold = [0] * 5

    for f in range(len(arq_folds)):
        file = open(diretorio+arq_folds[f], "r")
        folds.append(file.readlines())

    for l in range(1, len(folds[0]) - 1):
        for f in range(len(folds)):
            linha = folds[f][l].split(",")
            classe_esperada = int(linha[0])
            classe_predita = int(linha[1])
            totais[classe_esperada] = totais[classe_esperada] + 1
            matriz_confusao[classe_esperada][classe_predita] = matriz_confusao[classe_esperada][classe_predita] + 1
            total_fold[f] = total_fold[f] + 1
            if classe_esperada == classe_predita:
                acertos[classe_esperada] = acertos[classe_esperada] + 1
                acertos_fold[f] = acertos_fold[f] + 1

    precisions, recalls = calcularPredRec(matriz_confusao, classes)
    fMeasures = calcularFmeasures(precisions, recalls, classes)

    for f in range(classes):
        if totais[f] != 0:
            medias[f] = acertos[f] / totais[f]

    for f in range(5):
        if total_fold[f] != 0:
            media_fold[f] = acertos_fold[f] / total_fold[f]

    #print(matriz_confusao)
    #print(str(matriz_confusao[0][0]) + " " + str(matriz_confusao[0][1]))
    #print(str(matriz_confusao[1][0]) + " " + str(matriz_confusao[1][1]))
    print("===")
    print(precisions)
    print(recalls)
    print(fMeasures)
    print(str(getMelhoresFolds(medias, max(medias))) + str(medias))

    acc_media = np.mean(medias)
    desvio_padrao = np.std(medias)
    macrof = np.mean(fMeasures)
    melhorAcc = max(media_fold)
    melhorFold = getMelhoresFolds(media_fold, melhorAcc)
    arq.write(descritor + "," + tipo + "," + solver + "," + str(acc_media) + "," + str(desvio_padrao) + ","
              + str(macrof) + "," + str(melhorFold) + "," + str(melhorAcc) + "\n")




def initResultados(dir_resultados, tipos):

    arq = open(dir_resultados + "resultados.csv", 'w')
    arq.write("Descritor, Classificacao, Solver, Acc. Media, Desvio Padrao, Macro-F Media, Melhor Fold, Melhor Acc.\n")

    descritores = os.listdir(dir_resultados)
    qtd_descritores = len(descritores)
    for d in range(qtd_descritores):
        if(descritores[d] == "resultados.csv"):
            continue
        qtd_tipos = len(tipos)
        for t in range(qtd_tipos):
            dir_solvers = dir_resultados + descritores[d] + "/"
            solvers = os.listdir(dir_solvers)
            qtd_solvers = len(solvers)

            for s in range(qtd_solvers):
                dir_tipos = dir_solvers + solvers[s] + "/"
                dir_folds = dir_tipos + tipos[t] + "/"
                folds = os.listdir(dir_folds)
                print(folds)
                ##calcular(dir_folds, descritores[d], solvers[s], tipos[t], folds, arq)

    arq.close()

initResultados(DIR_RESULTADOS, TIPOS)
