# Laboratorio 4. Pregunta 1
# Natalia Escudero 20223377

#Cliente

import sys
import socket

if __name__ == '__main__':
    m = sys.argv[1]
    n = sys.argv[2]

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 9000)

    print(f"Conectando a servidor: {server_address[0]}:{server_address[1]}")

    sock.connect(server_address)

    msg = f"{m},{n}" #parametros de media y varianza
    
    sock.sendall(msg.encode("utf-8")) #envia los parametros al servidor A

    print(f"Parámetros enviados")
    sock.close()
