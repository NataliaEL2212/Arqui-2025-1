#include <stdio.h>
#include <stdlib.h>

// Declaración de la función externa en ensamblador para calcular la moda
extern int moda_asm(int *arreglo, int N);

// Declaración de la función en C para calcular la moda
int moda_c(int *arreglo, int N);

int main()
{
    // Arreglo de ejemplo con algunos valores repetidos
    int a[16] = {1, 2, 2, 2, 3, 4, 4, 5, 3, 3, 3, 32, 12, 2, 3};
    int N = 16;  // Tamaño del arreglo
    int modac, modaasm;

    // Calcular la moda usando la versión en C
    modac = moda_c(a, N);

    // Calcular la moda usando la versión en ensamblador
    modaasm = moda_asm(a, N);

    // Imprimir los resultados
    printf("Moda en C: %d \n", modac);
    printf("Moda en ASM: %d \n", modaasm);

    return 0;
}

// Función en C para calcular la moda
int moda_c(int *arreglo, int N)
{
    int cont_max = 0;  // Variable para almacenar el máximo contador de repeticiones
    int cont_int;      // Variable para almacenar el contador de repeticiones de un valor específico
    int moda_value;    // Variable para almacenar el valor de la moda

    // Bucle externo (recorre cada elemento del arreglo)
    for (int i = 0; i < N; i++)
    {
        cont_int = 0;  // Reiniciar el contador de repeticiones para el valor en la posición 'i'

        // Bucle interno (compara el valor de 'arreglo[i]' con todos los demás elementos)
        for (int j = 0; j < N; j++)
        {
            // Si se encuentra una coincidencia, incrementa el contador
            if (arreglo[i] == arreglo[j])
            {
                cont_int = cont_int + 1;
            }
        }

        // Si el contador de repeticiones es mayor que el máximo encontrado, actualiza 'cont_max' y la moda
        if (cont_int > cont_max)
        {
            cont_max = cont_int;  // Actualiza el máximo contador de repeticiones
            moda_value = arreglo[i];  // Actualiza el valor de la moda
        }
    }

    return moda_value;  // Devuelve el valor de la moda
}
