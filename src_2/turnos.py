# turnos.py

def registrar_llegada(diccionario_llegadas, numero_turno, nombre):
    # Guardamos en el diccionario el número de turno como clave y el nombre como valor
    diccionario_llegadas[numero_turno] = nombre
    print("--------------------------------------------------")
    print(f"✅ Se registró a {nombre} con el turno número {numero_turno}")
    print("--------------------------------------------------")

def atender_siguiente(diccionario_llegadas, diccionario_atenciones, turno_actual):
    # Verificamos si el turno que queremos atender realmente existe en las llegadas
    if turno_actual in diccionario_llegadas:
        # Obtenemos el nombre de la persona
        nombre = diccionario_llegadas[turno_actual]
        
        # Lo agregamos al diccionario de atenciones
        diccionario_atenciones[turno_actual] = nombre
        
        # Lo eliminamos de llegadas para que ya no esté en espera
        del diccionario_llegadas[turno_actual]
        
        print("--------------------------------------------------")
        print(f"📢 Llamando para atención a: {nombre} (Turno {turno_actual})")
        print("--------------------------------------------------")
        return True # Retornamos True para saber que la atención fue exitosa
    else:
        print("--------------------------------------------------")
        print("⚠️ No hay nadie esperando con ese turno o no han llegado más personas.")
        print("--------------------------------------------------")
        return False # Retornamos False porque no se pudo atender a nadie

def mostrar_estado(diccionario_llegadas, diccionario_atenciones):
    print("\n=== PERSONAS ESPERANDO ===")
    if len(diccionario_llegadas) == 0:
        print("No hay nadie en fila.")
    else:
        for turno in diccionario_llegadas:
            print(f"Turno {turno}: {diccionario_llegadas[turno]}")
            
    print("\n=== PERSONAS YA ATENDIDAS ===")
    if len(diccionario_atenciones) == 0:
        print("Aún no se ha atendido a nadie.")
    else:
        for turno in diccionario_atenciones:
            print(f"Turno {turno}: {diccionario_atenciones[turno]}")