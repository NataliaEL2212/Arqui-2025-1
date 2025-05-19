import time

def countdown(n):
    # Función que decrementa el valor n hasta 0
    while n > 0:
        n -= 1

def main():
    start = time.time()          # Marca inicio del conteo de tiempo
    countdown(100_000_000)       # Ejecuta la función síncrona
    end = time.time()            # Marca fin del conteo de tiempo
    print(f"Synchronous countdown took {end - start:.2f} seconds")  # Muestra duración

if __name__ == "__main__":
    main()
