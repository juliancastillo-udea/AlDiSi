# main.py
import turnos

def iniciar_sistema():
    # Diccionarios vacíos al iniciar el programa
    llegadas = {}
    atenciones = {}
    
    # Contadores para saber qué número asignar y a quién llamar
    turno_para_asignar = 1
    turno_para_atender = 1
    
    opcion = "0"
    
    # Ciclo principal del menú
    while opcion != "4":
        print("\n" + "="*30)
        print("   SISTEMA DE TURNOS BÁSICO")
        print("="*30)
        print("1. Registrar nueva llegada")
        print("2. Atender al siguiente turno")
        print("3. Ver estado de los turnos")
        print("4. Salir del programa")
        
        opcion = input("\nElige una opción (1-4): ")
        
        if opcion == "1":
            nombre_persona = input("Ingresa el nombre de la persona: ")
            # Llamamos a la función y le pasamos los datos
            turnos.registrar_llegada(llegadas, turno_para_asignar, nombre_persona)
            # Aumentamos el contador para la próxima persona
            turno_para_asignar = turno_para_asignar + 1
            
        elif opcion == "2":
            # Llamamos a la función y guardamos su resultado (True o False)
            se_pudo_atender = turnos.atender_siguiente(llegadas, atenciones, turno_para_atender)
            # Solo si se atendió a alguien, avanzamos el contador de atención
            if se_pudo_atender == True:
                turno_para_atender = turno_para_atender + 1
                
        elif opcion == "3":
            turnos.mostrar_estado(llegadas, atenciones)
            
        elif opcion == "4":
            print("Saliendo del sistema de turnos. ¡Hasta luego!")
            
        else:
            print("❌ Opción no válida. Por favor, intenta de nuevo.")

# Ejecutamos nuestra función principal para arrancar el programa
iniciar_sistema()