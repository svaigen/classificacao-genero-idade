import math
from scipy.io import wavfile

import os

DIR_AUDIOS = "audios_wav/"
audios = os.listdir(DIR_AUDIOS)
t_audios = len(audios)

total = 0
masculino = 0
feminino = 0
fem_1 = 0
fem_2 = 0
fem_3 = 0
fem_4 = 0
masc_1 = 0
masc_2 = 0
masc_3 = 0
masc_4 = 0
faixa_1 = 0
faixa_2 = 0
faixa_3 = 0
faixa_4 = 0
trecho_1 = 0
trecho_2 = 0
trecho_3 = 0
trecho_4 = 0
trecho_5 = 0

def isTrecho(i, trecho):
    resto = i % 5
    if resto == trecho:
        return True
    else:
        return False

def isFaixa(i, faixa):
    div = i // 100
    div = div + 1
    if div == faixa:
        return True
    else:
        return False

def isMaculino(i):
    div = i // 50
    resto = div % 2
    if resto == 0:
        return True
    else:
        return False

for i in range(1, 401):
    pos = i - 1
    fname = DIR_AUDIOS + str(i) + ".wav"
    audio = wavfile.read(fname)
    duration = len(audio[1]) / audio[0]
    segundos = math.floor(duration)
    masc = isMaculino(pos)
    f_1 = isFaixa(pos, 1)
    f_2 = isFaixa(pos, 2)
    f_3 = isFaixa(pos, 3)
    f_4 = isFaixa(pos, 4)
    #print("Audio " + str(i) + ": " + str(segundos) + " segundos " + str(masc) + "//" + str(f_1) + str(f_2) + str(f_3) + str(f_4))
    total = total + segundos
    if(masc):
        masculino = masculino + segundos
    else:
        feminino = feminino + segundos

    if(isTrecho(pos, 0)):
        trecho_1 = trecho_1 + segundos
    elif(isTrecho(pos, 1)):
        trecho_2 = trecho_2 + segundos
    elif(isTrecho(pos, 2)):
        trecho_3 = trecho_3 + segundos
    elif(isTrecho(pos, 3)):
        trecho_4 = trecho_4 + segundos
    elif(isTrecho(pos, 4)):
        trecho_5 = trecho_5 + segundos

    if(f_1):
        faixa_1 = faixa_1 + segundos
    if(f_2):
        faixa_2 = faixa_2 + segundos
    if(f_3):
        faixa_3 = faixa_3 + segundos
    if(f_4):
        faixa_4 = faixa_4 + segundos

    if(f_1 and masc):
        masc_1 = masc_1 + segundos
    if (f_1 and not masc):
        fem_1 = fem_1 + segundos
    if(f_2 and masc):
        masc_2 = masc_2 + segundos
    if (f_2 and not masc):
        fem_2 = fem_2 + segundos
    if(f_3 and masc):
        masc_3 = masc_3 + segundos
    if (f_3 and not masc):
        fem_3 = fem_3 + segundos
    if(f_4 and masc):
        masc_4 = masc_4 + segundos
    if (f_4 and not masc):
        fem_4 = fem_4 + segundos

f = open("duracao.csv", "w")
f.write("total\t\t" + str(total) + "\t\t" + str(total/60) + "\t\t" + str(total/3600) + "\n")
f.write("masc\t\t" + str(masculino) + "\t\t" + str(masculino/60) + "\t\t" + str(masculino/3600) + "\n")
f.write("femin\t\t" + str(feminino) + "\t\t" + str(feminino/60) + "\t\t" + str(feminino/3600) + "\n")
f.write("faixa1\t\t" + str(faixa_1) + "\t\t" + str(faixa_1/60) + "\t\t" + str(faixa_1/3600) + "\n")
f.write("faixa2\t\t" + str(faixa_2) + "\t\t" + str(faixa_2/60) + "\t\t" + str(faixa_2/3600) + "\n")
f.write("faixa3\t\t" + str(faixa_3) + "\t\t" + str(faixa_3/60) + "\t\t" + str(faixa_3/3600) + "\n")
f.write("faixa4\t\t" + str(faixa_4) + "\t\t" + str(faixa_4/60) + "\t\t" + str(faixa_4/3600) + "\n")
f.write("masc_1\t\t" + str(masc_1) + "\t\t" + str(masc_1/60) + "\t\t" + str(masc_1/3600) + "\n")
f.write("masc_2\t\t" + str(masc_2) + "\t\t" + str(masc_2/60) + "\t\t" + str(masc_2/3600) + "\n")
f.write("masc_3\t\t" + str(masc_3) + "\t\t" + str(masc_3/60) + "\t\t" + str(masc_3/3600) + "\n")
f.write("masc_4\t\t" + str(masc_4) + "\t\t" + str(masc_4/60) + "\t\t" + str(masc_4/3600) + "\n")
f.write("fem_1\t\t" + str(fem_1) + "\t\t" + str(fem_1/60) + "\t\t" + str(fem_1/3600) + "\n")
f.write("fem_2\t\t" + str(fem_2) + "\t\t" + str(fem_2/60) + "\t\t" + str(fem_2/3600) + "\n")
f.write("fem_3\t\t" + str(fem_3) + "\t\t" + str(fem_3/60) + "\t\t" + str(fem_3/3600) + "\n")
f.write("fem_4\t\t" + str(fem_4) + "\t\t" + str(fem_4/60) + "\t\t" + str(fem_4/3600) + "\n")
f.close()

print("TOTAL : " + str(total))
print("CONF GEN : " + str(masculino + feminino))
print("CONF FAIXA : " + str(faixa_1 + faixa_2 + faixa_3 + faixa_4))
print("CONF GEN E FAIXA: " + str(masc_1 + masc_2 + masc_3 + masc_4 + fem_1 + fem_2 + fem_3 + fem_4))
print("CON TRECHO : " + str(trecho_1 + trecho_2 + trecho_3 + trecho_4 + trecho_5))
print("MASCULINO : " + str(masculino))
print("FEMININO : " + str(feminino))
print("FAIXA 1 : " + str(faixa_1))
print("FAIXA 2 : " + str(faixa_2))
print("FAIXA 3 : " + str(faixa_3))
print("FAIXA 4 : " + str(faixa_4))
print("MASCULINO E FAIXA 1 : " + str(masc_1))
print("MASCULINO E FAIXA 2 : " + str(masc_2))
print("MASCULINO E FAIXA 3 : " + str(masc_3))
print("MASCULINO E FAIXA 4 : " + str(masc_4))
print("FEMININO E FAIXA 1 : " + str(fem_1))
print("FEMININO E FAIXA 2 : " + str(fem_2))
print("FEMININO E FAIXA 3 : " + str(fem_3))
print("FEMININO E FAIXA 4 : " + str(fem_4))
print("TRECHO 1 : " + str(trecho_1) + " -- " + str(trecho_1/80))
print("TRECHO 2 : " + str(trecho_2) + " -- " + str(trecho_2/80))
print("TRECHO 3 : " + str(trecho_3) + " -- " + str(trecho_3/80))
print("TRECHO 4 : " + str(trecho_4) + " -- " + str(trecho_4/80))
print("TRECHO 5 : " + str(trecho_5) + " -- " + str(trecho_5/80))