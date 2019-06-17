import os
import numpy as np

DIR_RESULTADOS = "resultados/"
DIR_LATE_FUSION = "late_fusion/"

TIPOS = ["genero", "faixa", "faixa_genero"]
SOLVERS = ["adam", "lbfgs", "sgd"]
FOLDS = 5

entradas = [
    ["lbp-full", "mfcc50", "early_rh_rp_ssd"],
    ["lbp-full", "mfcc50", "ssd"],
    ["lbp-full", "ssd"],
    ["mfcc50", "early_rh_rp_ssd"],
    ["mfcc50", "ssd"]
]


def getNumClasses(tipo):
    if tipo == "genero":
        return 2
    elif tipo == "faixa":
        return 4
    return 8


def getValores(resultado_fold):
    file_resultado = open(resultado_fold, "r")
    valores = [0] * 80
    linhas = file_resultado.readlines()
    for l in range(1, len(linhas)-1):
        linhas[l] = linhas[l].replace("\n", "")
        valores[l - 1] = linhas[l].split(",")
    return valores

def calcularSoma(soma, valores):
    idx = 2
    for l in range(len(valores)):
        for c in range(idx, len(valores[l])):
            #print(str(soma[l][c]) + " + " +  valores[l][c] + " = "+ str(soma[l][c] + float(valores[l][c])))
            soma[l+1][c] = soma[l+1][c] + float(valores[l][c])
    return soma

def calcularMult(mult, valores):
    idx = 2
    for l in range(len(valores)):
        for c in range(idx, len(valores[l])):
            mult[l + 1][c] = mult[l + 1][c] * float(valores[l][c])
    return mult


def calcularMax(max, valores):
    idx = 2
    for l in range(len(valores)):
        for c in range(idx, len(valores[l])):
            max[l + 1][c] = np.maximum(max[l + 1][c], float(valores[l][c]))
    return max




def calcularMin(min, valores):
    idx = 2
    for l in range(len(valores)):
        for c in range(idx, len(valores[l])):
            min[l + 1][c] = np.minimum(min[l + 1][c], float(valores[l][c]))
    return min


def calcular(dir_resultados, dir_lf, entrada, solver, tipo, f, num_classes):
    print("calcular " + str(entrada) + " " + solver + " " + tipo + " " + str(f) )
    soma = [[0 for x in range(num_classes+2)] for y in range(81)]
    mult = [[1 for x in range(num_classes + 2)] for y in range(81)]
    max = [[0 for x in range(num_classes+2)] for y in range(81)]
    min = [[1 for x in range(num_classes + 2)] for y in range(81)]

    for descritor in entrada:
        resultado_fold = dir_resultados + descritor + "/" + solver + "/" + tipo + "/fold_" + str(f) + ".csv"
        valores = getValores(resultado_fold)
        soma = calcularSoma(soma, valores)
        mult = calcularMult(mult, valores)
        max = calcularMax(max, valores)
        min = calcularMin(min, valores)

    header = ["classe_esperada", "classe_predida", "probabilidades"]
    soma[0] = header
    mult[0] = header
    max[0] = header
    min[0] = header
    for l in range(0, len(valores)):
        soma[l+1][0] = valores[l][0]
        mult[l+1][0] = valores[l][0]
        max[l+1][0] = valores[l][0]
        min[l+1][0] = valores[l][0]
        
        soma[l+1][1] = soma[l+1].index(np.max(soma[l+1][2:])) - 2
        mult[l + 1][1] = mult[l + 1].index(np.max(mult[l + 1][2:])) - 2
        max[l + 1][1] = max[l + 1].index(np.max(max[l + 1][2:])) - 2
        min[l + 1][1] = min[l + 1].index(np.max(min[l + 1][2:])) - 2

    classes = "_".join(entrada)
    path = dir_lf + classes + "/" + solver + "/" + tipo +"/fold_" + str(f) + "/"
    if not os.path.exists(path):
        os.makedirs(path)

    arq_soma = open(path + "soma" + ".csv", 'w')
    arq_mult = open(path + "mult" + ".csv", 'w')
    arq_max = open(path + "max" + ".csv", 'w')
    arq_min = open(path + "min" + ".csv", 'w')

    for item in soma:
        arq_soma.write("%s\n" % item)
    arq_soma.close()

    for item in mult:
        arq_mult.write("%s\n" % item)
    arq_mult.close()

    for item in max:
        arq_max.write("%s\n" % item)
    arq_max.close()

    for item in min:
        arq_min.write("%s\n" % item)
    arq_min.close()



def init_late_fusion(dir_resultados, dir_lf, entradas, tipos, solvers, folds):
    for tipo in tipos:
        num_classes = getNumClasses(tipo)
        for solver in solvers:
            for f in range(5):
                for entrada in entradas:
                    calcular(dir_resultados, dir_lf, entrada, solver, tipo, f, num_classes)

    ''''
    DESCRITORES -> TIPO - > FOLDS -> SOLVERS -> METODOS
    '''



init_late_fusion(DIR_RESULTADOS, DIR_LATE_FUSION, entradas, TIPOS, SOLVERS, FOLDS)