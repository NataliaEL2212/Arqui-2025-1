# Un servidor es un programa cuyo propósito es servir algo, ya sea una base de datos, un servidor web, entre otros. Se pueden almacenar múltiples servidores en una sola computadora, y se distinguen por medio de "puertos". Un puerto es un elemento lógico (16 bits)
# que permite identificar servidores en una red de computadoras. Se utiliza un socket, que es la combinación de IP + Puerto. Para Python, se utilizará la librería socket. Crearemos un servidor

import socket

SOCK_BUFFER = 1024 #variable de 1024 bites (1KB)

if __name__ == '__main__':
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # familia, tipo de socket
    server_address = ("0.0.0.0", 5003) # 0.0.0.0 indica al socket que escuche en todas las interfaces disponibles. 5000 es el puerto que usaremos, una opción segura porque no suele usarse

    print(f"Iniciando servidor en {server_address[0]}:{server_address[1]}")

    sock.bind(server_address) #adjuntamos el socket

    sock.listen(5)

    while True:
        print("Esperando conexiones...")
        conn, client_address = sock.accept()

        print(f"Conexion desde {client_address[0]}:{client_address[1]}")

        try: 
            while True: 
                data = conn.recv(SOCK_BUFFER) #esperamos que se llene el buffer, el resultado se guarda en data

                if data: #verificamos si data esta vacio
                    print(f"Recibi: {data}")
                    conn.sendall(data) #retornamos el valor, porque este servidor cumple la funcion de un echo
                else:
                    print("No hay más datos")
                    break
        except ConnectionResetError:
            print("El cliente cerró la conexión de de manera abrupta")
        finally:
            print("Cerrando la conexión")
            conn.close()
 