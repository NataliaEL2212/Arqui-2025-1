// Declaraciones de las funciones en ensamblador externas
extern void arreglo_escalar_asm_float_simd(float *arreglo, float escalar, float *arreglo_salida, int N); 
extern void arreglo_escalar_asm_float(float *arreglo, float escalar, float *arreglo_salida, int N); 

// Función en C para realizar la multiplicación escalar
void arreglo_escalar_c_float(float *arreglo, float escalar, float *arreglo_salida, int N)
{
    // Itera sobre cada elemento del arreglo y lo multiplica por el escalar
    for (int i = 0; i < N; i++)
    {
        arreglo_salida[i] = arreglo[i] * escalar;  // Multiplica el elemento de arreglo[i] por el escalar
    }
}
