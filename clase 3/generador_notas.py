    #Ahora se modificará el programa de calc_notas_manual.py para adaptarlo a un programa CSV

'''
import time
from random import randint

if __name__ == "__main__":
    inicio = time.perf_counter()
    
    contenido = ""

    encabezado = f"codigo, {','.join([f"lab_{idx+1}" for idx in range (12)])}, examen1, examen2\n"
    contenido += encabezado

    
    #Generaremos las notas a partir de valores aleatorios
    codigo_inicial = 20250001
    for i in range(200):
        linea = f"{codigo_inicial + i},{','.join([str(randint(0,20)) for _ in range(14)])}\n" #son 14 notas en total
        contenido += linea

    inicio_archivo = time.perf_counter()

    #Ahora la parte CSV
    with open("notas.csv", "w+") as f:
        f.write(contenido)

    fin = time.perf_counter()

    t_ejecucion = fin - inicio
    t_archivo = fin - inicio_archivo

    print(f"Tiempo de escritura del archivo: {t_archivo} segundos y de la ejecucion: {t_ejecucion}")
'''

    #NOTA: NO OLVIDAR DEL \n O SE PONDRA TODO EN UNA LINEA
    #El siguiente ejemplo sera sobre calcular las notas finales en base a lo escrito en el csv

import time
from random import randint

if __name__ == "__main__":
    inicio = time.perf_counter()

    with open("notas.csv", "r") as archivo:
        contenido = archivo.read()
    
    datos = contenido.split("\n")[1:] #dividimos el contenido en líneas desde la segunda linea, lista de strings

    codigo_inicial = 20250001

    for dato in datos:
        valores = [int(val) for val in dato.split(",")] #dividimos las lineas, se separa cada elemento individual separado por una coma, nos aseguramos que se convierta a un numero entero
        notas_labs = valores[1:13] #todas las notas de laboratorio, a partir del segundo, se ignora el primero porque es el codigo del alumno
        e1 = valores[13]
        e2 = valores[14]

        lab = sum(notas_labs) / len(notas_labs)
        nota_final = (5 * lab + 2 * e1 + 2 * e2) / 10
        print(f"Nota final: {nota_final}")

    inicio_archivo = time.perf_counter()

    fin = time.perf_counter()

    t_ejecucion = fin - inicio
    t_archivo = fin - inicio_archivo

    print(f"Tiempo de escritura del archivo: {t_archivo} segundos y de la ejecucion: {t_ejecucion}")

    #Notar que saldrá error si la última linea del archivo cvs esta vacia 
    #A diferencia de C, en Python un for asume un valor como iterador, mientras que en C va sumando y recorriendo la variable hasta su limite (0,1,2,3,...)