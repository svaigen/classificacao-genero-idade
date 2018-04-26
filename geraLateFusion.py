import os
import sys
import shutil
import numpy as np
np.set_printoptions(suppress=True)

CLASSE_ESPERADA_INDEX = 0
METODO = ["soma","multiplicacao","maximo","minimo"]

entradas = [
            [
              ["../resultados/Descritores Individuais/LBP-full-gen_faixa/4folds/0-gen_faixa-4folds-csvc-linear/fold0-analysis.csv",
               "../resultados/Descritores Individuais/MFCC50-gen_faixa/4folds/0-gen_faixa-4folds-csvc-linear/fold0-analysis.csv",
               "../resultados/Early Fusion/rh_rp_ssd-gen_faixa/4folds/0-gen_faixa-4folds-csvc-linear/fold0-analysis.csv"],
              ["../resultados/Descritores Individuais/LBP-full-gen_faixa/4folds/0-gen_faixa-4folds-csvc-linear/fold1-analysis.csv",
               "../resultados/Descritores Individuais/MFCC50-gen_faixa/4folds/0-gen_faixa-4folds-csvc-linear/fold1-analysis.csv",
               "../resultados/Early Fusion/rh_rp_ssd-gen_faixa/4folds/0-gen_faixa-4folds-csvc-linear/fold1-analysis.csv"], 
              ["../resultados/Descritores Individuais/LBP-full-gen_faixa/4folds/0-gen_faixa-4folds-csvc-linear/fold2-analysis.csv",
               "../resultados/Descritores Individuais/MFCC50-gen_faixa/4folds/0-gen_faixa-4folds-csvc-linear/fold2-analysis.csv",
               "../resultados/Early Fusion/rh_rp_ssd-gen_faixa/4folds/0-gen_faixa-4folds-csvc-linear/fold2-analysis.csv"],
              ["../resultados/Descritores Individuais/LBP-full-gen_faixa/4folds/0-gen_faixa-4folds-csvc-linear/fold3-analysis.csv",
               "../resultados/Descritores Individuais/MFCC50-gen_faixa/4folds/0-gen_faixa-4folds-csvc-linear/fold3-analysis.csv",
               "../resultados/Early Fusion/rh_rp_ssd-gen_faixa/4folds/0-gen_faixa-4folds-csvc-linear/fold3-analysis.csv"],
            ],
            [
              ["../resultados/Descritores Individuais/LBP-full-gen_faixa/4folds/0-gen_faixa-4folds-csvc-poly/fold0-analysis.csv",
               "../resultados/Descritores Individuais/MFCC50-gen_faixa/4folds/0-gen_faixa-4folds-csvc-poly/fold0-analysis.csv",
               "../resultados/Early Fusion/rh_rp_ssd-gen_faixa/4folds/0-gen_faixa-4folds-csvc-poly/fold0-analysis.csv"],
              ["../resultados/Descritores Individuais/LBP-full-gen_faixa/4folds/0-gen_faixa-4folds-csvc-poly/fold1-analysis.csv",
               "../resultados/Descritores Individuais/MFCC50-gen_faixa/4folds/0-gen_faixa-4folds-csvc-poly/fold1-analysis.csv",
               "../resultados/Early Fusion/rh_rp_ssd-gen_faixa/4folds/0-gen_faixa-4folds-csvc-poly/fold1-analysis.csv"], 
              ["../resultados/Descritores Individuais/LBP-full-gen_faixa/4folds/0-gen_faixa-4folds-csvc-poly/fold2-analysis.csv",
               "../resultados/Descritores Individuais/MFCC50-gen_faixa/4folds/0-gen_faixa-4folds-csvc-poly/fold2-analysis.csv",
               "../resultados/Early Fusion/rh_rp_ssd-gen_faixa/4folds/0-gen_faixa-4folds-csvc-poly/fold2-analysis.csv"],
              ["../resultados/Descritores Individuais/LBP-full-gen_faixa/4folds/0-gen_faixa-4folds-csvc-poly/fold3-analysis.csv",
               "../resultados/Descritores Individuais/MFCC50-gen_faixa/4folds/0-gen_faixa-4folds-csvc-poly/fold3-analysis.csv",
               "../resultados/Early Fusion/rh_rp_ssd-gen_faixa/4folds/0-gen_faixa-4folds-csvc-poly/fold3-analysis.csv"],
            ],
            [
              ["../resultados/Descritores Individuais/LBP-full-gen_faixa/4folds/0-gen_faixa-4folds-csvc-radial/fold0-analysis.csv",
               "../resultados/Descritores Individuais/MFCC50-gen_faixa/4folds/0-gen_faixa-4folds-csvc-radial/fold0-analysis.csv",
               "../resultados/Early Fusion/rh_rp_ssd-gen_faixa/4folds/0-gen_faixa-4folds-csvc-radial/fold0-analysis.csv"],
              ["../resultados/Descritores Individuais/LBP-full-gen_faixa/4folds/0-gen_faixa-4folds-csvc-radial/fold1-analysis.csv",
               "../resultados/Descritores Individuais/MFCC50-gen_faixa/4folds/0-gen_faixa-4folds-csvc-radial/fold1-analysis.csv",
               "../resultados/Early Fusion/rh_rp_ssd-gen_faixa/4folds/0-gen_faixa-4folds-csvc-radial/fold1-analysis.csv"], 
              ["../resultados/Descritores Individuais/LBP-full-gen_faixa/4folds/0-gen_faixa-4folds-csvc-radial/fold2-analysis.csv",
               "../resultados/Descritores Individuais/MFCC50-gen_faixa/4folds/0-gen_faixa-4folds-csvc-radial/fold2-analysis.csv",
               "../resultados/Early Fusion/rh_rp_ssd-gen_faixa/4folds/0-gen_faixa-4folds-csvc-radial/fold2-analysis.csv"],
              ["../resultados/Descritores Individuais/LBP-full-gen_faixa/4folds/0-gen_faixa-4folds-csvc-radial/fold3-analysis.csv",
               "../resultados/Descritores Individuais/MFCC50-gen_faixa/4folds/0-gen_faixa-4folds-csvc-radial/fold3-analysis.csv",
               "../resultados/Early Fusion/rh_rp_ssd-gen_faixa/4folds/0-gen_faixa-4folds-csvc-radial/fold3-analysis.csv"],
            ],
            [
              ["../resultados/Descritores Individuais/LBP-full-gen_faixa/5folds/0-gen_faixa-5folds-csvc-linear/fold0-analysis.csv",
               "../resultados/Descritores Individuais/MFCC50-gen_faixa/5folds/0-gen_faixa-5folds-csvc-linear/fold0-analysis.csv",
               "../resultados/Early Fusion/rh_rp_ssd-gen_faixa/5folds/0-gen_faixa-5folds-csvc-linear/fold0-analysis.csv"],
              ["../resultados/Descritores Individuais/LBP-full-gen_faixa/5folds/0-gen_faixa-5folds-csvc-linear/fold1-analysis.csv",
               "../resultados/Descritores Individuais/MFCC50-gen_faixa/5folds/0-gen_faixa-5folds-csvc-linear/fold1-analysis.csv",
               "../resultados/Early Fusion/rh_rp_ssd-gen_faixa/5folds/0-gen_faixa-5folds-csvc-linear/fold1-analysis.csv"], 
              ["../resultados/Descritores Individuais/LBP-full-gen_faixa/5folds/0-gen_faixa-5folds-csvc-linear/fold2-analysis.csv",
               "../resultados/Descritores Individuais/MFCC50-gen_faixa/5folds/0-gen_faixa-5folds-csvc-linear/fold2-analysis.csv",
               "../resultados/Early Fusion/rh_rp_ssd-gen_faixa/5folds/0-gen_faixa-5folds-csvc-linear/fold2-analysis.csv"],
              ["../resultados/Descritores Individuais/LBP-full-gen_faixa/5folds/0-gen_faixa-5folds-csvc-linear/fold3-analysis.csv",
               "../resultados/Descritores Individuais/MFCC50-gen_faixa/5folds/0-gen_faixa-5folds-csvc-linear/fold3-analysis.csv",
               "../resultados/Early Fusion/rh_rp_ssd-gen_faixa/5folds/0-gen_faixa-5folds-csvc-linear/fold3-analysis.csv"],
              ["../resultados/Descritores Individuais/LBP-full-gen_faixa/5folds/0-gen_faixa-5folds-csvc-linear/fold4-analysis.csv",
               "../resultados/Descritores Individuais/MFCC50-gen_faixa/5folds/0-gen_faixa-5folds-csvc-linear/fold4-analysis.csv",
               "../resultados/Early Fusion/rh_rp_ssd-gen_faixa/5folds/0-gen_faixa-5folds-csvc-linear/fold4-analysis.csv"],
            ],
            [
              ["../resultados/Descritores Individuais/LBP-full-gen_faixa/5folds/0-gen_faixa-5folds-csvc-poly/fold0-analysis.csv",
               "../resultados/Descritores Individuais/MFCC50-gen_faixa/5folds/0-gen_faixa-5folds-csvc-poly/fold0-analysis.csv",
               "../resultados/Early Fusion/rh_rp_ssd-gen_faixa/5folds/0-gen_faixa-5folds-csvc-poly/fold0-analysis.csv"],
              ["../resultados/Descritores Individuais/LBP-full-gen_faixa/5folds/0-gen_faixa-5folds-csvc-poly/fold1-analysis.csv",
               "../resultados/Descritores Individuais/MFCC50-gen_faixa/5folds/0-gen_faixa-5folds-csvc-poly/fold1-analysis.csv",
               "../resultados/Early Fusion/rh_rp_ssd-gen_faixa/5folds/0-gen_faixa-5folds-csvc-poly/fold1-analysis.csv"], 
              ["../resultados/Descritores Individuais/LBP-full-gen_faixa/5folds/0-gen_faixa-5folds-csvc-poly/fold2-analysis.csv",
               "../resultados/Descritores Individuais/MFCC50-gen_faixa/5folds/0-gen_faixa-5folds-csvc-poly/fold2-analysis.csv",
               "../resultados/Early Fusion/rh_rp_ssd-gen_faixa/5folds/0-gen_faixa-5folds-csvc-poly/fold2-analysis.csv"],
              ["../resultados/Descritores Individuais/LBP-full-gen_faixa/5folds/0-gen_faixa-5folds-csvc-poly/fold3-analysis.csv",
               "../resultados/Descritores Individuais/MFCC50-gen_faixa/5folds/0-gen_faixa-5folds-csvc-poly/fold3-analysis.csv",
               "../resultados/Early Fusion/rh_rp_ssd-gen_faixa/5folds/0-gen_faixa-5folds-csvc-poly/fold3-analysis.csv"],
              ["../resultados/Descritores Individuais/LBP-full-gen_faixa/5folds/0-gen_faixa-5folds-csvc-poly/fold4-analysis.csv",
               "../resultados/Descritores Individuais/MFCC50-gen_faixa/5folds/0-gen_faixa-5folds-csvc-poly/fold4-analysis.csv",
               "../resultados/Early Fusion/rh_rp_ssd-gen_faixa/5folds/0-gen_faixa-5folds-csvc-poly/fold4-analysis.csv"],
            ],
            [
              ["../resultados/Descritores Individuais/LBP-full-gen_faixa/5folds/0-gen_faixa-5folds-csvc-radial/fold0-analysis.csv",
               "../resultados/Descritores Individuais/MFCC50-gen_faixa/5folds/0-gen_faixa-5folds-csvc-radial/fold0-analysis.csv",
               "../resultados/Early Fusion/rh_rp_ssd-gen_faixa/5folds/0-gen_faixa-5folds-csvc-radial/fold0-analysis.csv"],
              ["../resultados/Descritores Individuais/LBP-full-gen_faixa/5folds/0-gen_faixa-5folds-csvc-radial/fold1-analysis.csv",
               "../resultados/Descritores Individuais/MFCC50-gen_faixa/5folds/0-gen_faixa-5folds-csvc-radial/fold1-analysis.csv",
               "../resultados/Early Fusion/rh_rp_ssd-gen_faixa/5folds/0-gen_faixa-5folds-csvc-radial/fold1-analysis.csv"], 
              ["../resultados/Descritores Individuais/LBP-full-gen_faixa/5folds/0-gen_faixa-5folds-csvc-radial/fold2-analysis.csv",
               "../resultados/Descritores Individuais/MFCC50-gen_faixa/5folds/0-gen_faixa-5folds-csvc-radial/fold2-analysis.csv",
               "../resultados/Early Fusion/rh_rp_ssd-gen_faixa/5folds/0-gen_faixa-5folds-csvc-radial/fold2-analysis.csv"],
              ["../resultados/Descritores Individuais/LBP-full-gen_faixa/5folds/0-gen_faixa-5folds-csvc-radial/fold3-analysis.csv",
               "../resultados/Descritores Individuais/MFCC50-gen_faixa/5folds/0-gen_faixa-5folds-csvc-radial/fold3-analysis.csv",
               "../resultados/Early Fusion/rh_rp_ssd-gen_faixa/5folds/0-gen_faixa-5folds-csvc-radial/fold3-analysis.csv"],
              ["../resultados/Descritores Individuais/LBP-full-gen_faixa/5folds/0-gen_faixa-5folds-csvc-radial/fold4-analysis.csv",
               "../resultados/Descritores Individuais/MFCC50-gen_faixa/5folds/0-gen_faixa-5folds-csvc-radial/fold4-analysis.csv",
               "../resultados/Early Fusion/rh_rp_ssd-gen_faixa/5folds/0-gen_faixa-5folds-csvc-radial/fold4-analysis.csv"],
            ]
           ] 
