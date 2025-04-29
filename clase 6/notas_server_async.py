import socket
import asyncio
from random import randint
import time

SOCK_BUFFER = 1024

def busca_notas(codigo: str) -> list[int]:
    """
    Busca las notas correspondientes al codigo de alumno suministrado
    :param codigo: string que contiene el codigo del alumno
    :returns: lista de enteros con las notas correspondientes al codigo
    """
    with open("notas.csv", "r") as f:
        contenido = f.read()
    
    contenido = contenido.split("\n")

    notas = list()
    for fila in contenido:
        if codigo in fila:
            notas = [int(valor) for valor in fila.split(",")[1:]]
            break
    return notas


def calc_nota_final(notas: list[int]) -> float:
    """
    Calcula la nota final en base a una lista de notas especificas.
    :param notas: Lista de notas que el cliente envia.
    :returns: float con el valor de la nota final.
    """
    notas_labs = notas[0:12]
    e1 = notas[12]
    e2 = notas[13]

    lab = sum(notas_labs) / len(notas_labs)

    nota_final = ((5 * lab) + (2.5 * e1) + (2.5 * e2)) / 10

    return nota_final


async def main(): 
    server_adress = ("0.0.0.0", 5000)

    server = await asyncio.start_server(handle_client, server_adress[0], server_adress[1]) #esta funcion hace toda la creacion y configuracion del servidor
    #el callback nos permite ceder el desarrollo del programa a la maquina y esperar a que esta tenga interrupciones para manejar sus eventos, es como una corrutina

    async with server:
        print(f"Iniciando el servidor en {server_adress[0]}:{server_adress[1]}")
        await server.serve_forever() #se pasa el control del programa al serve_forever, que esperara que un cliente se conecte para calcular la nota.
        #No todos los servidores TCP funcionan asi, depende de su aplicacion y la logica de su programa. Debemos definir la logica de nuestro servidor cuando se conecte un cliente (handle_client), de eso se encarga el callback


async def handle_client(reader: asyncio.StreamReader, writer: asyncio.StreamWriter):
    print("cliente conectado")

    try:
        while True:
            data = await reader.read(SOCK_BUFFER) #leemos la data
            await asyncio.sleep(randint(3,7)) #esperamos un tiempo aleatorio
            if data:
                codigo = data.decode("utf-8") #decodificamos el codigo
                valores = busca_notas(codigo) #buscamos las notas
                if len(valores) > 0:
                    nota_final = calc_nota_final(valores) #calcular la nota final
                else:
                    nota_final = -1 #error
                writer.write(str(nota_final).encode("utf-8")) #decodificamos la nota final y la enviamos
                await writer.drain() #esperamos a que el buffer se vacie para volver a escribir
            else:
                print("No hay mas datos") #termina
                break
    except KeyboardInterrupt:
            print("Usuario terminó el servidor")
    except ConnectionResetError:
        print("El cliente cerró la conexión de de manera abrupta")
    finally:
        writer.close()
        await writer.wait_closed()

if __name__ == "__main__":
    asyncio.run(main()) #corremos el programa asincrono principal

    #corrutina = llamar multiples veces a una funcion asincrona
    '''
    Tiempo total de ejecucion: 6.005310 segundos
    '''
    #Observamos una gran diferencia con el servidor sincrono, ahora si se pueden atender a varios clientes al mismo tiempo
    #Si a un servidor asíncrono le introduces un time.sleep se vuelve síncrono
