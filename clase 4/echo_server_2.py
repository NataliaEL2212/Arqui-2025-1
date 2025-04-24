# Ahora el servidor va a recibir una cadena con notas, la va a descomponer, y luego devolverá la nota final

import socket
import time

SOCK_BUFFER = 1024 #variable de 1024 bites (1KB)

def calc_nota_final(notas: list[int]) -> float:
    #calcula la nota final en base a una lista de notas especificas
    notas_labs = valores[1:13]
    e1 = valores[13]
    e2 = valores[14]

    lab = sum(notas_labs) / len(notas_labs)

    nota_final = ((5 * lab) + (2.5 * e1) + (2.5 * e2)) / 10

    return nota_final

if __name__ == '__main__':
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # familia, tipo de socket
    server_address = ("0.0.0.0", 5007) # 0.0.0.0 indica al socket que escuche en todas las interfaces disponibles. 5000 es el puerto que usaremos, una opción segura porque no suele usarse

    print(f"Iniciando servidor en {server_address[0]}:{server_address[1]}")

    sock.bind(server_address) #adjuntamos el socket

    sock.listen(5)

    while True:
        print("Esperando conexiones...")
        conn, client_address = sock.accept()

        print(f"Conexion desde {client_address[0]}:{client_address[1]}")

        try: 
           while True: 
                #si aca se colocara inicio, siempre que se iterara el bucle se reescribiría el valor IMPORTANTE!!!
                data = conn.recv(SOCK_BUFFER) #esperamos que se llene el buffer, el resultado se guarda en data
                if data: #verificamos si data esta vacio
                    print(f"Recibi: {data}")
                    inicio = time.perf_counter() #para contabilizar solamente el tiempo que el servidor demora en realizar la operacion
                    valores = data.decode("utf-8").split(",") #decodificamos de utf-8 a str
                    valores = [int(valor) for valor in valores] #pasamos de str a int
                    nota_final = calc_nota_final(valores[1:]) #devuelve un float
                    conn.sendall(str(nota_final).encode("utf-8")) #convertimos a string, luego codificamos a utf-8 y enviamos
                    fin = time.perf_counter() #se termina el cronómetro una vez que se envía de vuelta. en teoría, debería ser el mismo tiempo que toma el cliente en realizar su tarea, sin contar el tiempo que el dato demora en viajar
                else:
                    print("No hay más datos")
                    break
        except ConnectionResetError:
            print("El cliente cerró la conexión de de manera abrupta")
        finally:
            t_ejecucion = fin - inicio
            print(f"Tiempo total de ejecucion: {t_ejecucion:.5f} segundos.")
            print("Cerrando la conexión")
            conn.close()
 