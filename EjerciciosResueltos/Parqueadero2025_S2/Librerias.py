# Librerias ======================================================
import random as rnd
from datetime import date, datetime, timedelta
from pytz import timezone
import math as mt
import statistics as st
import os
# Librerias ======================================================

# Funciones ======================================================
def CalcularDeltaTiempo(inicio, fin):
    """
    Calcula la diferencia en horas entre dos objetos datetime y retorna el techo del número.
    Se recomienda el uso de datetime.now()

    Args:
        inicio (datetime): El objeto datetime de inicio.
        fin (datetime): El objeto datetime de fin.

    Returns:
        int: La diferencia en horas, redondeada hacia arriba.
    """
    diferencia = fin - inicio
    horas_totales = diferencia.total_seconds() / 3600
    return mt.ceil(horas_totales)

def ImprimirMenu():
    """
    Imprime el menú del programa

    Args:
        None.

    Returns:
        None
    """
    logo = """
                                 _______
                                /|_||_\\`.__
                                (   _    _ _|
                                =`-(_)--(_)-'
    """
    lineas = []
    lineas.append(logo)
    lineas.append('Bienvenido al Parqueadero "Insertar Nombre Del Parqueadero"')
    lineas.append('\t1. Registrar Usuario')
    lineas.append('\t2. Ingresar Vehiculo')
    lineas.append('\t3. Retirar Vehiculo')
    lineas.append('\t4. Salir')
    for linea in lineas:
        print(linea.center(80))
    return None

def ValidarOpcion(opcion:str) -> int:
    """
    Valida si la opción ingresada es una de las opciones permitidas y retorna su valor numérico.

    La función verifica si la opción es una de las permitidas ('1' a '5'). Si la opción es válida, retorna su valor entero.
    En caso contrario, retorna 0. También retorna 0 si la opción incluye '0' o si su longitud es diferente de 1.

    Args:
        opcion (str): La opción ingresada por el usuario, que deberá ser un número entre '1' y '5' como cadena.

    Returns:
        int: El valor entero de la opción si es válida; 0 en caso contrario.
    """
    opcion = str(opcion)
    opciones = ['1','2','3','4']
    if len(opcion) != 1:
        return 0
    else:
        if '0' in opcion:
            return 0
        elif len(opcion)==1:
            if opcion in opciones:
                return int(opcion)
            else:
                return 0
        else:
            return 0

def ValidarNombre(nombre:str):
    """
    Valida si el nombre ingresado es válido.

    Un nombre válido debe tener más de dos caracteres y contener únicamente letras. Si el nombre no cumple
    con estos criterios, se agrega un mensaje de error a la lista proporcionada y se retorna False.

    Args:
        nombre (str): El nombre a validar.

    Returns:
        bool: True si el nombre es válido, False en caso contrario.
    """
    nombre = str(nombre)
    if len(nombre) > 2:
        if nombre.isalpha():
            return True
        else:
            return False
    else:
        return False

def ValidarApellido(apellido: str) -> bool:
    """
    Valida si el apellido ingresado es válido.

    Un apellido válido debe tener más de dos caracteres y contener únicamente letras. Si el apellido no cumple
    con estos requisitos, se agrega un mensaje de error a la lista proporcionada y se retorna False.

    Args:
        apellido (str): El apellido a validar.

    Returns:
        bool: True si el apellido es válido, False en caso contrario.
    """
    apellido = str(apellido)
    if len(apellido) > 2:
        if apellido.isalpha():
            return True
        else:
            return False
    else:
        return False

def ValidarDocumento(documento:str):
    """
    Valida si el documento ingresado es válido.

    Un documento válido debe tener más de tres caracteres y contener únicamente dígitos. Si el documento no cumple
    con estos criterios, se agrega un mensaje de error a la lista proporcionada y se retorna False.

    Args:
        documento (str): El documento a validar.

    Returns:
        bool: True si el documento es válido, False en caso contrario.
    """
    documento = str(documento)
    if len(documento) > 3:
        if documento.isnumeric():
            return True
        else:
            return False
    else:
        return False

def ValidarPlaca(placa:str):
    """
    Valida si la placa ingresada es válida según el formato esperado.

    Una placa válida debe tener exactamente 6 caracteres, donde los primeros tres deben ser letras y los últimos tres dígitos.
    Si la placa no cumple con estos requisitos, se agrega un mensaje de error a la lista proporcionada y se retorna False.

    Args:
        placa (str): La placa de vehículo a validar.

    Returns:
        bool: True si la placa es válida, False en caso contrario.
    """
    placa = str(placa)
    if len(placa) == 6:
        letras = placa[:3]
        numeros = placa[3:]
        if letras.isalpha():
            if numeros.isnumeric():
                #Placa esta ok
                return True
            else:
                return False
        else:
            return False
    else:
        return False

