'''def lee_num() -> int:
    
    #Lee un numero desde el terminal
    #Retorna un entero que presenta el promedio de una lista
    #Se utulizan listas para este ejercicio

    while True:
        num = input()
        try:
            num = int(num)
            break
        except ValueError:
            print("No se ingreso un numero valido. Vuelve a intentarlo")

    return num

if __name__ == '__main__':

    print("Ingrese la cantidad de numeros a promediar: ")
    rango = lee_num()

    nums = list()
    
    for _ in range(rango):
        print("Ingrese un numero: ")
        nums.append(lee_num())

    promedio = sum(nums) / len(nums)
        
    print(f"El promedio es: {promedio}")
    '''

#En la siguiente solución se muestra lo planteado por el profesor

'''
def lee_num(msg: str) -> int:

    while True:
        try:
            num = input(msg)  #TIENE QUE ESTAR DENTRO DEL BLOQUE TRY PARA QUE SE INTENTE ACCEDER A LA EXCEPCIÓN
            num = int(num)
            break
        except ValueError:
            print("No se ingreso un numero valido. Vuelve a intentarlo")
        except KeyboardInterrupt:
            print("El usuario ha cerrado el programa")
            exit(0)

    return num

if __name__ == '__main__':

    rango = lee_num("Ingrese la cantidad de muestras a tomar: ")

    nums = list()

    for _ in range(rango):
        nums.append(lee_num("Ingrese un numero: "))

    promedio = sum(nums) / len(nums)
        
    print(f"El promedio es: {promedio}")
'''

#Otro cambio

'''
def lee_num(msg: str) -> int | None:
    while True:
        try:
            num = input(msg)  #TIENE QUE ESTAR DENTRO DEL BLOQUE TRY PARA QUE SE INTENTE ACCEDER A LA EXCEPCIÓN
            if num.lower() == 'q':
                return None
            num = int(num)
            break
        except ValueError:
            print("No se ingreso un numero valido. Vuelve a intentarlo")
        except KeyboardInterrupt:
            print("\nEl usuario ha cerrado el programa")
            exit(0)

    return num

if __name__ == '__main__':

    nums = list()

    while True:
        numero = lee_num("Ingrese un numero u oprima 'q' para terminar: ")
        if numero is None:
            break

        nums.append(numero)

    promedio = sum(nums) / len(nums)
        
    print(f"El promedio es: {promedio}")
'''

#Otro cambio

'''
def lee_num(msg: str) -> int | None:
    while True:
        try:
            num = input(msg)  #TIENE QUE ESTAR DENTRO DEL BLOQUE TRY PARA QUE SE INTENTE ACCEDER A LA EXCEPCIÓN
            if num.lower() == 'q':
                return None
            num = int(num)
            break
        except ValueError:
            print("No se ingreso un numero valido. Vuelve a intentarlo")
        except KeyboardInterrupt:
            print("\nEl usuario ha cerrado el programa")
            exit(0)

    return num

if __name__ == '__main__':

    nums = list()

    idx = 0
    while True:
        numero = lee_num("Ingrese un numero para la muestra {idx + 1} u oprima 'q' para terminar: ")
        if rango is None:
            break
        nums.append(numero)
        idx += 1

    promedio = sum(nums) / len(nums)
        
    print(f"El promedio es: {idx} muestras es: {promedio}")
'''
