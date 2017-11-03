import os
import sys
import shutil
from python_speech_features import mfcc
import scipy.io.wavfile as wav

OPC_MFCC = 1

def getDados(caminho,extensao):
    total_arqs = len(os.listdir(caminho))
    arqs = []
    for i in range(total_arqs):
        arqs.append(caminho+str(i+1)+extensao)
    return arqs       

def geraMFCC(arqs,diretorio):
    print("Generating MFCC descriptors...")

    if os.path.exists(diretorio):
        shutil.rmtree(diretorio)
    os.makedirs(diretorio)

    mfcc_feat = []
    for arq in arqs:
        script = "sox --i -D "+arq)
        (rate,sig) = wav.read(arq)
        mfcc_feat.append(mfcc(sig,rate,nfft=2048))

caminho_spec = "../spectrograms/60/"
caminho_audio = "../audios_wav/"

arqs = getDados(caminho_audio,".wav")
desc_opc = OPC_MFCC
if desc_opc == OPC_MFCC:
    geraMFCC(arqs,"../mfcc/")