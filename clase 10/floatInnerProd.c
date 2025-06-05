#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>

// Declaración de funciones externas implementadas en ensamblador
extern float asmFloatInnerProd_v2(float *v1, float *v2, int N);  // Función asm que retorna el producto punto
extern void asmFloatInnerProd(float *v1, float *v2, int N, float *ip);  // Función asm que guarda el producto punto en ip

// Declaración de funciones auxiliares
void initVector(float *v, int N);  // Inicializa un vector con valores aleatorios
void cFloatInnerProd(float *v1, float *v2, int N, float *ip);  // Calcula el producto punto de dos vectores en C
float cFloatInnerProd_v2(float *v1, float *v2, int N);  // Versión de cFloatInnerProd que retorna el valor directamente
float calcRelErr(float ref, float cal);  // Calcula el error relativo entre el valor calculado y el valor de referencia

int main()
{
    // Inicializa la semilla para los números aleatorios utilizando el tiempo actual
    srandom(time(NULL));

    // Declaración de variables
    float *v1, *v2, ipC, ipAsm, ipCA, ipAsmA;
    int N = 1024;  // Tamaño de los vectores

    // Reserva memoria dinámica para los vectores v1 y v2
    v1 = malloc(N * sizeof(float));
    v2 = malloc(N * sizeof(float));

    // Inicializa los vectores con valores aleatorios
    initVector(v1, N);
    initVector(v2, N);

    // Variables para medir el tiempo de ejecución
    struct timespec ti, tf;
    double elapsed;

    // Medir el tiempo de ejecución de la función en C
    clock_gettime(CLOCK_REALTIME, &ti);  // Obtiene el tiempo de inicio
    cFloatInnerProd(v1, v2, N, &ipC);  // Llama a la función que calcula el producto punto en C
    clock_gettime(CLOCK_REALTIME, &tf);  // Obtiene el tiempo de fin
    // Calcula el tiempo transcurrido en nanosegundos
    elapsed = (tf.tv_sec - ti.tv_sec) * 1e9 + (tf.tv_nsec - ti.tv_nsec);
    printf("El tiempo en nanosegundos que toma la función en C es %lf\n", elapsed);

    // Medir el tiempo de ejecución de la función en ensamblador
    clock_gettime(CLOCK_REALTIME, &ti);  // Obtiene el tiempo de inicio
    asmFloatInnerProd(v1, v2, N, &ipAsm);  // Llama a la función que calcula el producto punto en ensamblador
    clock_gettime(CLOCK_REALTIME, &tf);  // Obtiene el tiempo de fin
    // Calcula el tiempo transcurrido en nanosegundos
    elapsed = (tf.tv_sec - ti.tv_sec) * 1e9 + (tf.tv_nsec - ti.tv_nsec);
    printf("El tiempo en nanosegundos que toma la función en ASM es %lf\n", elapsed);

    // Calcula el producto punto utilizando las versiones que retornan un valor
    ipCA = cFloatInnerProd_v2(v1, v2, N);  // Cálculo en C
    ipAsmA = asmFloatInnerProd_v2(v1, v2, N);  // Cálculo en ensamblador

    // Opcional: Descomentar para imprimir los resultados de producto punto
    // printf("Resultado con void C %f \n", ipC);
    // printf("Resultado con void asm %f \n", ipAsm);
    // printf("Resultado con retorno C %f \n", ipCA);
    // printf("Resultado con retorno asm %f \n", ipAsmA);

    // Liberar la memoria reservada para los vectores
    free(v1);
    free(v2);

    return 0;
};

// Función para inicializar un vector con valores aleatorios basados en las funciones trigonométricas
void initVector(float *v, int N)
{
    for (int i = 0; i < N; i++)
    {
        // Genera un número aleatorio entre 0 y 254
        float e = random() % 255;
        // Asigna a cada elemento del vector la suma de sin(e) y cos(e)
        v[i] = (sinf(e) + cosf(e));
    }
}

// Función para calcular el producto punto entre dos vectores utilizando C (con puntero para almacenar el resultado)
void cFloatInnerProd(float *v1, float *v2, int N, float *ip)
{
    int i = 0;
    float sum = 0;
    // Calcula el producto punto recorriendo los vectores
    for (i = 0; i < N; i++)
    {
        sum += v1[i] * v2[i];  // Suma los productos de los elementos correspondientes
    }
    // Guarda el resultado en la dirección apuntada por 'ip'
    ip[0] = sum;
}

// Función para calcular el producto punto entre dos vectores utilizando C (retorna el valor directamente)
float cFloatInnerProd_v2(float *v1, float *v2, int N)
{
    int i = 0;
    float sum = 0;
    // Calcula el producto punto recorriendo los vectores
    for (i = 0; i < N; i++)
    {
        sum += v1[i] * v2[i];  // Suma los productos de los elementos correspondientes
    }
    return sum;  // Retorna el resultado del producto punto
}

// Función para calcular el error relativo entre dos valores (referencia y calculado)
float calcRelErr(float ref, float cal)
{
    return fabsf(ref - cal) / fabsf(ref);  // Calcula el error relativo como la diferencia absoluta dividida por el valor de referencia
}
