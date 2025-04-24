#Cliente que recibe como input de la terminal el código de un alumno y lo envía al servidor, luego muestra lo que devuelve el servidor, que es la nota final del alumno

import socket
import time

SOCK_BUFFER = 1024


if __name__ == '__main__':
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 5000)

    print(f"Conectando a servidor: {server_address[0]}:{server_address[1]}")

    sock.connect(server_address)

    msg = input("Inserte el código del alumno: ")
    inicio = time.perf_counter()
    sock.sendall(msg.encode("utf-8"))
    data = sock.recv(SOCK_BUFFER)
    fin = time.perf_counter()
    sock.close()

    print(f"La nota final es: {data}")
    print(f"Tiempo total de la operacion I/O: {(fin - inicio):.6f} segundos")