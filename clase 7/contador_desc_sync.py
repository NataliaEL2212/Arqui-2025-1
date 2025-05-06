#programa contador descendente sincrono

import time

N = 100_000_000

def cuenta(n: int) -> None:
    while n > 0:
        n-=1

if __name__ == '__main__':
    inicio = time.perf_counter()
    cuenta(N)
    fin = time.perf_counter()

    print(f"Tiempo total de ejecucion: {(fin - inicio):.6f} segundos")

    '''
    Tiempo total de ejecucion: 1.064594 segundos
    '''