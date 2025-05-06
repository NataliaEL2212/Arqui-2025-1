import asyncio
import time

SOCK_BUFFER = 1024


async def nota_client(codigo: str) -> float:
    """
    Envia una solicitud de codigo de alumno al servidor de manera asincrona y recibe una respuesta de la nota final.
    :param codigo: str representando el codigo de alumno
    :returns: Nota final representada como float
    """
    reader, writer = await asyncio.open_connection('localhost', 5000)

    print(f'Send: {codigo!r}')
    writer.write(codigo.encode("utf-8"))
    await writer.drain()

    data = await reader.read(SOCK_BUFFER)
    print(f'Received: {data.decode("utf-8")!r}')

    print('Close the connection')
    writer.close()
    await writer.wait_closed()

    return float(data.decode("utf-8"))


async def main(codigos: list[str]) -> list[float]:
    notas = await asyncio.gather(*(nota_client(codigo) for codigo in codigos))

    return notas


if __name__ == '__main__':
    inicio = time.perf_counter()
    notas = asyncio.run(main(['20250001', '20250002', '20250003', '20250004', '20250005']))
    fin = time.perf_counter()

    print(notas)

    print(f"Tiempo total de ejecucion: {(fin - inicio):.6f} segundos")