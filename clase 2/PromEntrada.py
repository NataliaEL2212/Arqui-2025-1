def lee_num() -> int:
    
    #Lee un numero desde el terminal
    #Retorna un entero que presenta el numero ingresado

    while True:
        num = input("Ingrese un numero: ")
        try:
            num = int(num)
            break
        except ValueError:
            print("No se ingreso un numero valido. Vuelve a intentarlo")

    return int(num)

if __name__ == '__main__':

    acomulado = 0

    for i in range(4):
        resultado = lee_num()
        acomulado += resultado
    
    acomulado /= 4
        
    print(f"El promedio es: {acomulado}")