saidas = ["../resultados/Late Fusion/LBP-full_MFCC50_EarlyRH-RP-SSD/gen_faixa/4folds/linear/fold0.csv",
          "../resultados/Late Fusion/LBP-full_MFCC50_EarlyRH-RP-SSD/gen_faixa/4folds/linear/fold1.csv",
          "../resultados/Late Fusion/LBP-full_MFCC50_EarlyRH-RP-SSD/gen_faixa/4folds/linear/fold2.csv",
          "../resultados/Late Fusion/LBP-full_MFCC50_EarlyRH-RP-SSD/gen_faixa/4folds/linear/fold3.csv",
          "../resultados/Late Fusion/LBP-full_MFCC50_EarlyRH-RP-SSD/gen_faixa/4folds/poly/fold0.csv",
          "../resultados/Late Fusion/LBP-full_MFCC50_EarlyRH-RP-SSD/gen_faixa/4folds/poly/fold1.csv",
          "../resultados/Late Fusion/LBP-full_MFCC50_EarlyRH-RP-SSD/gen_faixa/4folds/poly/fold2.csv",
          "../resultados/Late Fusion/LBP-full_MFCC50_EarlyRH-RP-SSD/gen_faixa/4folds/poly/fold3.csv",
          "../resultados/Late Fusion/LBP-full_MFCC50_EarlyRH-RP-SSD/gen_faixa/4folds/radial/fold0.csv",
          "../resultados/Late Fusion/LBP-full_MFCC50_EarlyRH-RP-SSD/gen_faixa/4folds/radial/fold1.csv",
          "../resultados/Late Fusion/LBP-full_MFCC50_EarlyRH-RP-SSD/gen_faixa/4folds/radial/fold2.csv",
          "../resultados/Late Fusion/LBP-full_MFCC50_EarlyRH-RP-SSD/gen_faixa/4folds/radial/fold3.csv",
          "../resultados/Late Fusion/LBP-full_MFCC50_EarlyRH-RP-SSD/gen_faixa/5folds/linear/fold0.csv",
          "../resultados/Late Fusion/LBP-full_MFCC50_EarlyRH-RP-SSD/gen_faixa/5folds/linear/fold1.csv",
          "../resultados/Late Fusion/LBP-full_MFCC50_EarlyRH-RP-SSD/gen_faixa/5folds/linear/fold2.csv",
          "../resultados/Late Fusion/LBP-full_MFCC50_EarlyRH-RP-SSD/gen_faixa/5folds/linear/fold3.csv",
          "../resultados/Late Fusion/LBP-full_MFCC50_EarlyRH-RP-SSD/gen_faixa/5folds/linear/fold4.csv",
          "../resultados/Late Fusion/LBP-full_MFCC50_EarlyRH-RP-SSD/gen_faixa/5folds/poly/fold0.csv",
          "../resultados/Late Fusion/LBP-full_MFCC50_EarlyRH-RP-SSD/gen_faixa/5folds/poly/fold1.csv",
          "../resultados/Late Fusion/LBP-full_MFCC50_EarlyRH-RP-SSD/gen_faixa/5folds/poly/fold2.csv",
          "../resultados/Late Fusion/LBP-full_MFCC50_EarlyRH-RP-SSD/gen_faixa/5folds/poly/fold3.csv",
          "../resultados/Late Fusion/LBP-full_MFCC50_EarlyRH-RP-SSD/gen_faixa/5folds/poly/fold4.csv",
          "../resultados/Late Fusion/LBP-full_MFCC50_EarlyRH-RP-SSD/gen_faixa/5folds/radial/fold0.csv",
          "../resultados/Late Fusion/LBP-full_MFCC50_EarlyRH-RP-SSD/gen_faixa/5folds/radial/fold1.csv",
          "../resultados/Late Fusion/LBP-full_MFCC50_EarlyRH-RP-SSD/gen_faixa/5folds/radial/fold2.csv",
          "../resultados/Late Fusion/LBP-full_MFCC50_EarlyRH-RP-SSD/gen_faixa/5folds/radial/fold3.csv",
          "../resultados/Late Fusion/LBP-full_MFCC50_EarlyRH-RP-SSD/gen_faixa/5folds/radial/fold4.csv"
         ]