def CalculoPago(horas:float):
    """
    Calcula el costo total del parqueadero basándose en las horas de uso.

    Args:
        horas (float): Número de horas que el vehículo permaneció en el parqueadero.

    Returns:
        float: El costo total a pagar por el servicio de parqueadero.
    """
    total = horas * 7500
    return total

def ImprimirFactura(nombre:str, apellido:str, documento:str, placa:str, valortotal:float,  horas, ancho=80):
    """
    Imprime una factura detallada del servicio de parqueadero.

    Args:
        nombre (str): Nombre del cliente.
        apellido (str): Apellido del cliente.
        documento (str): Número de documento del cliente.
        placa (str): Placa del vehículo.
        valortotal (float): Valor total a pagar por el servicio.
        horas (float): Número de horas que el vehículo permaneció en el parqueadero.
        ancho (int, optional): Ancho de la factura para formatear la salida. Por defecto es 80.

    Returns:
        None: La función imprime la factura directamente en la consola.
    """
    bogota_timezone = timezone('America/Bogota')
    linea = '-'*ancho
    overline = '¯'*(ancho)
    print(linea)
    saludo = 'Bienvenidos'
    print(saludo.center(80))
    parqueadero = 'Parqueadero Insertar Nombre del Parqueadero'
    print(parqueadero.center(80))
    nit = '123.666.000-9'
    print(nit.center(80))
    fecha = datetime.now(bogota_timezone)
    fecha_formateada = fecha.strftime("%Y-%m-%d")
    print(fecha_formateada.center(80))
    print(linea)
    print(overline)
    print(fecha_formateada.center(80))
    print(f'Usuario: {nombre} {apellido} -Documento {documento} | Placa: {placa}'.center(80))
    print(linea)
    print(overline)
    print('Placa'.center(20), 'Horas'.center(30), 'Valor a Pagar'.rjust(29), sep='')
    print(linea)
    print(overline)
    print(placa.center(20), f'Horas:{horas}'.center(30), f'$ {valortotal:,.0f}'.rjust(29), sep='')
    print(linea)
    print(overline)
    print('Gracias por Preferirnos'.center(80))
    print('Vuelva Pronto'.center(80))
    print('Desarrollado por Castillo-Enterprises 🏯'.center(80))
    print(linea)
    return None

def CrearArchivo(nombre='Parqueadero.csv'):
    """
    Crea un archivo CSV para el registro del parqueadero y escribe la fila de encabezados.
    https://en.wikipedia.org/wiki/UTF-8
    UTF-8 is a character encoding standard used for electronic communication.
    Defined by the Unicode Standard, the name is derived from Unicode Transformation Format – 8-bit.
    As of July 2025, almost every webpage is transmitted as UTF-8.
    UTF-8 supports all 1,112,064 valid Unicode code points using a variable-width encoding of one to four one-byte (8-bit) code units.
    ♥️♥️ https://www.youtube.com/watch?v=MijmeoH9LT4 ♥️♥️ Tom Scott, Muy calidoso, pero mucho
    Args:
        nombre (str): Nombre del archivo CSV a crear.

    Returns:
        None: No retorna ningún valor.
    """
    with open(nombre, 'w', encoding='utf-8') as f:
        f.write('Nombre,Apellido,Documento,Placa,TiempoIngreso,TiempoSalida,ValorPagado\n')
    return None

def GuardarRegistro(archivo, nombre, apellido, documento, placa, ingreso, salida, valor_pagado):
    """
    Guarda un registro de parqueo en un archivo CSV existente.

    Args:
        archivo (str): Ruta o nombre del archivo CSV donde se almacenará el registro.
        nombre (str): Nombre del usuario.
        apellido (str): Apellido del usuario.
        documento (str): Documento de identificación del usuario.
        placa (str): Placa del vehículo.
        ingreso (str): Fecha y hora de ingreso del vehículo al parqueadero.
        salida (str): Fecha y hora de salida del vehículo del parqueadero.
        valor_pagado (float): Valor total pagado por el tiempo de parqueo.

    Returns:
        None: No retorna ningún valor.
    """
    with open(archivo, 'a', encoding='utf-8') as f:
        f.write(f'"{nombre}","{apellido}","{documento}","{placa}","{ingreso}","{salida}",{valor_pagado}\n')
    return None

# Funciones ======================================================