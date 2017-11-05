'''
DESCRITOR   PESSOA  FAIXA_ETARIA    GENERO
0..49       0..9    0-14            MASC
50..99      10..19  0-14            FEM
100..149    20..29  15-24           MASC
150..199    30..39  15-24           FEM
200..249    40..49  25-54           MASC
250..299    50..59  25-54           FEM
300..349    60..69  55-++           MASC
350..399    70..79  55-++           FEM
'''

import os
import sys
import shutil
import random

AMOSTRAS_POR_PESSOA = 5
NUM_FOLDS = 4
CLASS_GENERO = 1
CLASS_FAIXA = 2
CLASS_GEN_FAIXA = 3

arq_descritor = "../mfcc/mfcc.txt"
diretorio_folds = "../folds/"
def getDescritores(arquivo):
    arq = open(arquivo,"r")
    lines = arq.readlines()
    descritores = []
    pessoas_descritores = []
    for l in range(len(lines)):
        padroes = lines[l].split(" ")
        for n in range(len(padroes)-1): #o -1 faz com que nao seja atribuido nada para o \n
            padroes[n] = "{}:".format(n) + padroes[n]
        descritores.append(padroes)
        if ((l+1) % AMOSTRAS_POR_PESSOA == 0):
            pessoas_descritores.append([int(l/AMOSTRAS_POR_PESSOA),descritores])
            descritores = []
    arq.close()
    return pessoas_descritores
    
