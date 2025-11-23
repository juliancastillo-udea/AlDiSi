# Librerias ======================================================
import random as rnd
from datetime import date, datetime, timedelta
from pytz import timezone
import math as mt
import statistics as st
import os
import Librerias as lib
# Librerias ======================================================
# --------------Almacenamiento de datos---------------------
dicUsuarios = {
    'Nombre': [],
    'Apellido': [],
    'Documento': [],
    'Placa': []
}

dicRegistro = {}

dicHistorico = {
    'Placa':[],
    'Documento':[],
    'FechaRegistro':[],
    'TiempoEnParqueadero':[]
}
# /--------------Almacenamiento de datos--------------------

# --------------Almacenamiento persistente------------------
lib.CrearArchivo()
# /--------------Almacenamiento persistente------------------

# --------------Menu principal------------------
# Script Principal ===============================================
while True:
"""
  █████████
 ███░░░░░███
░███    ░░░
░░█████████
 ░░░░░░░░███
 ███    ░███
░░█████████
 ░░░░░░░░░

  ██████
 ███░░███
░███ ░███
░███ ░███
░░██████
 ░░░░░░

 ████
░░███
 ░███
 ░███
 ░███
 ░███
 █████
░░░░░

 █████ ████
░░███ ░███
 ░███ ░███
 ░███ ░███
 ░░████████
  ░░░░░░░░

  ██████
 ███░░███
░███ ░░░
░███  ███
░░██████
 ░░░░░░

  ███
 ░░░
 ████
░░███
 ░███
 ░███
 █████
░░░░░

  ██████
 ███░░███
░███ ░███
░███ ░███
░░██████
 ░░░░░░

 ████████
░░███░░███
 ░███ ░███
 ░███ ░███
 ████ █████
░░░░ ░░░░░

  ██████
 ░░░░░███
  ███████
 ███░░███
░░████████
 ░░░░░░░░

 ████████
░░███░░███
 ░███ ░░░
 ░███
 █████
░░░░░

"""
    break
# /--------------Menu principal------------------
