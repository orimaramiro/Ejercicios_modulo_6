# Archivos [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios con archivos

import csv


def ej3():
    print('Ejercicio de archivos CSV 1º')
    archivo = 'stock.csv'
    
    # Realice un programa que abra el archivo 'stock.csv'
    # en modo lectura y cuente el stock total de tornillos
    # a lo largo de todo el archivo, 
    # sumando el stock en cada fila del archivo

    # Para eso debe leer los datos del archivo
    # con "csv.DictReader", y luego recorrer los datos
    # dentro de un bucle y solo acceder a la columna "tornillos"
    # para cumplir con el enunciado del ejercicio

    # Comenzar aquí, recuerde el identado dentro de esta funcion
    csvfile = open(archivo, "r")
    data_tornillos = list(csv.DictReader(csvfile))
    cant_tornillos = 0
    for item in data_tornillos:
        cant_tornillos += int(item["tornillos"])

    print('Hay en stock', cant_tornillos, "Tornillos")
    csvfile.close()



    


def ej4():
    print('Ejercicios con archivos CSV 2º')
    archivo = 'propiedades.csv'

    # Realice un programa que abra el archivo CSV "propiedades.csv"
    # en modo lectura. Recorrar dicho archivo y contar
    # la cantidad de departamentos de 2 ambientes y la cantidad
    # de departamentos de 3 ambientes disponibles.
    # Al finalizar el proceso, imprima en pantalla los resultados.

    # Tener cuidado que hay departamentos que no tienen definidos
    # la cantidad de ambientes, verifique el texto no esté vacio
    # antes de convertirlo a entero con "int( .. )"
    # NOTA: Si desea investigar puede evitar que el programa explote
    # utilizando "try except", tema que se verá la clase que viene.

    # Comenzar aquí, recuerde el identado dentro de esta funcion
    csvfile = open(archivo, 'r')
    busca_deptos = list(csv.DictReader(csvfile))

    de2_ambientes = 0
    de3_ambientes = 0
    
    cant_deptos = len(busca_deptos)
    
    for deptos in range(cant_deptos):
        row = busca_deptos[deptos]
        try:
            cant_ambientes = int(row.get('ambientes'))
            
            if cant_ambientes == 2:
                de2_ambientes += 1
            elif cant_ambientes == 3:
                de3_ambientes += 1
        except:
            continue
            
    print('Sobre', cant_deptos,'propiedades:')
    print('Hay', de2_ambientes, 'departamentos de 2 ambientes.')
    print('Hay', de3_ambientes, 'departamentos de 3 ambientes.')
    csvfile.close()


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    ej3()
    ej4()
