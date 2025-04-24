#concurrencia:
    #todos tienen el mismo nivel de prioridad, es decir, si se tuvieran múltiples jugadores se buscará secuencialmente el primero que esté disponible, si existe uno que tenga mayor prioridad no se elegirá primero como con las interrupciones

#Python utiliza una librería para manejar los procesos asíncronos, llamada asyncio
#Para usar asyncio, es decir hacer operaciones concurrentes, el código asíncrono debe ejecutarse dentro de "corrutinas". Una corrutina es una función asíncrona, se señala colocando un async antes del def. La parte asíncrona del código sólo puede ser ejecutada dentro de la
#corrutina,  para llamar esa función se usa un "await" (esperar a que termine la corrutina).

import asyncio
import time

async def cuenta(): #nuestra función asíncrona
    print(f"Uno")
    await asyncio.sleep(1) #espera hasta que termine el sleep asíncrono 
    print(f"Dos")

async def main(): #el programa arranca siendo síncrono, pero no se puede usar asyncio en un programa síncrono, por lo que se crea este loop asíncrono para usar la función
    await asyncio.gather(cuenta(), cuenta(), cuenta()) #bloquea el código hasta que todas las funciones sea ejecutada
    
if __name__ == '__main__':
    inicio = time.perf_counter()
    asyncio.run(main()) #corre un código asíncrono para que todo el main se ejecute
    fin = time.perf_counter()

    t_ejecucion = fin - inicio
    print(f"Timepo total de ejecución: {t_ejecucion:.6f} segundos")

'''
Uno
Uno
Uno
Dos
Dos
Dos
Timepo total de ejecución: 1.002876 segundos
''' #a diferencia del código síncrono, ha disminuido bastante el tiempo de ejecución