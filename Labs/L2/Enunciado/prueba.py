import random
import os
import csv
import time

inicio = time.perf_counter()

# Nombre del archivo
archivo = "listanombres.txt"
archivo_csv = "nombres_repetidos.csv"

# Verificar si el archivo de nombres existe
if not os.path.exists(archivo):
    print("Archivo listanombres.txt no encontrado")
else:
    # Leer el archivo y almacenar los nombres en una lista
    with open(archivo, "r", encoding="utf-8") as f:
        nombres = f.read().splitlines()

    # Seleccionar un nombre al azar
    nombre_seleccionado = random.choice(nombres)
    print("Nombre seleccionado:", nombre_seleccionado)

    # Crear el archivo CSV si no existe
    if not os.path.exists(archivo_csv):
        with open(archivo_csv, "w", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["Nombres", "Repetición"])

    # Leer el archivo CSV y actualizar datos 
    filas = []
    nombre_encontrado = False
    with open(archivo_csv, "r", encoding="utf-8") as f:
        
        reader = csv.reader(f) #guardar contenido del csv en el iterador reader
        
        filas = list(reader)

        for i in range(1, len(filas)):
            if filas[i][0] == nombre_seleccionado:
                filas[i][1] = str(int(filas[i][1]) + 1)
                nombre_encontrado = True
                break
    
    # Si el nombre no estaba en el archivo, agregarlo
    if not nombre_encontrado:
        filas.append([nombre_seleccionado, "1"])

    # Escribir los datos actualizados en el CSV
    with open(archivo_csv, "w", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows(filas) 

    print("Se ha actualizado el archivo", archivo_csv)

fin = time.perf_counter()
duracion = fin - inicio
print("duracion:", duracion)
