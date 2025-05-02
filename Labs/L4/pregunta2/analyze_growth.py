# Laboratorio 4. Pregunta 2
# Natalia Escudero 20223377

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
    archivo_csv = sys.argv[1]
    with open(archivo_csv, "r") as archivo:
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
    
        # 2024-01,16194.47,2024-02,9943.27 deberia verse asi

    #despues de haber separado por meses
    stats = []
    for idx in range(datos_anuales[idx]):
        stat = getStats(datos_anuales[idx])
        stats.append(stat)
    
    with open("growth_stats.csv", "w") as archivo:
        archivo.write(filas)
    print(f"Escrito growth_stats.csv con {len(filas)} filas.")

    