import os
import sys
import shutil
from skimage.feature import local_binary_pattern
from skimage import data
import scipy
import cv2
from python_speech_features import mfcc
import scipy.io.wavfile as wav
import numpy as np
np.set_printoptions(suppress=True)

OPC_MFCC = 1
OPC_RP = 2
OPC_EARLY = 3
OPC_LBP = 4
MFCC_DESC = 10

def getDados(caminho,extensao):
    total_arqs = len(os.listdir(caminho))
    arqs = []
    for i in range(total_arqs):
        arqs.append(caminho+str(i+1)+extensao)
    return arqs       

def geraMFCC(arqs,arquivo):
    print "Generating MFCC descriptors..."
    file = open(arquivo,"w")    
    for arq in arqs:
        (rate,sig) = wav.read(arq)
        feature = mfcc(sig,rate,nfft=2048,winlen=0.030,winstep=0.05)
        passo_slice = int(len(feature) / MFCC_DESC)
        feature = feature[::passo_slice,:][:MFCC_DESC,:]
        for ft in feature:
            for cepstral in ft:
                file.write("%f " % cepstral)            
        file.write("\n")
    file.close()
    print "MFCC descriptors Done!"

def geraLBP(arqs,arq_out):
    LBPNeighbors = 8
    LBPRadius = 2
    print "Generating LBP descriptors"
    file = open(arq_out,"w")
    for arq in arqs:
        LBPNeighbors = 8
        LBPRadius = 2
        image = cv2.imread(arq,0)
        lbp_image = local_binary_pattern(image, LBPNeighbors, LBPRadius, 'nri_uniform')
        hist = scipy.stats.itemfreq(lbp_image)
        pattern = np.zeros(59)
        for (i, value) in hist:
            pattern[int(i)] = value
        max_value = np.sum(hist)
        pattern = pattern / max_value
        h_size = pattern.shape[0]
        if h_size != 59:
            print "Tamanho do histograma diferente de 59 para o arquivo " + arq
        for i in range(0,h_size):
            file.write("%f " % pattern[i])
        file.write("\n")
    file.close()


def corrigeRP(arq_original, arq_corrigido):
    print "Corrigindo descritor RP..."
    f_o = open(arq_original,"r")
    f_c = open(arq_corrigido,"w")
    conteudo = f_o.readlines()
    descritores = []
    for linha in conteudo:
        n_linha = linha.replace(","," ").replace(".wav","").partition(" ")
        descritores.append([int(n_linha[0]),n_linha[2]])
    descritores = sorted(descritores, key=lambda descritor: descritor[0])
    for descritor in descritores:
        #print len(descritor[1].split(" "))
        f_c.write(descritor[1])
    f_o.close()
    f_c.close()
    print "Descritor RP corrigido!"

def geraEarlyFusion(arq_descritores,arq_early):
    print "Gerando descritor baseado em Early Fusion"
    f_early = open(arq_early,"w")
    conteudos = []
    for arq in arq_descritores:
        f = open(arq,"r")
        conteudos.append(f.readlines())        
        f.close()
    for linha in range(len(conteudos[0])):
        conteudo_linha = ""
        for conteudo in conteudos:
            conteudo_linha += conteudo[linha].replace("\n","").replace("\r","") + " "
        f_early.write(conteudo_linha.rpartition(" ")[0]+"\n")
    f_early.close()
    print "Descritor gerado!"



caminho_spec = "/home/svaigen/tic-genero-faixaetaria/spectrograms-ver-z2/"
caminho_audio = "../audios_wav/"

arqs = getDados(caminho_spec,".png")
desc_opc = OPC_EARLY

if desc_opc == OPC_MFCC:
    geraMFCC(arqs,"../mfcc/mfcc.txt")
elif desc_opc == OPC_RP:
    corrigeRP("../descritores/rp.txt","../descritores/rp_corrigido.txt")
elif desc_opc == OPC_EARLY:
    geraEarlyFusion(["../descritores/mfcc50.txt","../descritores/early_lbp_rh_rp_ssd.txt"],"../descritores/early_mfcc_lbp_rh_rp_ssd.txt")
elif desc_opc == OPC_LBP:
    geraLBP(arqs,"../descritores/lbp-ver-z2.txt")