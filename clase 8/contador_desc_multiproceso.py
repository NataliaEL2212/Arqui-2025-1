import time
from multiprocessing import Process

def countdown(n):
    # Función que decrementa n hasta 0
    while n > 0:
        n -= 1

def main():
    n = 100_000_000
    start = time.time()          # Marca inicio

    # Creamos dos procesos que ejecutan countdown con la mitad del trabajo cada uno
    p1 = Process(target=countdown, args=(n // 2,))
    p2 = Process(target=countdown, args=(n // 2,))

    # Iniciamos ambos procesos en paralelo
    p1.start()
    p2.start()

    # Esperamos a que ambos procesos terminen antes de continuar
    p1.join()
    p2.join()

    end = time.time()            # Marca fin
    print(f"Multiprocessing countdown took {end - start:.2f} seconds")  # Duración total

if __name__ == "__main__":
    main()

