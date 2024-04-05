#!/usr/bin/env python3
"""
Script para verificar la instalación.

iousdgfkusdbngodfnbhgidfg
test 4
"""


def main():
    # Insertar acá su nombre completo
    STUDENT_NAME = "Nombre del Alumno"
    
    # Levantamos los datos del .csv
    dic = {}
    direc = r'test_data.csv'
    with open(direc,'rt') as archivo:       
        for i,linea in enumerate(archivo,1): 
            linea = linea.rstrip('\n')
            if i == 1:
                nombres_columnas = linea.split('\t')
                for nombres in nombres_columnas:
                    dic[nombres] = []
            else:
                datos_linea = linea.split('\t')
                for i,datos in enumerate(datos_linea):
                    if datos != '':
                        dic[nombres_columnas[i]].append(float(datos))
    # Calculamos el promedio de cada columna de interés
    prom_x = sum(dic['posx'])/len(dic['posx'])
    prom_y = sum(dic['posy'])/len(dic['posy'])
    prom_z = sum(dic['posz'])/len(dic['posz'])

    # Imprimimos los resultados
    print(f'¡Hola, {STUDENT_NAME}!')
    print(f'La posición promedio en x es {round(prom_x,2)}')
    print(f'La posición promedio en y es {round(prom_y,2)}')
    print(f'La posición promedio en z es {round(prom_z,2)}')

if __name__ == '__main__':
    # Ejecutamos el código 
    main()
