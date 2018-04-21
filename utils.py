import os
import sys
import shutil
from skimage.feature import local_binary_pattern
from skimage import data
import scipy
import numpy as np
import cv2
import random
from itertools import cycle
np.set_printoptions(suppress=True)

OPC_ZONEAMENTO_HORIZONTAL = 1
OPC_ZONEAMENTO_VERTICAL = 2
OPC_SORTEIA_FOLDS = 3

TIPO_CLASS_GENERO = 1
TIPO_CLASS_FAIXA = 2
TIPO_CLASS_GEN_FAIXA = 3

caminho_spec_full = "/home/svaigen/tic-genero-faixaetaria/spectrograms/"
caminho_spec_hor = "/home/svaigen/tic-genero-faixaetaria/spectrograms-hor-"
caminho_spec_ver = "/home/svaigen/tic-genero-faixaetaria/spectrograms-ver-"

caminho_arq_fold = "/home/svaigen/tic-genero-faixaetaria/folds/especificacao/gen_faixa-4.txt"
num_folds = 4
tipo_class = TIPO_CLASS_GEN_FAIXA

num_zonas = 3
opc = OPC_SORTEIA_FOLDS

def getDados(caminho,extensao):
    total_arqs = len(os.listdir(caminho))
    arqs = []
    for i in range(total_arqs):
        arqs.append(caminho+str(i+1)+extensao)
    return arqs  

def zoneamento_horizontal(arqs,caminho_hor,num_zonas):
    for i in range(0,num_zonas):
        if not os.path.exists(caminho_hor):
            os.makedirs(caminho_hor+"z"+str(i)+"/")
    count = 0
    for arq in arqs:
        count = count + 1
        img = cv2.imread(arq,cv2.IMREAD_COLOR)
        for i in range(num_zonas):
            fatia = img.shape[0] / num_zonas
            imgresult = img[fatia*i:fatia*(i+1),:,:]
            cv2.imwrite(caminho_hor+"z"+str(i)+"/"+str(count)+".png",imgresult)

def zoneamento_vertical(arqs,caminho_vert, num_zonas):
    for i in range(0,num_zonas):
        if not os.path.exists(caminho_vert):
            os.makedirs(caminho_vert+"z"+str(i)+"/")
    count = 0
    for arq in arqs:
        count = count + 1
        img = cv2.imread(arq,cv2.IMREAD_COLOR)
        for i in range(num_zonas):
            fatia = img.shape[1] / num_zonas
            imgresult = img[:,fatia*i:fatia*(i+1),:]
            cv2.imwrite(caminho_vert+"z"+str(i)+"/"+str(count)+".png",imgresult)

def sorteia_folds(num_folds,tipo_class,num_pessoas,caminho_arq):
    arq = open(caminho_arq,"w")
    pool_fold = []
    folds = [{} for i in range(num_folds)]

    for i in range (0,num_folds):
        pool_fold.append(str(i))
        folds[i] = []
    pool_fold = cycle(pool_fold)

    if tipo_class == TIPO_CLASS_GENERO:
        bucket_masc = ['0','1','2','3','4','5','6','7','8','9','20','21','22','23','24','25','26','27','28','29','40','41','42','43','44','45','46','47','48','49','60','61','62','63','64','65','66','67','68','69']
        bucket_fem = ['10','11','12','13','14','15','16','17','18','19','30','31','32','33','34','35','36','37','38','39','50','51','52','53','54','55','56','57','58','59','70','71','72','73','74','75','76','77','78','79']
        random.shuffle(bucket_masc)
        random.shuffle(bucket_fem)    
        while(bucket_masc and bucket_fem):
            fold_insert = next(pool_fold)        
            folds[int(fold_insert)].append(bucket_masc.pop(0))
            folds[int(fold_insert)].append(bucket_fem.pop(0))

    elif tipo_class == TIPO_CLASS_FAIXA:
        bucket_0_14 = ['0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19']
        bucket_15_24 = ['20','21','22','23','24','25','26','27','28','29','30','31','32','33','34','35','36','37','38','39']
        bucket_25_54 = ['40','41','42','43','44','45','46','47','48','49','50','51','52','53','54','55','56','57','58','59']
        bucket_55_mais = ['60','61','62','63','64','65','66','67','68','69','70','71','72','73','74','75','76','77','78','79']
        random.shuffle(bucket_0_14)
        random.shuffle(bucket_15_24)
        random.shuffle(bucket_25_54)
        random.shuffle(bucket_55_mais)
        while(bucket_0_14 and bucket_15_24 and bucket_25_54 and bucket_55_mais):
            fold_insert = next(pool_fold)
            folds[int(fold_insert)].append(bucket_0_14.pop(0))
            folds[int(fold_insert)].append(bucket_15_24.pop(0))
            folds[int(fold_insert)].append(bucket_25_54.pop(0))
            folds[int(fold_insert)].append(bucket_55_mais.pop(0))
    
    elif tipo_class == TIPO_CLASS_GEN_FAIXA:
        bucket_masc_0_14 = ['0','1','2','3','4','5','6','7','8','9']
        bucket_fem_0_14 = ['10','11','12','13','14','15','16','17','18','19']
        bucket_masc_15_24 = ['20','21','22','23','24','25','26','27','28','29']
        bucket_fem_15_24 = ['30','31','32','33','34','35','36','37','38','39']
        bucket_masc_25_54 = ['40','41','42','43','44','45','46','47','48','49']
        bucket_fem_25_54 = ['50','51','52','53','54','55','56','57','58','59']
        bucket_masc_55_mais = ['60','61','62','63','64','65','66','67','68','69']
        bucket_fem_55_mais = ['70','71','72','73','74','75','76','77','78','79']
        random.shuffle(bucket_masc_0_14)
        random.shuffle(bucket_masc_15_24)
        random.shuffle(bucket_masc_25_54)
        random.shuffle(bucket_masc_55_mais)
        random.shuffle(bucket_fem_0_14)
        random.shuffle(bucket_fem_15_24)
        random.shuffle(bucket_fem_25_54)
        random.shuffle(bucket_fem_55_mais)
        while(bucket_masc_0_14 and bucket_masc_15_24 and bucket_masc_25_54 and bucket_masc_55_mais and bucket_fem_0_14 and bucket_fem_15_24 and bucket_fem_25_54 and bucket_fem_55_mais):
            fold_insert = next(pool_fold)
            folds[int(fold_insert)].append(bucket_masc_0_14.pop(0))
            folds[int(fold_insert)].append(bucket_masc_15_24.pop(0))
            folds[int(fold_insert)].append(bucket_masc_25_54.pop(0))
            folds[int(fold_insert)].append(bucket_masc_55_mais.pop(0))
            folds[int(fold_insert)].append(bucket_fem_0_14.pop(0))
            folds[int(fold_insert)].append(bucket_fem_15_24.pop(0))
            folds[int(fold_insert)].append(bucket_fem_25_54.pop(0))
            folds[int(fold_insert)].append(bucket_fem_55_mais.pop(0))

    for fold in folds:
        for elem in fold:
            arq.write(elem + " ")
        arq.write("\n")

    arq.close()

#main
arqs = getDados(caminho_spec_full,".png")
if opc == OPC_ZONEAMENTO_HORIZONTAL:
    zoneamento_horizontal(arqs,caminho_spec_hor,num_zonas)
elif opc == OPC_ZONEAMENTO_VERTICAL:
    zoneamento_vertical(arqs,caminho_spec_ver,num_zonas)
elif opc == OPC_SORTEIA_FOLDS:
    sorteia_folds(num_folds,tipo_class,40,caminho_arq_fold)