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

    acumulado = 0

    for i in range(4):
        acumulado += nums[i]
    
    print(nums)
    acumulado /= 4
        
    print(f"El promedio es: {acumulado}")

    #En python existen iterables, que son conjuntos de datos que pueden ser iterados. Para los iterables, "range" indica la cantidad de iteraciones
    #for i in range(4):
    #   print(l[i])
    #es igual a:
    #for i in l
    #   print(l[i])