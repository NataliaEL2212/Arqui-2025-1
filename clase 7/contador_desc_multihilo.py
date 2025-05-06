import time

N = 100_000_000

def cuenta(n: int) -> None:
    while n > 0:
        n-=1

if __name__ == '__main__':
    inicio = time.perf_counter()
    t1 = Thread(target=cuenta, args = (N//2,)) #division entera
    t2 = Thread(target=cuenta, args = (N//2,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    fin = time.perf_counter()

    print(f"Tiempo total de ejecucion: {(fin - inicio):.6f} segundos")

    '''
    Tiempo total de ejecucion: 1.065520 segundos
    '''

    #Observamos que usar hilos tiene un comportamiento peor que uno secuencial, el tiempo de ejecución es mayor
    #Ambos hilos empiezan, e intentan acceder a la variable n al mismo tiempo. Están compitiendo entre ellos para ver quien accede a n antes (racing) y por ello n puede no tener el valor necesario al accederse. Este es un gran problema de vulnerabilidad.
    ##Esto se debe a que nuestra función cuenta() no tiene operaciones de I/O (entrada o salida), solo son comparaciones y una resta.
    #Usar time.sleep() como en el ejemplo contador_simple_multihilo.py evita que ocurra "Race Condition", porque lo ralentiza manualmente.
    #Race Condition es un evento en el cual se mitigan la cantidad y uso de hilos. Como comparten la misma memoria, se busca evitar que el valor de n sea modificado varias veces. En este particular ejercicio cada hilo tiene un n independiente por lo cual no existe ese riesgo,
    #pero Python no tiene forma de determinarlo, por lo que igual aplica la restricción. Es decir, ejecuta un hilo y luego ejecuta el siguiente, no permite ejecutarlos al mismo tiempo para evitar la falta de memoria.
    #En este ejemplo seria mejor usar asyncio, pero requiere operaciones de I/O entonces no será posible. Asyncio permite utilizar la concurrencia sin crear múltiples hilos.