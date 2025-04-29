import asyncio
import time
from random import randint

SOCK_BUFFER = 1024

async def nota_client(codigo: str) -> float:
    #Envia una solicitud de codigo de alumno al servidor de manera asincrona y recibe una respuesta 
    # :param codigo: str representando el codigo de alumno
    # :returns: Nota final representada como float
    reader, writer = await asyncio.open_connection('127.0.0.1', 5000) #(host, port) #donde reader es el reemplazo del socket para lectura y writer para escritura. 127.0.0.1 es en realidad localhost, solo con otro nombre
    print(f'Send: {codigo!r}')
    writer.write(codigo.encode("utf-8")) #enviar el codigo
    await writer.drain() #se asegura que el buffer de escritura esté completamente limpio para su escritura. .write siempre se usa con .drain (obligatorio)

    data = await reader.read(SOCK_BUFFER) #esperar a que devuelva la nota final
    print(f'Receiver: {float(data.decode("utf-8"))}') #imprimir el valor en la terminal

    print('Close the connection')
    writer.close() #cerrar la conexion
    await writer.wait_closed() #esperar a que se cierre. .close siempre se usa con .wait_closed (recomendacion)

async def main(): #para usar el gather debe usarse una funcion main asincrona. Esta es nuestra corrutina
    await asyncio.gather(nota_client(str(randint(20250001,20250200))), nota_client(str(randint(20250001,20250200))), nota_client(str(randint(20250001,20250200))), nota_client(str(randint(20250001,20250200))), nota_client(str(randint(20250001,20250200)))) #se crean codigos aleatorios
    #notas = asyncio.gather(*(nota_client(codigo) for codigo in codigos)) #el * es para iterarlo, gather no puede recibir un iterable entonces el * "unpacking operator" lo convierte en una lista

if __name__ == '__main__':
    inicio = time.perf_counter()
    asyncio.run(main()) #correr el main asincrono
    fin = time.perf_counter()

    t_ejecucion = fin - inicio

    print(f"Tiempo total de ejecucion: {t_ejecucion:.6f} segundos")

    '''
    Tiempo total de ejecucion: 45.050876 segundos
    '''

    #Se demora bastante porque el servidor es síncrono y solo atiende una conexión a la vez. Incluso si los 5 clientes son asíncronos, el servidor escucha uno por uno
