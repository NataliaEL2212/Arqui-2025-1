import time
from multiprocessing import Pool

def power_chunk(args):
    n, chunk_size = args
    partial_result = 1
    for _ in range(chunk_size):
        partial_result *= n
    return partial_result

def main():
    n = 100_000
    num_processes = 4
    chunk_size = n // num_processes

    args = [(n, chunk_size) for _ in range(num_processes)]

    start = time.time()
    with Pool(processes=num_processes) as pool:
        results = pool.map(power_chunk, args)

    total_power = 1
    for r in results:
        total_power *= r

    end = time.time()
    print(f"Multiprocessing pool power calculation took {end - start:.2f} seconds")

if __name__ == "__main__":
    main()
