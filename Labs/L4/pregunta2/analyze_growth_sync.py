# Laboratorio 4. Pregunta 2
# Natalia Escudero 20223377

import time
import sys

def getStats(datos_anuales: str) -> str: # 2024-01,16194.47,2024-02,9943.27...
    revenues = []

    for dato in datos:
        valores = [float(val) for val in dato.split(",")] #convertimos a float

    for i in range(len(datos_anuales)/2): #para solo tener los revs en la misma lista
        revenues.append(valores[i+1]) #vamos agregando los revenues
        
    crecimiento_porcentual_mensual = []
    for i in range(1:12):
        crecimiento_porcentual_mensual[i] = (rev[i] - rev[i-1]) / rev[i-1] * 100
    prom_crecimiento = statistics.mean(revenues)
    dev_crecimiento = statistics.pstdev(revenues)
    rev_ordenado = sorted(rev, reverse=True)
    primero = rev_ordenado[0]
    segundo = rev_ordenado[1]
    tercero = rev_ordenado[2]

    return f"{valores[0]},{crecimiento_porcentual_mensual[0]},{prom_crecimientoh},{dev_crecimiento,},{primero},{segundo},{tercero}"

if __name__ == '__main__':  
    archivos = []
    archivos[0] = sys.argv[1]
    archivos[1] = sys.argv[2]
    archivos[2] = sys.argv[3]

    lista = []

    inicio = time.perf_counter()
    for i in range(1:3):
        with open(archivos[i], "r") as archivo:
        contenido = archivo.read()
    
        filas = contenido.split("\n")[1:] #dividimos el contenido en líneas desde la segunda linea, lista de strings

        fila_inicial = [int(val) for val in datos[0].split("-")]
        año_inicial = fila_inicial[0] #el primer año visto en el archivo csv

        año = año_inicial
        cant_años = 0
        datos_anuales = []
        for i in range(len(datos)): #todas las filas
            if año in filas[i]: #revisamos que la linea sea del año evaluado
                datos_anuales[cant_años] = f"{datos_anuales[cant_años]},{filas[i]}" #unimos a la string
                i += 1 #pasamos a la siguiente fila
            else:
                año += 1 #pasamos al siguiente año
                cant_años += 1

        for idx in range(datos_anuales[idx]):
            stat = getStats(datos_anuales[idx])
            lista.append(stat)

    with open("growth_stats_sync.csv", "w") as archivo:
        archivo.write(lista)

    fin = time.perf_counter()
    duracion = fin - inicio
    print(f"Tiempo total (sincrono): {duracion} s")
    print(f"Escrito growth_stats_sync.csv con {len(filas)} filas.")
    
