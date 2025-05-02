# Laboratorio 4. Pregunta 1
# Natalia Escudero 20223377

import socket
from random import randint

SOCK_BUFFER = 1024

if __name__ == '__main__':
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ("0.0.0.0", 9000)

    print(f"Iniciando servidor en {server_address[0]}:{server_address[1]}")

    sock.bind(server_address)

    sock.listen(5)

    while True:
        print("Esperando conexiones...")
        conn, client_address = sock.accept()

        print(f"Conexion desde {client_address[0]}:{client_address[1]}")

        valores_iniciales = conn.recv(SOCK_BUFFER) #recibe los valores iniciales
        valores = [int(val) for val in valores_iniciales.split(",")] #separamos cada valor
        media = valores[1] #la media
        varianza = valores[2] #la varianza

        try: 
            while True: 
                state = conn.recv(SOCK_BUFFER) #ahora empieza a recibir estados de B y C

                #0s
                if "FREE" in state: #siempre y cuando no esten ocupados, si lo estan no envia nada
                    temp = randint(10, 40)
                    msg = f"{datetime.datetime.now()|{temp}}" #
                    conn.sendall(msg) #envia simultaneamente a B y C
                time.sleep(0.5) #cada 0.5 vuelve a enviar

                #0.5s
                if "FREE" in state: 
                    temp = randint(10, 40)
                    conn.sendall(temp) 
                time.sleep.sleep(0.5)

                #1s
                alert = 0 #no hay alertas aun

                with open(f"B_metrics_{datetime.datetime.now()}.txt", "r", encoding="utf-8") as f: #revisa el archivo de B
                    media_B = f.read()
                if media_B > media: #alerta critica de B
                    printf(f"ALERTA: Media elevada: {media_B} > {media}")
                    alert += 1 #hay una alerta

                with open(f"C_metrics_{datetime.datetime.now()}.txt", "r", encoding="utf-8") as f: #revisa el archivo de C
                    varianza_C = f.read()
                if varianza_C > varianza:
                    printf(f"ALERTA: Varianza elevada: {varianza_C} > {varianza}")
                    alert += 1 #hay una alerta

                if alert == 2: #si ambas alertas se cumplen
                    nombre_alerta = f"WARNING_CRITICAL_FAILURE_{datetime.datetime.now()}.txt"
                    with open(nombre_alerta, "w", encoding="utf-8") as f: #crea un .txt con la alerta
                        f.write(f"CRITICAL FAILURE at {datetime.datetime.now()} media= {media_B}; varianza= {varianza_C}")
                    print(f"*** WARNING CRITICAL GENERATED:{nombre_alerta}") #avisa que hay dos alertas en la consola

        except ConnectionResetError:
            print("El cliente cerró la conexión de de manera abrupta")
        finally:
            print("Cerrando la conexión")
            conn.close()