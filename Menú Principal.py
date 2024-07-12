import funciones as fn
trabajadores = [
    "Juan Pérez", "María García", "Carlos López", "Ana Martínez", "Pedro Rodríguez", 
    "Laura Hernández", "Miguel Sánchez", "Isabel Gómez", "Francisco Díaz", "Elena Fernández"
    ]

sueldo_trabajadores = {} # diccionario de sueldo 


while True:
    print("------MENU-----")
    print("0. Inicializar sueldos")
    print("1. Asignar sueldos aleatorios")
    print("2. Ver estadísticas")
    print("3. Calcular Estadísticas")
    print("4. Generar Reporte en csv")
    print("5. Salir")

    opcion = int(input("Ingrese su opción: "))
    if opcion == 0:
        sueldo_trabajadores = {trabajador : 0 for trabajador in trabajadores} # inicializamos el diccionario en 0
        print("Sueldos inicializados correctamente")
    elif opcion == 1:
        if not sueldo_trabajadores:
            print("Primero debe inicializar los sueldos")
        else:
            sueldo_trabajadores = fn.asignar_Sueldo_aleatorios(trabajadores)
    elif opcion == 2:
        if sueldo_trabajadores :
            fn.clasificar_sueldos(sueldo_trabajadores)
        else:
            print("Por favor asignar sueldos")
    elif opcion == 3:
        if sueldo_trabajadores:
            max_sueldo,min_sueldo,promedio_sueldo = fn.calculo_estadistico(sueldo_trabajadores)
            if max_sueldo is not None:
                print("Sueldo Máximo: $",max_sueldo)
                print("Sueldo Mínimo: $",min_sueldo)
                print("Sueldo Promedio: $",promedio_sueldo)
            else:
                print("Por favor asignar sueldos")

    elif opcion == 4:
        if sueldo_trabajadores:
            fn.generar_reporte(sueldo_trabajadores)
        else:
            print("Por favor asignar sueldos")

    elif opcion == 5:
        print("Finalizando programa…")
        print("Desarrollado por Eric Rubilar")
        print("RUT 20.185.087-8")
        break
    else:
        print("Eliga una opción entre 0 y 5")