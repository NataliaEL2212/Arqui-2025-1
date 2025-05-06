#Crea dos hilos y modificamos el valor inicial. Simulamos un race condition para observar como ocurre, el Global Interpreter Lock nunca permitirá que ocurra uno naturalmente. Esto es bueno porque evitará problemas de vulnerabilidad, pero malo porque no se puede 
#hacer paralelismo sin usar multiprocessing, la cual es una alternativa muy costosa en base a recursos (crea múltiples procesos con múltiples intérpretes) y puede crear race conditions no sólo en memoria, pero en otros factores.

import time
from concurrent.futures import ThreadPoolExecutor #Nueva librería que usaremos para crear threads. Es más avanzada que Threading y puede crear pools, lo que significa que los threads no se eliminan apenas terminen y su ejecución es más rápida. Conforme un hilo se
#libera se le asignan más tareas. Es decir, para 10k tareas no es necesario crear 10k hilos.

class FakeDatabase:
    def __init__(self):
        self.value = 0
    def actualiza(self, nombre: str) -> None:
        print(f"[Thread {nombre}] Esperando actualzación")
        copia_local = self.value
        copia_local += 1
        time.sleep(0.1) #forzamos un race condition cambiando al otro hilo. No hay garantia del orden de ejecucion, no sabemos cuál inició antes
        self.value = copia_local
        print(f"[Thread {nombre}] Terminando actualización")

if __name__ == '__main__':
    db = FakeDatabase()

    print(f"[Main] Valor inicial de la base de datos: {db.value}")

    with ThreadPoolExecutor(max_workers=2) as executor: #define dos hilos para que ejecuten actualiza()
        for i in range(2):
            executor.submit(db.actualiza, f"t{i}")

    print(f"[Main] Valor final de la base de datos: {db.value}")