import time

def cuenta():
    print("Uno")
    time.sleep(1) #time.sleep permite suspender la ejecución de un programa durante el tiempo en ()
    print("Dos")

def main():
    for _ in range(3):
        cuenta()

if __name__ == '__main__':
    inicio = time.perf_counter()
    main()
    fin = time.perf_counter()

    t_ejecucion = fin - inicio

    print(f"Timepo total de ejecución: {t_ejecucion:.6f} segundos")

    '''
    Uno
    Dos
    Uno
    Dos
    Uno
    Dos
    Timepo total de ejecución: 3.001354 segundos
    ''' #observamos que cuentan los tiempos de delay