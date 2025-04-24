#Envía un mensaje al servidor y lo recibe de vuelta en 4 bytes
#la ñ en ASCII es un byte, pero en utf-8 son dos bytes

import socket

SOCK_BUFFER = 4


if __name__ == '__main__':
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 5003)

    print(f"Conectando a servidor: {server_address[0]}:{server_address[1]}")

    sock.connect(server_address)

    msg = "Hola mundo!"
    msg_bytes = msg.encode("utf-8")

    sock.sendall(msg_bytes)
    bytes_recibidos = 0 #variable para contabilizar los bytes recibidos
    bytes_esperados = len(msg_bytes) #variable para contar el total de bytes que se deben recibir

    full_msg = "" #str vacia para esperar el mensaje completo

    while bytes_recibidos < bytes_esperados: #mientras que no se hayan recibido los datos totales
        data = sock.recv(SOCK_BUFFER) #se reciben datos parciales en grupos de 4 bytes
        print(f"Recibi parcial: {data}") #observando los grupos de bytes
        bytes_recibidos += len(data) #vamos sumando el tamaño de cada mensaje parcial
        full_msg += data.decode("utf-8") #se pasa de byte a utf-8

    sock.close()

    print(f"Recibi: {full_msg}")

    #Resultado:
    #Recibi parcial: b'Hola'
    #Recibi parcial: b' mun'
    #Recibi parcial: b'do!'
    #Recibi: Hola mundo!