def geraFolds(pessoas_descritores,num_folds,tipo_class):
    print("Gerando folds...")
    arq_folds = []
    for i in range(num_folds):
        arq_folds.append(diretorio_folds+"fold"+str(i)+".txt")    
    
    if tipo_class == CLASS_GENERO:
        classe_masc = []
        classe_fem  = []
        
        for pessoa in pessoas_descritores:
            if (pessoa[0]<10) or (pessoa[0]>19 and pessoa[0]<30) or (pessoa[0]>39 and pessoa[0]<50) or (pessoa[0]>59 and pessoa[0]<70):
                classe_masc.append(pessoa)
            else:
                classe_fem.append(pessoa)
        random.shuffle(classe_masc)
        random.shuffle(classe_fem)
        pessoas_classe_por_fold = int(len(classe_masc)/len(arq_folds))

        for n_fold in range(len(arq_folds)):
            init_index = n_fold * pessoas_classe_por_fold
            end_index = (n_fold+1) * pessoas_classe_por_fold
            arq = open(arq_folds[n_fold],"w")
            for pessoa in range(init_index,end_index):
                for descritor in classe_masc[pessoa][1]:
                    arq.write("0") #Classe 0 : masculino
                    for padrao in descritor:
                        arq.write(" "+padrao)
                for descritor in classe_fem[pessoa][1]:
                    arq.write("1") #Classe 1 : feminino
                    for padrao in descritor:
                        arq.write(" "+padrao)                        
            arq.close()
    
    if tipo_class == CLASS_FAIXA:
        classe_0_14 = []
        classe_15_24 = []
        classe_25_54 = []
        classe_54_mais = []
        
        for pessoa in pessoas_descritores:
            if (pessoa[0]<20):
                classe_0_14.append(pessoa)
            elif (pessoa[0]<40):
                classe_15_24.append(pessoa)
            elif (pessoa[0]<60):
                classe_25_54.append(pessoa)
            else:
                classe_54_mais.append(pessoa)
            
        random.shuffle(classe_0_14)
        random.shuffle(classe_15_24)
        random.shuffle(classe_25_54)
        random.shuffle(classe_54_mais)
        pessoas_classe_por_fold = int(len(classe_0_14)/len(arq_folds))

        for n_fold in range(len(arq_folds)):
            init_index = n_fold * pessoas_classe_por_fold
            end_index = (n_fold+1) * pessoas_classe_por_fold
            arq = open(arq_folds[n_fold],"w")
            for pessoa in range(init_index,end_index):
                for descritor in classe_0_14[pessoa][1]:
                    arq.write("0") #Classe 0 : 0_14
                    for padrao in descritor:
                        arq.write(" "+padrao)
                for descritor in classe_15_24[pessoa][1]:
                    arq.write("1") #Classe 1 : 15_24
                    for padrao in descritor:
                        arq.write(" "+padrao)
                for descritor in classe_25_54[pessoa][1]:
                    arq.write("2") #Classe 2 : 25_54
                    for padrao in descritor:
                        arq.write(" "+padrao)
                for descritor in classe_54_mais[pessoa][1]:
                    arq.write("3") #Classe 3 : 54_mais
                    for padrao in descritor:
                        arq.write(" "+padrao)                        
            arq.close()

    if tipo_class == CLASS_GEN_FAIXA:
        classe_0_14_masc = []
        classe_0_14_fem = []
        classe_15_24_masc = []
        classe_15_24_fem = []
        classe_25_54_masc = []
        classe_25_54_fem = []
        classe_54_mais_masc = []
        classe_54_mais_fem = []
        
        for pessoa in pessoas_descritores:
            if (pessoa[0]<10):
                classe_0_14_masc.append(pessoa)
            elif (pessoa[0]<20):
                classe_0_14_fem.append(pessoa)
            elif (pessoa[0]<30):
                classe_15_24_masc.append(pessoa)
            elif (pessoa[0]<40):
                classe_15_24_fem.append(pessoa)
            elif (pessoa[0]<50):
                classe_25_54_masc.append(pessoa)
            elif (pessoa[0]<60):
                classe_25_54_fem.append(pessoa)
            elif (pessoa[0]<70):
                classe_54_mais_masc.append(pessoa)
            else:
                classe_54_mais_fem.append(pessoa)
            
        random.shuffle(classe_0_14_masc)
        random.shuffle(classe_0_14_fem)
        random.shuffle(classe_15_24_masc)
        random.shuffle(classe_15_24_fem)
        random.shuffle(classe_25_54_masc)
        random.shuffle(classe_25_54_fem)
        random.shuffle(classe_54_mais_masc)
        random.shuffle(classe_54_mais_fem)

        pessoas_classe_por_fold = int(len(classe_0_14_masc)/len(arq_folds))

        for n_fold in range(len(arq_folds)):
            init_index = n_fold * pessoas_classe_por_fold
            end_index = (n_fold+1) * pessoas_classe_por_fold
            arq = open(arq_folds[n_fold],"w")
            for pessoa in range(init_index,end_index):
                for descritor in classe_0_14_masc[pessoa][1]:
                    arq.write("0") #Classe 0 : 0_14_masc
                    for padrao in descritor:
                        arq.write(" "+padrao)
                for descritor in classe_0_14_fem[pessoa][1]:
                    arq.write("1") #Classe 1 : 0_14_fem
                    for padrao in descritor:
                        arq.write(" "+padrao)
                for descritor in classe_15_24_masc[pessoa][1]:
                    arq.write("2") #Classe 2 : 15_24_masc
                    for padrao in descritor:
                        arq.write(" "+padrao)
                for descritor in classe_15_24_fem[pessoa][1]:
                    arq.write("3") #Classe 3 : 15_24_fem
                    for padrao in descritor:
                        arq.write(" "+padrao)
                for descritor in classe_25_54_masc[pessoa][1]:
                    arq.write("4") #Classe 4 : 25_54_masc
                    for padrao in descritor:
                        arq.write(" "+padrao)
                for descritor in classe_25_54_fem[pessoa][1]:
                    arq.write("5") #Classe 5 : 25_54_fem
                    for padrao in descritor:
                        arq.write(" "+padrao)
                for descritor in classe_54_mais_masc[pessoa][1]:
                    arq.write("6") #Classe 6 : 54_mais_masc
                    for padrao in descritor:
                        arq.write(" "+padrao)
                for descritor in classe_54_mais_fem[pessoa][1]:
                    arq.write("7") #Classe 0 : 54_mais_fem
                    for padrao in descritor:
                        arq.write(" "+padrao)
                                        
            arq.close()

    print("Folds gerados!")
    
pessoas_descritores = getDescritores(arq_descritor)
geraFolds(pessoas_descritores,NUM_FOLDS,CLASS_GENERO)