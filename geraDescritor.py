import os
import sys
import shutil
from python_speech_features import mfcc
import scipy.io.wavfile as wav
import numpy as np
np.set_printoptions(suppress=True)

OPC_MFCC = 1
MFCC_DESC = 100

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

caminho_spec = "../spectrograms/60/"
caminho_audio = "../audios_wav/"

arqs = getDados(caminho_audio,".wav")
desc_opc = OPC_MFCC
if desc_opc == OPC_MFCC:
    geraMFCC(arqs,"../mfcc/mfcc.txt")