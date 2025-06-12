import ctypes  # Importamos el módulo ctypes para interactuar con librerías compartidas en C/ensamblador
import numpy as np  # Importamos numpy para crear y manejar los arreglos numéricos
import time  # Importamos time para medir el tiempo de ejecución de las funciones

# Función en Python para realizar la multiplicación escalar
def arreglo_escalar(arreglo, escalar, arreglo_de_salida, N):
    # Itera sobre cada elemento del arreglo y lo multiplica por el escalar
    for i in range(N):
        arreglo_de_salida[i] = arreglo[i] * escalar  # Multiplicación escalar y almacenamiento en arreglo_de_salida

if __name__ == '__main__':
    # Cargamos la librería compartida que contiene las funciones en C/ensamblador
    lib = ctypes.CDLL('./lib_arreglos_escalar_float.so')

    # Definimos los tipos de los parámetros y el tipo de retorno de las funciones dentro de la librería compartida
    lib.arreglo_escalar_c_float.argtypes = [np.ctypeslib.ndpointer(dtype=np.float32), ctypes.c_float, np.ctypeslib.ndpointer(dtype=np.float32), ctypes.c_int32]
    lib.arreglo_escalar_asm_float.argtypes = [np.ctypeslib.ndpointer(dtype=np.float32), ctypes.c_float, np.ctypeslib.ndpointer(dtype=np.float32), ctypes.c_int32]
    lib.arreglo_escalar_asm_float_simd.argtypes = [np.ctypeslib.ndpointer(dtype=np.float32), ctypes.c_float, np.ctypeslib.ndpointer(dtype=np.float32), ctypes.c_int32]

    # Definimos el tamaño del arreglo y el escalar
    N = 1024*1024  # Número de elementos en el arreglo
    escalar = 10  # Valor escalar con el cual multiplicar cada elemento

    # Creamos el arreglo de números flotantes aleatorios entre 0 y 1, y lo convertimos a tipo float32
    arreglo_float = np.random.random(N).astype(np.float32)

    # Inicializamos los arreglos de salida para almacenar los resultados de cada implementación
    arreglo_float_out = np.zeros_like(arreglo_float)
    arreglo_float_out2 = np.zeros_like(arreglo_float)
    arreglo_float_out3 = np.zeros_like(arreglo_float)
    arreglo_float_out4 = np.zeros_like(arreglo_float)

    # Medición del tiempo para la implementación en Python
    t1 = time.perf_counter()  # Guardamos el tiempo de inicio
    arreglo_escalar(arreglo_float, escalar, arreglo_float_out, N)  # Llamamos a la función de Python para multiplicar el arreglo
    t2 = time.perf_counter()  # Guardamos el tiempo de finalización
    print("Tiempo Python:", t2 - t1)  # Imprimimos el tiempo transcurrido

    # Medición del tiempo para la implementación en C
    t1 = time.perf_counter()
    lib.arreglo_escalar_c_float(arreglo_float, escalar, arreglo_float_out2, N)  # Llamamos a la función en C para multiplicar el arreglo
    t2 = time.perf_counter()
    print("Tiempo C:", t2 - t1)  # Imprimimos el tiempo transcurrido

    # Medición del tiempo para la implementación en ensamblador
    t1 = time.perf_counter()
    lib.arreglo_escalar_asm_float(arreglo_float, escalar, arreglo_float_out3, N)  # Llamamos a la función en ensamblador para multiplicar el arreglo
    t2 = time.perf_counter()
    print("Tiempo Ensamblador:", t2 - t1)  # Imprimimos el tiempo transcurrido

    # Medición del tiempo para la implementación en ensamblador con SIMD
    t1 = time.perf_counter()
    lib.arreglo_escalar_asm_float_simd(arreglo_float, escalar, arreglo_float_out4, N)  # Llamamos a la función en ensamblador con SIMD para multiplicar el arreglo
    t2 = time.p
