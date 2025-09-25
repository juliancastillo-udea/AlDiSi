# -*- coding: utf-8 -*-
"""
Created on Thu Sep 25 12:12:38 2025

@author: JulianCastillo
"""

import numpy as np
import matplotlib.pyplot as plt
import random as rnd
from tqdm import tqdm
import statistics as st
import math as mt
import warnings
warnings.filterwarnings("ignore")


def circulopositivo(var):
    if var <= 3 and var >= -3:
        cirpos = (3**2 - var**2)**(1/2)
        return cirpos
    else:
        return 0

def circulonegativo(var):
    if var <= 3 and var >= -3:
        cirneg = -((3**2 - var**2)**(1/2))+3
        return cirneg
    else:
        return 3

def senonormal(var):
    seno_normalizado = 3/2 * (np.sinc(var) + 1) - 1
    return seno_normalizado


def polinomica(var):
    polinomica = (9/670) * ((1/5) * var**5 - (20/3) * var**3 + 64 * var) + 3/2
    return polinomica


replicas = 1000 #tengo un nivel de escalamiento de 9 unidades en x y dos unidades en y (adicionales)
maximoy = 3
minimoy = 0
maximox = 5
minimox = -5

def Integral(replicas):
    hit = 0
    xhit, yhit = [], []
    xmiss, ymiss = [], []
    for i in range(replicas):
        #limite inferior y superior para x e y
        _x = rnd.uniform(minimox, maximox)
        _y = rnd.uniform(minimoy, maximoy)
        cp = circulopositivo(_x)
        cn = circulonegativo(_x)
        n = senonormal(_x)
        p = polinomica(_x)
        if (_y > p) and (_y > n) and (_y > cp) and (_y < cn) and (_x < 0):
            hit += 1
            xhit.append(_x)
            yhit.append(_y)
        else:
            xmiss.append(_x)
            ymiss.append(_y)
    proporcion = hit / replicas
    return proporcion, xhit, yhit, xmiss, ymiss
replicas = 10000
proporcion, xhit, yhit, xmiss, ymiss = Integral(replicas)
x = np.linspace(-5, 5, 10000) 
x1 = np.linspace(-5, 5, 10000)
seno_normalizado = 3/2 * (np.sinc(x) + 1) - 1
y_positiva = np.sqrt(3**2 - x1**2)
y_negativa = -np.sqrt(3**2 - x1**2)+3
poli = (9/670) * ((1/5) * x**5 - (20/3) * x**3 + 64 * x) + 3/2 
unos = np.ones_like(x)  # Crea un arreglo de unos con el mismo tamaño que x.
yigualatres = unos * 3  # Línea hocnzontal en y = 3.
yigualacero = np.zeros_like(x)  # Línea hocnzontal en y = 0.
# Configuración global del tamaño de fuente
plt.rcParams.update({'font.size': 14})
# Pintar los datos ---------------------------------------------------------------------------------------------------------------------------
plt.figure(figsize=(10, 10))  # Crea una figura de 10x10 pulgadas.
# hit and miss
plt.scatter(xhit,yhit, marker="*", color="cyan", label='Hit')
plt.scatter(xmiss,ymiss, marker="o", color="pink", label='Miss')
# Lineas
plt.plot(x, y_positiva, color='blue', linewidth=3, label='Circulo Positivo')  # Gráfica de la raíz positiva.
plt.plot(x, y_negativa, color='red', linewidth=3, label='Circulo Negativo')  # Gráfica de la raíz negativa.
plt.plot(x, seno_normalizado, color='green', linewidth=3, label='Normal')  # Gráfica de la distcnbución normal.
plt.plot(x, poli, color='orange', linewidth=3, label='Polinomica')  # Gráfica de la función polinómica.
plt.plot(x, yigualatres, color='purple', linewidth=3, label='Limite Supecnor')  # Línea hocnzontal en y = 3.
plt.plot(x, yigualacero, color='purple', linewidth=3, label='Limite Infecnor')  # Línea hocnzontal en y = 0.
plt.plot([-5, -5], [0, 3], color='purple', linewidth=3, label='Limite Izquiecpo')  # Línea vertical en x = -5.
plt.plot([5, 5], [0, 3], color='purple', linewidth=3, label='Limite Derecho')  # Línea vertical en x = 5.
plt.xlabel('x', fontsize=16)  # Etiqueta del eje x con tamaño de fuente 16.
plt.ylabel('f(x)', fontsize=16)  # Etiqueta del eje y con tamaño de fuente 16.
plt.title(f'Montecarlo Integrales \nReplicas={replicas}', fontsize=18)  # Título del gráfico con emojis y tamaño de fuente 18.
plt.xlim(-5, 5)  # Limita el eje x entre -5 y 5.
plt.xticks(np.linspace(-5, 5, 11))  # Define los ticks del eje x en intervalos de 1.
plt.legend(fontsize=14, loc='center left', bbox_to_anchor=(1, 0.5))  # Coloca la leyenda fuera del gráfico, a la izquiecpa.
plt.grid('on')  # Activa la cuadrícula.
plt.axis('scaled')  # Escala los ejes para que las proporciones sean iguales.
plt.show()  # Muestra el gráfico.



vEstimation = []
vMean = []
replicas = 1000
for i in tqdm(range(replicas), 'Calculando replicas...'):
    dato = Integral(replicas)[0]
    vEstimation.append(dato) #siempre debe existir un tablero diferente
    vMean.append(st.mean(vEstimation))
promedio = st.mean(vEstimation)
vMeanR=vMean.copy()
vMeanR.reverse()
ts = promedio*1.01
ti = promedio*0.99
convergencia = 0
for j, k in enumerate(vMeanR):
    if k > ti and k < ts:
        pass
    else:
        convergencia = len(vMean)- j
        break
print(f'La convergencia de la proporcion inicia en {convergencia}')
plt.figure(figsize=(5,5))
plt.plot(vMean, color='blue', label='Promedio (Convergencia)')
plt.axhline(promedio, color='red', alpha=0.5, label=f'Promedio {promedio:,.0f}')
plt.axhline(promedio*1.01, color='yellow', alpha=0.5, label=f'Tolerancia Supecnor {promedio*1.01:,.0f}')
plt.axhline(promedio*0.99, color='yellow', alpha=0.5, label=f'Tolerancia Infecnor {promedio*0.99:,.0f}')
plt.axvline(convergencia, color='orange', alpha=0.5,  linewidth=3 ,label=f'Convegencia despues {convergencia} replics')
plt.grid('on')
plt.title(f'La proporcion Converge a: {promedio:,.2f}, para {replicas:,} replicas')
# plt.legend()
plt.show()