def extraiClassesEsperadas(arquivo):    
    classes_esperadas = []
    line = arquivo.pop(0)
    while (line != "\n"):
        classes_esperadas.append(line.split(";")[CLASSE_ESPERADA_INDEX])
        line = arquivo.pop(0)
    return classes_esperadas

def getDimensoes(arquivo_dimensoes):
    line = arquivo_dimensoes.pop(0)
    dimensao_coluna = len(line.split(";")) - 2
    dimensao_linha = 0
    while (line != "\n"):
        dimensao_linha = dimensao_linha + 1
        line = arquivo_dimensoes.pop(0)
    return (dimensao_linha,dimensao_coluna)

def processaSoma(matriz_soma,arquivo):
    line = arquivo.pop(0).replace("\n","").replace(",",".").split(";")[2:]
    for l in range(len(matriz_soma)):
        for c in range(len(line)):            
            matriz_soma[l][c] = matriz_soma[l][c] + float(line[c])
        line = arquivo.pop(0).replace("\n","").replace(",",".").split(";")[2:]
    return matriz_soma

def processaMult(matriz_mult,arquivo):
    line = arquivo.pop(0).replace("\n","").replace(",",".").split(";")[2:]
    for l in range(len(matriz_mult)):
        for c in range(len(line)):            
            matriz_mult[l][c] = matriz_mult[l][c] * float(line[c])
        line = arquivo.pop(0).replace("\n","").replace(",",".").split(";")[2:]
    return matriz_mult

