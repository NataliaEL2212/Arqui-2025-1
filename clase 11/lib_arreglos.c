extern void arreglo_escalar_asm(unsigned long long *arreglo, unsigned long long escalar, unsigned long long *arreglo_salida, int N);

void arreglo_escalar_c(unsigned long long *arreglo, unsigned long long escalar, unsigned long long *arreglo_salida, int N)
{
    // Función que realiza la multiplicación de cada elemento del arreglo por un escalar
    for (int i = 0; i < N; i++)  // Itera a través de todos los elementos del arreglo
    {
        arreglo_salida[i] = arreglo[i] * escalar;  // Multiplica cada elemento por el escalar y guarda el resultado
    }
}

int main()
{
    // Definición de los arreglos de entrada y salida
    unsigned long long arreglo[5] = {10, 20, 30, 40, 50};  // Arreglo de entrada
    unsigned long long arreglosalida[5] = {0, 0, 0, 0, 0};  // Arreglo de salida (inicializado en cero)

    // Llamada a la función en ensamblador que multiplica los elementos del arreglo por el escalar
    arreglo_escalar_asm(arreglo, 10, arreglosalida, 5);  // Multiplica cada elemento del arreglo por 10 y guarda el resultado en arreglosalida

    return 0;  // Termina la ejecución del programa
}
