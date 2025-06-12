// Declaración de la función en ensamblador que suma dos números de tipo unsigned long long
extern unsigned long long suma_asm(unsigned long long a, unsigned long long b);

// Función en C que suma dos números de tipo unsigned long long
unsigned long long suma(unsigned long long a, unsigned long long b)
{
    return a + b;  // Realiza la suma de los dos números y devuelve el resultado
}

// Función que realiza una operación con un número de tipo double
double operacion(double x)
{
    return 3.5 * x;  // Multiplica el número x por 3.5 y devuelve el resultado
}