def processaMax(matriz_max,arquivo):
    line = arquivo.pop(0).replace("\n","").replace(",",".").split(";")[2:]
    for l in range(len(matriz_max)):
        for c in range(len(line)): 
            matriz_max[l][c] = float(line[c]) if float(line[c]) > matriz_max[l][c] else matriz_max[l][c]
        line = arquivo.pop(0).replace("\n","").replace(",",".").split(";")[2:]           
    return matriz_max

def processaMin(matriz_min,arquivo):
    line = arquivo.pop(0).replace("\n","").replace(",",".").split(";")[2:]
    for l in range(len(matriz_min)):
        for c in range(len(line)): 
            matriz_min[l][c] = float(line[c]) if float(line[c]) < matriz_min[l][c] else matriz_min[l][c]
        line = arquivo.pop(0).replace("\n","").replace(",",".").split(";")[2:]           
    return matriz_min

def processaClassesPreditas(lista_predicoes,cabecalho):
    classes_preditas = []
    for predicoes in lista_predicoes:
        classes_preditas.append(cabecalho[np.argmax(predicoes)])
    return classes_preditas

def calculateConfusionMatrix(expectedList, predictedList):
    numberOfClass = expectedList.max() + 1
    cm = [[0 for i in range(numberOfClass)] for j in range(numberOfClass)]
    for i in range(numberOfClass):
        for j in range(numberOfClass):
            total = 0
            for k in range(len(expectedList)):
                if (expectedList[k] == i) and (predictedList[k] == j):
                    total = total + 1
            cm[i][j] = total
    return cm

