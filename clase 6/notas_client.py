import socket
from random import randint
import time

SOCK_BUFFER = 1024


if __name__ == '__main__':
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 5000)

    print(f"Conectando a servidor: {server_address[0]}:{server_address[1]}")

    sock.connect(server_address)
    nota_base = 20250001

    msg = f"{nota_base + randint(0, 200)}"
    inicio = time.perf_counter()
    sock.sendall(msg.encode("utf-8"))
    data = sock.recv(SOCK_BUFFER)
    fin = time.perf_counter()
    sock.close()

    print(f"Recibi: {data}")
    print(f"Tiempo total de la operacion I/O: {(fin - inicio):.6f} segundos")
