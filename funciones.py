import random
import csv
import statistics

def asignar_Sueldo_aleatorios(trabajadores):
 
    sueldo_trabajadores = {} # diccionario de sueldo 
    #Procedemos a iterar sobre cada trabajador en la lista de los trabajadores
    for trabajador in trabajadores:
        # se genera un sueldo aleatorio entre...
        sueldo = random.randint(300000,2500000)
        # asignamos el sueldo generado al trabajador que figura en el diccionario
        sueldo_trabajadores[trabajador] = sueldo
        
    print("Sueldos aleatorios asignados correctamente")
    print(sueldo_trabajadores)

    return sueldo_trabajadores

def clasificar_sueldos(sueldo_trabajadores):
    menor_800 = {}
    entre_800_2000 = {}
    mayor_2000 = {}
    for trabajador,sueldo in sueldo_trabajadores.items():
        if sueldo < 800000:
            menor_800[trabajador] = sueldo
        elif sueldo <= 2000000:
            entre_800_2000[trabajador] = sueldo
        else:
            mayor_2000[trabajador] = sueldo

    # Resultados
    print("Sueldos menores a $800.000 TOTAL:",len(menor_800))
    for trabajador,sueldo in menor_800.items():
        print(trabajador,": $",sueldo)

    print("Sueldos entre $800.000 y $2.000.000 TOTAL:",len(entre_800_2000))
    for trabajador,sueldo in entre_800_2000.items():
        print(trabajador,": $",sueldo)

    print("Sueldos superiores a $2.000.000 TOTAL:",len(mayor_2000))
    for trabajador,sueldo in mayor_2000.items():
        print(trabajador,": $",sueldo)
    
def calculo_estadistico(sueldo_trabajadores):
    '''
    maximo, minimo y promedio
    '''
    
    sueldos = list(sueldo_trabajadores.values()) #sueldos = [..........]

    if not sueldos:
        print("No hay sueldos asignados")
        return None,None,None
    
    max_sueldo = max(sueldos) # mayor a 2000
    min_sueldo = min(sueldos) # menor a 800
    promedio_sueldo = sum(sueldos) / len(sueldos)
    return max_sueldo,min_sueldo,promedio_sueldo


def generar_reporte(sueldo_trabajadores):
    '''
    reporte generado con csv sobre los sueldos de trabajadores y su clasificación
    '''
    with open('reportes_sueldos.csv','w',newline='') as archivo :
        escritor = csv.writer(archivo,delimiter=',')

        #escribir encabezados
        escritor.writerow(['Nombre trabajador','Sueldo Base','Descuento salud','Descuento AFP','Sueldo Liquido'])


        #escribir cada línea de datos
        for trabajador,sueldo in sueldo_trabajadores.items():
            descuento_salud = sueldo * 0.07
            descuento_Afp = sueldo * 0.12
            sueldo_liquido = sueldo - descuento_salud - descuento_Afp
            escritor.writerow([trabajador,sueldo,descuento_salud,descuento_Afp,sueldo_liquido])
    print("Reporte correctamente generado en reportes_sueldos.csv")
    