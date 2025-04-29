import time
from threading import Thread

def cuenta():
    print("Uno")
    time.sleep(1)
    print("Dos")


def main():
    t1 = Thread(target=cuenta) #recibe el target. un thread o hilo 
    t2 = Thread(target=cuenta)
    t3 = Thread(target=cuenta)

    t1.start() #deben de ejecutarse
    t2.start()
    t3.start()


if __name__ == "__main__":
    inicio = time.perf_counter()
    main()
    fin = time.perf_counter()

    t_ejecucion = fin - inicio

    print(f"Tiempo total de ejecucion: {t_ejecucion:.6f} segundos")

    '''
    Uno
    Uno
    Uno
    Tiempo total de ejecucion: 0.001088 segundos
    Dos
    Dos
    Dos
    '''

    #Multihilos solo funciona de manera concurrente utilizando i/o
    #El salto entre hilos funciona de manera similar a la de las concurrencias. Esto significa que actualmente hay 4 hilos de ejecucion: el principal: t1, t2, y t3. Por lo que ejecuta t1 -> t2 -> t3 -> main -> t1 -> t2 -> t3
    #El codigo termina cuando todos los hilos terminan de ejecutarse. Cada hilo es autónomo uno del otro y del main. A diferencia de asyncio, el programa no termina hasta que se terminen las concurrencias y luego el resto del main principal. 
    #No son procesos totalmente separados porque ocupan el mismo espacio de memoria, pero desde el punto de vista de la ejecución, si lo son. Es como si fueran 4 programas ejecutándose al mismo tiempo.
    #En otros lenguajes de programación se permite utilizar paralelismo, es decir, poner los hilos en múltiples núcleos y que los threads operen como si fueran un asyncio. Esto disminuye la posibilidad de errores y flags. Para el Python actual aún no se puede.