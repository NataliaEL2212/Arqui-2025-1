import time

def power(n):
    result = 1
    # Multiplicamos n por sí mismo n veces, para calcular n^n
    for _ in range(n):
        result *= n
    return result

def main():
    n = 100_000
    start = time.time()          # Inicio
    power(n)                     # Cálculo sincrónico
    end = time.time()            # Fin
    print(f"Synchronous power calculation took {end - start:.2f} seconds")

if __name__ == "__main__":
    main()
