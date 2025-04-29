import asyncio
import time


async def cuenta():
    print(f"Uno")
    await asyncio.sleep(1)
    print(f"Dos")


async def main():
    await asyncio.gather(cuenta(), cuenta(), cuenta())


if __name__ == "__main__":
    inicio = time.perf_counter()
    asyncio.run(main())
    fin = time.perf_counter()

    t_ejecucion = fin - inicio

    print(f"Tiempo total de ejecucion: {t_ejecucion:.6f} segundos")
