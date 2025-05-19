import numpy as np
import time

def mult_vector(row, vector):
    total = 0
    for i in range(len(row)):
        total += row[i] * vector[i]
    return total

def main():
    size = 5000
    np.random.seed(0)
    matrix = np.random.randint(0, 100, (size, size))
    vector = np.random.randint(0, 100, size)

    results = []
    start = time.time()
    for row in matrix:
        results.append(mult_vector(row, vector))
    end = time.time()
    print(f"Synchronous matrix-vector multiplication took {end - start:.2f} seconds")

if __name__ == "__main__":
    main()
