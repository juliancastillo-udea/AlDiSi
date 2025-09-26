# -*- coding: utf-8 -*-
"""
Created on Fri Sep 26 07:52:55 2025

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

def raizderecha(var):
    if var >= 0:
        rd = mt.sqrt(var)
    else:
        rd = 0
    return rd

def raizizquierda(var):
    if var <= 0:
        ri = mt.sqrt((-1)*var)
    else:
        ri = 0
    return ri

def normalita(var, desviacion_normal = 1, media_normal = 0):
    incremento_escala = 2 / (1 / (desviacion_normal * np.sqrt(2 * np.pi))) 
    normal = incremento_escala * (1 / (desviacion_normal * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((var - media_normal) / desviacion_normal) ** 2)
    return normal

def polinomica(var):
    polinomica = (9/670)*((1/5)*var**5 - (20/3)*var**3 + 64*var) + 3/2
    return polinomica

replicas = 100 #tengo un nivel de escalamiento de 10 en x y 3 unidades en y
maximoy = 3
minimoy = 0
maximox = 5
minimox = -5

def Integral(replicas):
    hit = 0
    xhit, yhit = [], []
    xmiss, ymiss = [], []
    for i in range(replicas):
        _x = rnd.uniform(minimox, maximox)
        _y = rnd.uniform(minimoy, maximoy) #hola, este y se queda quietico y 
        #aplicamos las funciones a los valores de _x
        rd = raizderecha(_x)
        ri = raizizquierda(_x)
        n = normalita(_x)
        p = polinomica(_x)
        if (_y > rd) and (_y > ri) and (_y > n) and (_y > p):
            hit += 1
            xhit.append(_x)
            yhit.append(_y)
        else:
            xmiss.append(_x)
            ymiss.append(_y)
    #aca ya terminamos el ciclo, todos los valores de replicas fueron evaluados
    proporcion = hit / replicas
    return proporcion, xhit, yhit, xmiss, ymiss
#ya me sali de la funcion y vamos a llamarla

replicas = 10000
proporcion, xhit, yhit, xmiss, ymiss = Integral(replicas)

# Calcular Vectores --------------------------------------------------------------------------------------------------------------------------
x = np.linspace(-5, 5, replicas)  # Genera un arreglo de 10,000 puntos equiespaciados entre -5 y 5.
rade = np.sqrt(x)  # Calcula la raíz cuadrada de los valores positivos de x
raiz = np.sqrt((-1)*x)  # Calcula la raíz cuadrada de los valores negativos de x
desviacion_normal, media_normal = 1, 0  # Define la desviación estándar y la media de la distribución normal.
incremento_escala = 2 / (1 / (desviacion_normal * np.sqrt(2 * np.pi)))  # Factor de escala para ajustar la distribución.
normal = incremento_escala * (1 / (desviacion_normal * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - media_normal) / desviacion_normal) ** 2)
poli = (9/670)*((1/5)*x**5 - (20/3)*x**3 + 64*x) + 3/2  # Polinomio de grado 5 ajustado con un factor de escala.
unos = np.ones_like(x)  # Crea un arreglo de unos con el mismo tamaño que x.
yigualatres = unos * 3  # Línea horizontal en y = 3.
yigualacero = np.zeros_like(x)  # Línea horizontal en y = 0.
plt.rcParams.update({'font.size': 14})  # Ajusta el tamaño de fuente global para las gráficas.
# Pintar los datos ---------------------------------------------------------------------------------------------------------------------------
plt.figure(figsize=(10, 10))  # Crea una figura de 10x10 pulgadas.
# hit and miss
plt.scatter(xhit,yhit, marker="*", color="cyan", label='Hit')
plt.scatter(xmiss,ymiss, marker="o", color="pink", label='Miss')
# Lineas
plt.plot(x, rade, color='blue', linewidth=3, label='Raiz Positiva')  # Gráfica de la raíz positiva.
plt.plot(x, raiz, color='red', linewidth=3, label='Raiz Negativa')  # Gráfica de la raíz negativa.
plt.plot(x, normal, color='green', linewidth=3, label='Normal')  # Gráfica de la distribución normal.
plt.plot(x, poli, color='orange', linewidth=3, label='Polinomica')  # Gráfica de la función polinómica.
plt.plot(x, yigualatres, color='purple', linewidth=3, label='Limite Superior')  # Línea horizontal en y = 3.
plt.plot(x, yigualacero, color='purple', linewidth=3, label='Limite Inferior')  # Línea horizontal en y = 0.
plt.plot([-5, -5], [0, 3], color='purple', linewidth=3, label='Limite Izquierdo')  # Línea vertical en x = -5.
plt.plot([5, 5], [0, 3], color='purple', linewidth=3, label='Limite Derecho')  # Línea vertical en x = 5.
plt.xlabel('x', fontsize=16)  # Etiqueta del eje x con tamaño de fuente 16.
plt.ylabel('f(x)', fontsize=16)  # Etiqueta del eje y con tamaño de fuente 16.
plt.title(r'☢️☢️☢️   Montecarlo Integrales Viernes 11 de Abril   ☢️☢️☢️', fontsize=18)  # Título del gráfico con emojis y tamaño de fuente 18.
plt.xlim(-5, 5)  # Limita el eje x entre -5 y 5.
plt.xticks(np.linspace(-5, 5, 11))  # Define los ticks del eje x en intervalos de 1.
plt.legend(fontsize=14, loc='center left', bbox_to_anchor=(1, 0.5))  # Coloca la leyenda fuera del gráfico, a la izquierda.
plt.grid('on')  # Activa la cuadrícula.
plt.axis('scaled')  # Escala los ejes para que las proporciones sean iguales.
plt.show()  # Muestra el gráfico.


vEstimation = []
vMean = []
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
plt.axhline(promedio*1.01, color='yellow', alpha=0.5, label=f'Tolerancia Superior {promedio*1.01:,.0f}')
plt.axhline(promedio*0.99, color='yellow', alpha=0.5, label=f'Tolerancia Inferior {promedio*0.99:,.0f}')
plt.axvline(convergencia, color='orange', alpha=0.5,  linewidth=3 ,label=f'Convegencia despues {convergencia} replics')
plt.grid('on')
plt.title(f'El Area Converge a: {promedio:,.2f}, para {replicas:,} replicas')
plt.legend()
plt.show()











