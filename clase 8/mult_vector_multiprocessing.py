import numpy as np
import time
from multiprocessing import Pool, cpu_count
from itertools import repeat

def mult_vector(row, vector):
    # Producto punto fila por vector
    total = 0
    for i in range(len(row)):
        total += row[i] * vector[i]
    return total

def main():
    size = 5000
    np.random.seed(0)
    matrix = np.random.randint(0, 100, (size, size))
    vector = np.random.randint(0, 100, size)

    num_processes = cpu_count()   # Detecta núcleos de CPU disponibles

    start = time.time()
    with Pool(processes=num_processes) as pool:
        # Preparamos argumentos: para cada fila del matrix se pasa la misma vector
        args = zip(matrix, repeat(vector))
        # Ejecutamos mult_vector en paralelo con argumentos desempaquetados
        results = pool.starmap(mult_vector, args)
    end = time.time()

    print(f"Multiprocessing matrix-vector multiplication took {end - start:.2f} seconds")

if __name__ == "__main__":
    main()
