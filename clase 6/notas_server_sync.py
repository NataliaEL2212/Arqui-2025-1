import socket
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


if __name__ == '__main__':
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ("0.0.0.0", 5000)

    print(f"Iniciando servidor en {server_address[0]}:{server_address[1]}")

    sock.bind(server_address)

    sock.listen(5)

    while True:
        print("Esperando conexiones...")
        conn, client_address = sock.accept()

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
                else:
                    print("No hay más datos")
                    break
        except KeyboardInterrupt:
            print("Usuario terminó el servidor")
        except ConnectionResetError:
            print("El cliente cerró la conexión de de manera abrupta")
        finally:
            print("Cerrando la conexión")
            conn.close()
