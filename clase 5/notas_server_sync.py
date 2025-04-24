#Servidor que recibe el código de un alumno, abre un archivo csv con sus notas y devuelve al cliente la nota final 

import socket
import time

SOCK_BUFFER = 1024


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
        
                if data:
                    print(f"Recibi: {data}")
                    inicio = time.perf_counter()

                    #abrimos el archivo csv
                    with open("notas.csv", "r") as f:
                        contenido = f.read()

                    datos = contenido.split("\n")[1:] #dividimos en líneas
                    
                    for dato in datos:
                        valores = [int(val) for val in dato.split(",")] #separamos cada valor
                        if valores[0] == int(data): #si el código de alumno es igual al indicado
                            nota_final = calc_nota_final(valores[1:])
                            fin_cpu = time.perf_counter()
                            inicio_io = time.perf_counter()
                            conn.sendall(str(nota_final).encode("utf-8"))
                            fin = time.perf_counter()
                            break #dejamos de buscar
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
            print(f"Total de operacion: {(fin - inicio):.6f} segundos")
            print(f"Total de CPU: {(fin_cpu - inicio):0.6f} segundos")
            print(f"Total I/O: {(fin - inicio_io):.6f} segundos")

#Ahora si tuviéramos múltiples clientes, el servidor (un sistema síncrono), que no puede atender a varios al mismo tiempo, se va a ver forzado a atender en orden