def lee_num() -> int:
    
    #Lee un numero desde el terminal
    #Retorna un entero que presenta el numero ingresado
    #Se utulizan listas para este ejercicio

    while True:
        num = input("Ingrese un numero: ")
        try:
            num = int(num)
            break
        except ValueError:
            print("No se ingreso un numero valido. Vuelve a intentarlo")

    return num

if __name__ == '__main__':

    nums = list()
    
    for _ in range(4):
        nums.append(lee_num())

    promedio = sum(nums) / len(nums)
        
    print(f"El promedio es: {promedio}")

    #