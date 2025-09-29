# -*- coding: utf-8 -*-
"""
Created on Fri Sep 26 07:53:32 2025

@author: JulianCastillo
"""

import random as rnd
import matplotlib.pyplot as plt
from tqdm import tqdm
import statistics as st
#Mi supuesto es evaluar la cantidad de lunes no festivos y martes y mierciles y jueves y viernes de los 
#meses que don manimal necesita evaluar.

def TiendaManimal():
    dias = {'Lunes':10,
            'Martes':13,
            'Miercoles':13,
            'Jueves':11,
            'Viernes':12,
            }
    compras = {'Lunes':[],
            'Martes':[],
            'Miercoles':[],
            'Jueves':[],
            'Viernes':[],
            }
    for llave, valor in dias.items():
        match llave:
            case 'Lunes':
                for i in range(dias[llave]):
                    usuarios = rnd.randint(22,33)
                    for j in range(usuarios):
                        p = rnd.random()
                        if p > 0.75:
                            venta = rnd.randint(25000,175000)
                            compras[llave].append(venta)
                        elif p > 0.6:
                            venta = rnd.randint(20000,55000)
                            compras[llave].append(venta)
                        elif p > 0.5:
                            venta = rnd.randint(25000,175000)
                            compras[llave].append(venta)
                            venta = rnd.randint(20000,55000)
                            compras[llave].append(venta)
                        elif p > 0.2:
                            venta = rnd.randint(50000,250000)
                            compras[llave].append(venta)
                        else:
                            venta = rnd.randint(10000,220000)
                            compras[llave].append(venta)
            case 'Martes':
                for i in range(dias[llave]):
                    usuarios = rnd.randint(22,33)
                    for j in range(usuarios):
                        p = rnd.random()
                        if p > 0.75:
                            venta = rnd.randint(25000,175000)
                            compras[llave].append(venta)
                        elif p > 0.6:
                            venta = rnd.randint(20000,55000)
                            compras[llave].append(venta)
                        elif p > 0.9:
                            venta = rnd.randint(25000,175000)
                            compras[llave].append(venta)
                            venta = rnd.randint(20000,55000)
                            compras[llave].append(venta)
                        elif p > 0.2:
                            venta = rnd.randint(50000,250000)
                            compras[llave].append(venta)
                        else:
                            venta = rnd.randint(10000,220000)
                            compras[llave].append(venta)
            case 'Miercoles':
                for i in range(dias[llave]):
                    usuarios = rnd.randint(30,52)
                    for j in range(usuarios):
                        p = rnd.random()
                        if p > 0.75:
                            venta = rnd.randint(25000,175000)
                            compras[llave].append(venta)
                        elif p > 0.6:
                            venta = rnd.randint(20000,55000)
                            compras[llave].append(venta)
                        elif p > 0.9:
                            venta = rnd.randint(25000,175000)
                            compras[llave].append(venta)
                            venta = rnd.randint(20000,55000)
                            compras[llave].append(venta)
                        elif p > 0.2:
                            venta = rnd.randint(50000,250000)
                            compras[llave].append(venta)
                        else:
                            venta = rnd.randint(10000,220000)
                            compras[llave].append(venta)
            case 'Jueves':
                for i in range(dias[llave]):
                    usuarios = rnd.randint(30,52)
                    for j in range(usuarios):
                        p = rnd.random()
                        if p > 0.75:
                            venta = rnd.randint(25000,175000)
                            compras[llave].append(venta)
                        elif p > 0.6:
                            venta = rnd.randint(20000,55000)
                            compras[llave].append(venta)
                        elif p > 0.9:
                            venta = rnd.randint(25000,175000)
                            compras[llave].append(venta)
                            venta = rnd.randint(20000,55000)
                            compras[llave].append(venta)
                        elif p > 0.2:
                            venta = rnd.randint(50000,250000)
                            compras[llave].append(venta)
                        else:
                            venta = rnd.randint(10000,220000)
                            compras[llave].append(venta)
            case 'Viernes':
                for i in range(dias[llave]):
                    usuarios = rnd.randint(40,65)
                    for j in range(usuarios):
                        p = rnd.random()
                        if p > 0.75:
                            venta = rnd.randint(25000,175000)
                            compras[llave].append(venta)
                        elif p > 0.6:
                            venta = rnd.randint(20000,55000)
                            compras[llave].append(venta)
                        elif p > 0.9:
                            venta = rnd.randint(25000,175000)
                            compras[llave].append(venta)
                            venta = rnd.randint(20000,55000)
                            compras[llave].append(venta)
                        elif p > 0.2:
                            venta = rnd.randint(50000,250000)
                            compras[llave].append(venta)
                        else:
                            venta = rnd.randint(10000,220000)
                            compras[llave].append(venta)
    return compras
      
compras = TiendaManimal()
tresmeses = 0
for llave,valor in compras.items():
    tresmeses += sum(valor)
    print(f'Ventas estimadas para {llave}, \n\t-->${sum(valor):,.0f}')
print(f'Ventas Estimadas para los tres meses ${tresmeses:,.0f}')
print('Nota, este valor es para una sola simulación, no es promedio o convergencia, ver convergencia a continuación')

replics = 100
vEstimation = []
vMean = []
for i in tqdm(range(replics), 'Calculando replicas...'):
    compras = TiendaManimal()
    tresmeses = 0
    for llave,valor in compras.items():
        tresmeses += sum(valor)
    vEstimation.append(tresmeses)
    vMean.append(st.mean(vEstimation))
vMeanR=vMean.copy()
vMeanR.reverse()
ts = vMean[-1]*1.005
ti = vMean[-1]*0.995
convergencia = 0
for j, k in enumerate(vMeanR):
    if k > ti and k < ts:
        pass
    else:
        convergencia = len(vMean)- j
        break

print(f'La convergencia inicia en {convergencia}')
plt.figure(figsize=(5,5))
plt.plot(vMean, color='blue', label='Promedio (Convergencia)')
plt.axhline(vMean[-1], color='red', alpha=0.5, label=f'Promedio {vMean[-1]:,.0f}')
plt.axhline(ts, color='yellow', alpha=0.5, label=f'Tolerancia Superior {ts:,.0f}')
plt.axhline(ti, color='yellow', alpha=0.5, label=f'Tolerancia Inferior {ti:,.0f}')
plt.axvline(convergencia, color='peru', alpha=0.5,  linewidth=3 ,label=f'Convegencia despues {convergencia} replics')
plt.grid('on')
plt.title(f'Convergencia del promedio\nEl modelo converge a: {vMean[-1]:,.0f}, para {replics:,} replicas')
plt.legend()

plt.show()
