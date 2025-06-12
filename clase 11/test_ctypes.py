import ctypes  # Importar el módulo ctypes para interactuar con librerías C/ensamblador

if __name__ == '__main__':

    # Definir tres números que se usarán en las operaciones
    x = 34654465
    y = 46546454
    z = 1322311

    # Cargar la librería compartida que contiene las funciones en C/ensamblador
    libreria = ctypes.CDLL('./lib_suma.so')

    # Configurar los tipos de los parámetros y el tipo de retorno de la función suma (C)
    libreria.suma.argtypes = [ctypes.c_ulonglong, ctypes.c_ulonglong]
    libreria.suma.restype = ctypes.c_ulonglong

    # Configurar los tipos de los parámetros y el tipo de retorno de la función suma_asm (Ensamblador)
    libreria.suma_asm.argtypes = [ctypes.c_ulonglong, ctypes.c_ulonglong]
    libreria.suma_asm.restype = ctypes.c_ulonglong

    # Llamar a la función suma (en C)
    print(libreria.suma(x, y))  # Imprime la suma de x + y usando la función en C
    # Llamar a la función suma_asm (en Ensamblador)
    print(libreria.suma_asm(x, y))  # Imprime la suma de x + y usando la función en Ensamblador
    # Mostrar la suma directamente en Python
    print(x + y)  # Imprime la suma de x + y directamente en Python

    # Configurar los tipos de los parámetros y el tipo de retorno de la función operacion
    libreria.operacion.argtypes = [ctypes.c_double]
    libreria.operacion.restype = ctypes.c_double

    # Llamar a la función operacion (en C o Ensamblador)
    print(libreria.operacion(x))  # Imprime 3.5 * x usando la función operacion
    # Calcular el mismo resultado directamente en Python
    print(3.5 * x)  # Imprime 3.5 * x directamente en Python
