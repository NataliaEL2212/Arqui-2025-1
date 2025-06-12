import ctypes
import numpy as np

# Función en Python que multiplica cada elemento del arreglo por un escalar
def arreglo_escalar(arreglo, escalar, arreglo_de_salida, N):
    for i in range(N):
        arreglo_de_salida[i] = arreglo[i] * escalar

if __name__ == '__main__':

    # Cargar la librería compartida que contiene las funciones en C y ensamblador
    lib_arreglos = ctypes.CDLL('./lib_arreglos.so')
    
    # Definir los tipos de los argumentos para las funciones de la librería
    lib_arreglos.arreglo_escalar_c.argtypes = [np.ctypeslib.ndpointer(dtype=np.uint64), ctypes.c_uint64, np.ctypeslib.ndpointer(dtype=np.uint64), ctypes.c_int32]
    lib_arreglos.arreglo_escalar_asm.argtypes = [np.ctypeslib.ndpointer(dtype=np.uint64), ctypes.c_uint64, np.ctypeslib.ndpointer(dtype=np.uint64), ctypes.c_int32]
    
    # Crear un arreglo de entrada aleatorio con valores entre 10 y 20, con tamaño 100
    arreglo_a = np.random.randint(10, 20, 100, dtype=np.uint64)
    escalar = 10  # Valor escalar con el que se multiplicarán los elementos del arreglo
    
    print("Arreglo original:")
    print(arreglo_a)

    # Inicializar los arreglos de salida
    arreglo_salida = np.zeros_like(arreglo_a)
    arreglo_salida2 = np.zeros_like(arreglo_a)
    arreglo_salida3 = np.zeros_like(arreglo_a)

    # Ejecutar la multiplicación usando la función en Python
    print("Python:")
    arreglo_escalar(arreglo_a, escalar, arreglo_salida, 100)
    print(arreglo_salida)

    # Ejecutar la multiplicación usando la función en C (desde la librería compartida)
    print("C:")
    lib_arreglos.arreglo_escalar_c(arreglo_a, escalar, arreglo_salida2, 100)
    print(arreglo_salida2)

    # Ejecutar la multiplicación usando la función en ensamblador (desde la librería compartida)
    print("ASM:")
    lib_arreglos.arreglo_escalar_asm(arreglo_a, escalar, arreglo_salida3, 100)
    print(arreglo_salida3)