def calculatePrecisionRecall(confusionMatrix):
    recalls = []
    for i in range(len(confusionMatrix)):
        recalls.append(float(confusionMatrix[i][i]) / float(confusionMatrix[i].sum()))
    precisions = []
    cmT = np.transpose(confusionMatrix)
    for i in range(len(cmT)):
        precisions.append(0 if cmT[i].sum() == 0 else float(cmT[i][i]) / float(cmT[i].sum()))
    return np.asarray(precisions,dtype=np.float), np.asarray(recalls,dtype=np.float)

def calculateFMeasure(precisions,recalls):
    fMeasures = []
    for i in range(len(precisions)):
        fMeasures.append(0 if precisions[i] + recalls[i] == 0 else (2*precisions[i]*recalls[i])/(precisions[i]+recalls[i]))
    return np.asarray(fMeasures,dtype=np.float)

def geraArquivosAnalise(predicoes,classes_esperadas,caminho_saida):    
    if not os.path.exists(caminho_saida.rpartition("/")[0]):
        os.makedirs(caminho_saida.rpartition("/")[0])    
    arq_saida = open(caminho_saida,"w")
        
    acuracias = []
    macrosF = []
    
    for predicao in predicoes:
        acertos = 0

        #'gambiarra' pra corrigir o problema da ordenacao de classes na classificacao por genero e faixa 
        if "gen_faixa" in caminho_saida:
            cabecalho = "0;2;4;6;1;3;5;7"
        else:
            cabecalho = ";".join("{}".format(i) for i in range(max(classes_esperadas)+1))
        
        classes_preditas = processaClassesPreditas(predicao[0],map(int,cabecalho.split(";")))

        arq_saida.write("{};\n".format(predicao[1]))
        arq_saida.write("esperada;predita;{}".format(cabecalho))
        arq_saida.write("\n")        
        for i in range(len(classes_esperadas)):
            arq_saida.write(str(classes_esperadas[i])+";"+str(classes_preditas[i])+";")
            arq_saida.write(";".join("{}".format(i) for i in predicao[0][i]))
            arq_saida.write("\n")
            acertos = (acertos + 1) if int(classes_esperadas[i]) == classes_preditas[i] else acertos
        acuracias.append(acertos/float(len(classes_esperadas)))
        arq_saida.write("Acuracia;{}\n\n".format(acuracias[-1]))
        
        confusion_matrix = calculateConfusionMatrix(np.asarray(classes_esperadas),np.asarray(classes_preditas))
        precisions,recalls = calculatePrecisionRecall(np.asarray(confusion_matrix))
        fMeasures = calculateFMeasure(precisions, recalls)
        macrosF.append(np.mean(fMeasures))
        arq_saida.write("Matriz de confusao;{};Recall\n".format(cabecalho))
        for i in range(len(confusion_matrix)):
            arq_saida.write(str(i) + ";" + ''.join("{};".format(d) for (i,d) in enumerate(confusion_matrix[i])) + str(recalls[i]) + "\n")
        arq_saida.write("Precision;")
        for i in range(len(confusion_matrix)):
            arq_saida.write(str(precisions[i]) + ";")
        arq_saida.write("\nClasse;F-Measure\n")
        for i in range(len(fMeasures)):
            arq_saida.write(str(i)+";"+str(fMeasures[i])+"\n")
        arq_saida.write("MacroF;"+str(macrosF[-1])+"\n\n")
    arq_saida.close()
    return acuracias,macrosF

