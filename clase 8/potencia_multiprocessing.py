import time
from multiprocessing import Pool

def power_chunk(args):
    n, chunk_size = args
    partial_result = 1
    # Cada proceso calcula n elevado a chunk_size (una parte de la potencia)
    for _ in range(chunk_size):
        partial_result *= n
    return partial_result

def main():
    n = 100_000
    num_processes = 4            # Número de procesos para paralelizar
    chunk_size = n // num_processes  # División equitativa del trabajo

    # Creamos lista de argumentos para cada proceso
    args = [(n, chunk_size) for _ in range(num_processes)]

    start = time.time()          # Inicio
    with Pool(processes=num_processes) as pool:
        # Ejecutamos power_chunk en paralelo con los argumentos preparados
        results = pool.map(power_chunk, args)

    # Combinamos resultados parciales multiplicándolos para obtener n^n total
    total_power = 1
    for r in results:
        total_power *= r

    end = time.time()            # Fin
    print(f"Multiprocessing pool power calculation took {end - start:.2f} seconds")

if __name__ == "__main__":
    main()

