# -*- coding: utf-8 -*-
"""
Created on Thu Sep 25 12:41:07 2025
Don Sauron
@author: JulianCastillo
"""
import random as rnd
import matplotlib.pyplot as plt
from tqdm import tqdm
import statistics as st

eArqueroMin, eArqueroMax = 95,105
eGuerreroMin, eGuerreroMax = 125,153
ePortadorMagiaMin, ePortadorMagiaMax = 175,201
eArtesanoMin, eArtesanoMax = 50,63
eLiderMin, eLiderMax = 300,413

hEliteMin, hEliteMax = 100,123
hLiderMin, hLiderMax = 150,177
hExploradorMin, hExploradorMax = 90, 109
hArtesanoMin, hArtesanoMax = 23,88
hSabioMin, hSabioMax = 35,51

def DonSauron():
    danioTotal = {'Elfo':[], 'Hombre':[], 'Golpes':0}
    totalPoblacion = int(rnd.uniform(0.10,0.15)*60_000)
    for i in range(totalPoblacion):
        #aca inicia el modelo.
        x = rnd.random()
        if x > 0.55:
            #aca hay elfos
            y = rnd.random() #vamos a evaluar el tipo de elfo
            z = rnd.random() #vamos a evaluar si lo golpea o no
            if z < 1/5:
                #hay un ataque
                if y > 0.6:
                    arquero = rnd.randint(eArqueroMin,eArqueroMax)
                    danioTotal['Elfo'].append(arquero)
                elif y > 0.3:
                    guerrero = rnd.randint(eGuerreroMin, eGuerreroMax)
                    danioTotal['Elfo'].append(guerrero)
                elif y > 0.2:
                    portadormagia = rnd.randint(ePortadorMagiaMin, ePortadorMagiaMax)
                    danioTotal['Elfo'].append(portadormagia)
                elif y > 0.05:
                    artesano = rnd.randint(eArtesanoMin, eArtesanoMax)
                    danioTotal['Elfo'].append(artesano)
                else:
                    lider = rnd.randint(eLiderMin, eLiderMax)
                    danioTotal['Elfo'].append(lider)
                danioTotal['Golpes']+=1
            else:
                #no hay un ataque y la magia de Sauron lo salva
                danioTotal['Elfo'].append(0)
        else:
            #aca hay humanos
            y = rnd.random()
            z = rnd.random()
            if z < 1/5:
                #hay un ataque
                if y > 0.5:
                    elite = rnd.randint(hEliteMin, hEliteMax)
                    danioTotal['Hombre'].append(elite)
                elif y > 0.4:
                    liderh = rnd.randint(hLiderMin, hLiderMax)
                    danioTotal['Hombre'].append(liderh)
                elif y > 0.25:
                    explorador = rnd.randint(hExploradorMin, hExploradorMax)
                    danioTotal['Hombre'].append(explorador)
                elif y > 0.15:
                    artesanoh = rnd.randint(hArtesanoMin, hArtesanoMax)
                    danioTotal['Hombre'].append(artesanoh)
                else:
                    sabio = rnd.randint(hSabioMin, hSabioMax)
                    danioTotal['Hombre'].append(sabio) 
                danioTotal['Golpes']+=1
            else:
                #no hay ataque
                danioTotal['Hombre'].append(0)
    return danioTotal
x = DonSauron()

# Convergencia --------------------------------------------------------------------------------------------------------
replics = 1000
vEstimationE = []
vEstimationH = []
vMeanE = []
vMeanH = []
for i in tqdm(range(replics), 'Calculando replicas...'):
    elfo_humano = DonSauron()
    elfo = sum(elfo_humano['Elfo'])
    humano = sum(elfo_humano['Hombre'])
    vEstimationE.append(elfo)
    vMeanE.append(st.mean(vEstimationE))
    vEstimationH.append(humano)
    vMeanH.append(st.mean(vEstimationH))


plt.figure(figsize=(5,5))
plt.plot(vMeanE, color='blue', label='Promedio (Convergencia)')
plt.plot(vMeanH, color='purple', label='Promedio (Convergencia)')
plt.axhline(vMeanE[-1], color='red', alpha=0.5, label=f'Promedio {vMeanE[-1]:,.0f}')
plt.axhline(vMeanH[-1], color='red', alpha=0.5, label=f'Promedio {vMeanH[-1]:,.0f}')

plt.grid('on')
plt.title(f'Convergencia del promedio para {replics:,} replicas')
plt.legend()
plt.show()
        
        
        
        
        
        
        
        
        
        
        
    