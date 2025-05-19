import numpy as np
import time

def mult_vector(row, vector):
    # Multiplica un vector fila por un vector columna (producto punto)
    total = 0
    for i in range(len(row)):
        total += row[i] * vector[i]
    return total

def main():
    size = 5000                 # Dimensiones de la matriz cuadrada
    np.random.seed(0)           # Semilla para reproducibilidad
    matrix = np.random.randint(0, 100, (size, size))  # Matriz aleatoria 5000x5000
    vector = np.random.randint(0, 100, size)          # Vector aleatorio tamaño 5000

    results = []
    start = time.time()         # Inicio del proceso
    # Para cada fila de la matriz calculamos el producto punto con el vector
    for row in matrix:
        results.append(mult_vector(row, vector))
    end = time.time()           # Fin
    print(f"Synchronous matrix-vector multiplication took {end - start:.2f} seconds")

if __name__ == "__main__":
    main()
