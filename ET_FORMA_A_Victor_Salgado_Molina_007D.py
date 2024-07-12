import random
import csv

trabajadores=["Juan Pérez”,”María García”,”Carlos López”,”Ana Martínez”,”Pedro Rodríguez”,”Laura Hernández”,”Miguel Sánchez”,”Isabel Gómez”,”Francisco Díaz”,”Elena Fernández"]
 
datos_guardados=[]


        
def asignar_sueldo():
    for trabajador in trabajadores:
        sueldo=random.randint(300000, 2500000)
        cantidad=random.randint(1, 10)
        datos_guardados.append({'nombre': trabajador, 'sueldo': sueldo, 'cantidad': cantidad})
        
def sueldos():
    sueldo_bajo=[]
    sueldo_minimo=[]
    sueldo_mayor=[]

    for sueldo in datos_guardados:
        sueldo = trabajadores['sueldo']
        if sueldo > 460000:
            sueldo_bajo.append(sueldo['nombre'])
        elif sueldo > 460000 < 900000:
            sueldo_minimo.append(sueldo['nombre'])
        elif sueldo == 2500000:
            sueldo_mayor.append(sueldo['nombre'])
    
    print("sueldos asignados")
    print(f"bajo (< $460,000 CLP):{sueldo_bajo}")
    print(f"minimo ($460,000 - $900,000 CLP):{sueldo_minimo}")
    print(f"mayor ($1,000,000 - $2,500,000 CLP):{sueldo_mayor}")

def estadisticas():
    sueldos=[]
    cantidad=[]
    sueldo_mas_grande = datos_guardados[sueldos]
    sueldo_mas_bajo = datos_guardados[sueldos]

    for sueldo in datos_guardados:
        sueldos.append(sueldo['sueldo'])
        cantidad.append(cantidad_trabajadores['cantidad'])

        if sueldo['sueldo'] > sueldo_mas_grande['sueldo']:
            sueldo_mas_grande = sueldo

        if sueldo['sueldo'] < sueldo_mas_bajo['sueldo']:
            sueldo_mas_bajo = sueldo

    #calcular suma de los sueldos
    suma_sueldos = sum(sueldo)

    #calcular promedio de los sueldos
    cantidad_trabajadores = len(sueldo)
    promedio = suma_sueldos / cantidad_trabajadores if cantidad_trabajadores > 0 else 0

    sueldo_media_geom = 1
    for cantidad in cantidad_trabajadores:
        sueldo_media_geom *= cantidad


    #media geometrica de los sueldos
    media_geom_cantidades = (sueldo_media_geom) ** (1/len(cantidad_trabajadores)) if len(cantidad_trabajadores) > 0 else 0

    valor_total_sueldos= sum(sueldo['sueldo'] * trabajadores['cantidad'] for trabajadores in datos_guardados)

    #imprimir estadisticas
    print("estadisticas totales de los trabajadores: ")
    print(f"sueldo mas alto: {sueldo_mas_grande['nombre']} (${sueldo_mas_grande['sueldo']} CLP")
    print(f"sueldo mas bajo: {sueldo_mas_bajo['nombre']} (${sueldo_mas_bajo['sueldo']} CLP")
    print(f"promedio: ${promedio:.2f} CLP")
    print(f"media geometrica: {media_geom_cantidades:.2f}")
    print(f"valor total de los sueldos: ${valor_total_sueldos:.2f}CLP")


def reporte():
    with open ('reporte_sueldos.csv', 'w', newline='') as archivo:
        writer = csv.writer(archivo)
        writer.writerow(['Nombre', 'Sueldo', 'Descuento en Salud (7%)', 'Descuento AFP (12%)', 'sueldo final'])

        for sueldo in datos_guardados:
            sueldo = trabajadores['sueldo']
            cantidad = trabajadores['cantidad']
            descuento_salud = sueldo *0.07
            descuento_AFP = sueldo *0.12
            sueldo_final = sueldo - descuento_salud- descuento_AFP

            writer.writerow([trabajadores['nombre'], sueldo, cantidad, descuento_salud, descuento_AFP, sueldo_final])
            

def menu():
    while True:
        print('''
              1. Asignar sueldos aleatorios
              2. Clasificar Sueldos
              3. Ver Estadisticas
              4. Reporte de sueldos
              5. Salir
              ''')
        opc = input("Opcion: ")
        if opc.isnumeric():
            opc=int(opc)
            if opc == 1:
                asignar_sueldo()
                print("sueldos asignados")
            elif opc == 2:
                sueldos()
            elif opc== 3:
                estadisticas()
            elif opc == 4: 
                reporte()
                print("reporte generado correctamente en 'reporte_sueldos.csv'.")
            elif opc == 5:
                print('''
                      Finalizando Programa...
                      desarrollado por Victor Salgado
                      RUT 21.912.900-9
                      ''' )
                break
            else:
                print("Opcion invalida, porfavor ingrese un numero entre el 1 y el 5")
        else:
            print("ERROR, porfavor ingresar un numero del 1 al 5")

menu()
                














 






        


        
    
    