def geArquivoResumo(lista_acuracias,lista_macroF,caminho): 
    lista_acuracias = np.asarray(lista_acuracias,dtype="float64")
    lista_macroF = np.asarray(lista_macroF,dtype="float64")
    lista_acuracias = np.transpose(lista_acuracias)
    lista_macroF = np.transpose(lista_macroF)
    caminho = caminho + "resumo.csv"    
    arq = open(caminho,"w")
    arq.write("metodo;acc. media;desvio padrao;macroF media;melhor acc.;fold melhor acc.\n")
    for i in range(len(lista_acuracias)):
        arq.write(METODO[i]+";")
        arq.write(str(np.average(lista_acuracias[i]))+";")
        arq.write(str(np.std(lista_acuracias[i]))+";")
        arq.write(str(np.average(lista_macroF[i]))+";")        
        arq.write(str(np.max(lista_acuracias[i]))+";"+str(np.argmax(lista_acuracias[i]))+"\n")
    arq.close()



for fold in entradas:
    lista_acuracias = []
    lista_macroF = []

    for conjunto_entrada in fold:
        #requerido para inicializacao
        arquivo = open(conjunto_entrada[0],"r")
        lines = arquivo.readlines()
        dimensoes = getDimensoes(lines[4:])
        classes_esperadas = extraiClassesEsperadas(lines[4:])
        predicoes_soma = np.zeros(dimensoes,dtype=np.float64)
        predicoes_mult = np.ones(dimensoes,dtype=np.float64)
        predicoes_max = np.zeros(dimensoes,dtype=np.float64)        
        predicoes_min = np.ones(dimensoes,dtype=np.float64)
        arquivo.close()
        
        for entrada in conjunto_entrada:
            arquivo = open(entrada,"r")
            lines = arquivo.readlines()
            predicoes_soma = processaSoma(predicoes_soma, lines[4:])
            predicoes_mult = processaMult(predicoes_mult, lines[4:])
            predicoes_max = processaMax(predicoes_max,lines[4:])
            predicoes_min = processaMin(predicoes_min,lines[4:])                                                         
            arquivo.close()

        arq_saida = saidas.pop(0)
        acuracias, macrosF = geraArquivosAnalise([[predicoes_soma,"Soma"],[predicoes_mult,"Multiplicacao"],[predicoes_max,"Maximo"],[predicoes_min,"Maximo dos minimos"]],map(int,classes_esperadas),arq_saida)       
        lista_acuracias.append(acuracias)
        lista_macroF.append(macrosF)
    
    geArquivoResumo(lista_acuracias,lista_macroF,arq_saida.rpartition("/")[0]+"/")

        
