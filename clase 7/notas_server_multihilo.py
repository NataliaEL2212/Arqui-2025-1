# notas_server pero utilizando multihilo. Usando el codigo de notas_server_sync como base:

import socket
import time
from threading import Thread
from random import randint

SOCK_BUFFER = 1024
#texto = "hola mundo" #variable global usada para observar como los threads comparten espacio de memoria
contador_cliente = 0

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

def handle_client(conn: socket.socket, client_address: tuple[str, int]): #funcion que se anclará al thread, recibe como entradas el conn y el client adress de cada solicitud
    global contador_cliente #le indicamos a python que no es necesario crear una nueva variable y que use como referencia la global externa. No es obligatorio pero es una precaución
    contador_cliente += 1
    print(f"Numero de clientes conectados concurrentemente: {contador_cliente}") #observamos cuantos clientes hay conectados concurrentemente
    print(f"Conexion desde {client_address[0]}:{client_address[1]}")
    try: 
        while True:
            data = conn.recv(SOCK_BUFFER)
            time.sleep(randint(3, 7))
            if data:
                print(f"Recibi: {data}")

                codigo = data.decode("utf-8")
                valores = busca_notas(codigo)
                if len(valores) > 0:
                    nota_final = calc_nota_final(valores)
                else:
                    nota_final = -1
                conn.sendall(str(nota_final).encode("utf-8"))
                #print(texto) #demostramos que las variables globales pueden ser vistas en todos los threads porque comparten el mismo espacio de memoria
            else:
                print("No hay más datos")
                break
    except KeyboardInterrupt:
        print("Usuario terminó el servidor")
    except ConnectionResetError:
        print("El cliente cerró la conexión de de manera abrupta")
    finally:
        print("Cerrando la conexión")
        contador_cliente -= 1 #se desconecta un cliente
        print(f"Numero de clientes conectados concurrentemente: {contador_cliente}") #observamos cuantos clientes hay conectados concurrentemente
        conn.close()

if __name__ == '__main__':
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ("0.0.0.0", 5000)

    print(f"Iniciando servidor en {server_address[0]}:{server_address[1]}")

    sock.bind(server_address)

    sock.listen(5)

    while True:
        print("Esperando conexiones...")
        conn, client_address = sock.accept()
        t = Thread(target=handle_client, args=(conn,client_address)) #podemos usar el mismo nombre del thread
        t.start()
        #no se usa join porque sino esperara a que termine cada cliente y tendremos una cola, dejará de ser multicliente

        

        