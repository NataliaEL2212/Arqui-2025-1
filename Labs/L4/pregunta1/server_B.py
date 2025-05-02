# Laboratorio 4. Pregunta 1
# Natalia Escudero 20223377

#Servidor que espera 10 valores y obtiene la media

import socket

SOCK_BUFFER = 1024

if __name__ == '__main__':
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 8001)

    print(f"Iniciando servidor en {server_address[0]}:{server_address[1]}")

    sock.bind(server_address)

    sock.listen(5)

    while True:
        print("Esperando conexiones...")
        conn, client_address = sock.accept()

        print(f"Conexion desde {client_address[0]}:{client_address[1]}")

        sockFile = sock.makefile(mode='w') #crea el archivo

        try: 
            while True: 
                conn.sendall("FREE:B") #envia
                data = conn.recv(SOCK_BUFFER) 

                #Calcular varianza
                if(len(datos) == 10): #ya hay 10 datos

                    conn.sendall("BUSY:B") #envia
                    time.sleep(randint(1, 3)) #esperamos un tiempo aleatorio
                    datos = [int(val) for val in sockFile.split("\n")] #agrupamos los datos
                    varianza = statistics.mean(datos) #calculamos la media
                    nombre_B = f"B_metrics_{datetime.datetime.now()}.txt" #nombre del archivo B
                    with open(nombre_B, "w", encoding="utf-8"):
                        f.write(sockFile) #escribimos los 10 valores obtenidos

                elif data:
                    sockFile.write(data) #escribimos en el socket lo obtenido
                    sockFile.flush() #borramos los datos del socket para iniciar desde 0

                else:
                    print("No hay más datos")
                    break
        except ConnectionResetError:
            print("El cliente cerró la conexión de de manera abrupta")
        finally:
            print("Cerrando la conexión")
            conn.close()