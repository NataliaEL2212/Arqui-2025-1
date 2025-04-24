#Envía un mensaje al servidor

import socket
import time

SOCK_BUFFER = 1024


if __name__ == '__main__':
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 5007)

    print(f"Conectando a servidor: {server_address[0]}:{server_address[1]}")

    sock.connect(server_address)

    msg = "20250020,20,3,18,16,1,9,2,8,15,4,14,4,14,1"

    inicio = time.perf_counter()
    #socket.sendall(msg) #va a haber un problema porque esta esperando en formato bytes, no str
    sock.sendall(msg.encode("utf-8"))
    data = sock.recv(SOCK_BUFFER)

    fin = time.perf_counter()

    sock.close()

    print(f"Recibi: {data}")

    t_ejecucion = fin - inicio
    print(f"Tiempo total de ejecucion: {t_ejecucion:.5f} segundos.")

    