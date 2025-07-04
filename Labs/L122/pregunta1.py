#Lab 12
#Natalia Cristina Escudero Lay 
#20223377

import ctypes
import numpy as np
import time
import matplotlib.pyplot as plt

def convolucionar_vector(xn,hk,yn,N,K):
    for n in range(0,N):
        for k in range(0,K):
            if n - k >= 0: #de lo contrario x[n-k]=0 por lo que y[n]=0 (y[n] nunca fue inicializado)
                yn[n] = yn[n] + xn[n-k]*hk[k] 

if __name__ == '__main__':
    #Cargando la librería compartida
    lib = ctypes.CDLL('./lib_convolucion.so')
    
    #Parámetros y retornos de las funciones de la librería compartida
    lib.convolucionar_vector_c_float.argtypes = [np.ctypeslib.ndpointer(dtype=np.float32), np.ctypeslib.ndpointer(dtype=np.float32), np.ctypeslib.ndpointer(dtype=np.float32), ctypes.c_ulonglong, ctypes.c_ulonglong]
    lib.convolucionar_vector_asm_float.argtypes = [np.ctypeslib.ndpointer(dtype=np.float32), np.ctypeslib.ndpointer(dtype=np.float32), np.ctypeslib.ndpointer(dtype=np.float32), ctypes.c_ulonglong, ctypes.c_ulonglong]
    lib.convolucionar_vector_asm_float_simd.argtypes = [np.ctypeslib.ndpointer(dtype=np.float32), np.ctypeslib.ndpointer(dtype=np.float32), np.ctypeslib.ndpointer(dtype=np.float32), ctypes.c_ulonglong, ctypes.c_ulonglong]

    #Definiendo los valores iniciales
    N = [16, 64, 256, 1024, 4096, 16384, 65536]
    K = 4

    #Definiendo las listas donde se guardarán los tiempos de ejecución
    tiempos_python = list()
    tiempos_c = list()
    tiempos_asm = list()
    tiempos_asm_simd = list()

#Por cada N
    for n in N:
        #Creamos los arreglos de números flotantes aleatorios entre 0 y 1, y los convertimos a tipo float32
        xn_float = np.random.random(n).astype(np.float32)
        hk_float = np.random.random(K).astype(np.float32)

        # Inicializamos los arreglos de salida para almacenar los resultados de cada implementación
        yn_float = np.random.random(n+K-1).astype(np.float32) #vector de salida de ejemplo, luego se vacia el arreglo

        yn_float_out = np.zeros_like(yn_float)          #Python
        yn_float_out2 = np.zeros_like(yn_float)         #C
        yn_float_out3 = np.zeros_like(yn_float)         #ASM
        yn_float_out4 = np.zeros_like(yn_float)         #ASM-SIMD
        
        # Medición de los tiempos para la implementación en Python
        t1 = time.perf_counter()  
        convolucionar_vector(xn_float, hk_float, yn_float_out, n, K)
        t2 = time.perf_counter() 
        tiempos_python.append(t2-t1)

        # Medición de los tiempos para la implementación en C
        t1 = time.perf_counter()  
        lib.convolucionar_vector_c_float(xn_float, hk_float, yn_float_out2, n, K)
        t2 = time.perf_counter() 
        tiempos_c.append(t2-t1)

        # Medición de los tiempos para la implementación en ASM
        t1 = time.perf_counter()  
        lib.convolucionar_vector_asm_float(xn_float, hk_float, yn_float_out3, n, K)
        t2 = time.perf_counter() 
        tiempos_asm.append(t2-t1)

        # Medición de los tiempos para la implementación en ASM_SIMD
        t1 = time.perf_counter()
        lib.convolucionar_vector_asm_float_simd(xn_float, hk_float, yn_float_out4, n, K)
        t2 = time.perf_counter() 
        tiempos_asm_simd.append(t2-t1)
        
    #Generando las gráficas con la librería matplotlib 
    print(tiempos_python)
    plt.plot(N, tiempos_python,'y')
    plt.plot(N, tiempos_c,'b')
    plt.plot(N, tiempos_asm,'g')
    plt.plot(N, tiempos_asm_simd,'r')

    plt.grid()
    plt.title("Gráfica de tiempo de ejecución vs N")
    plt.xlabel("Valores de N")
    plt.ylabel("Tiempo de ejecución")
    plt.legend(['Python','C','ASM','ASM_SIMD'])

    plt.savefig("pregunta1.png",dpi = 300)
    plt.close()