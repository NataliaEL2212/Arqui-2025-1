global asmFloatInnerProd      ; Declaramos el nombre de la función global
section .text                 ; Sección de código (por lo general para instrucciones)

asmFloatInnerProd:            ; Nombre de la función

    ; Inicializamos los registros xmm0, xmm1, y xmm2 a cero.
    xorpd   xmm0, xmm0        ; Limpia el registro xmm0 (lo pone a cero)
    xorpd   xmm1, xmm1        ; Limpia el registro xmm1 (lo pone a cero)
    xorpd   xmm2, xmm2        ; Limpia el registro xmm2 (lo pone a cero)

    cmp     rdx, 0            ; Compara el número de elementos (almacenado en rdx) con 0
    je      done              ; Si el número de elementos es 0, salta a la etiqueta 'done'

next:                          ; Comienza el bucle de procesamiento de cada par de elementos

    movss   xmm0, [rdi]       ; Carga el valor de la dirección de memoria apuntada por 'rdi' (primer arreglo) en xmm0
    movss   xmm1, [rsi]       ; Carga el valor de la dirección de memoria apuntada por 'rsi' (segundo arreglo) en xmm1
    mulss   xmm0, xmm1        ; Multiplica el valor de xmm0 (del primer arreglo) por el valor de xmm1 (del segundo arreglo) y guarda el resultado en xmm0
    addss   xmm2, xmm0        ; Suma el resultado (almacenado en xmm0) a la acumulación que está en xmm2

    add     rdi, 4            ; Incrementa el puntero 'rdi' en 4 (apunta al siguiente valor del primer arreglo)
    add     rsi, 4            ; Incrementa el puntero 'rsi' en 4 (apunta al siguiente valor del segundo arreglo)
    sub     rdx, 1            ; Decrementa el contador de elementos (almacenado en rdx)
    jnz     next              ; Si rdx no es cero, salta al inicio de 'next' para procesar el siguiente par de elementos

done:                          ; Aquí termina el bucle y la función

    movss   [rcx], xmm2       ; Almacena el resultado acumulado (almacenado en xmm2) en la dirección de memoria apuntada por 'rcx'
    ret                        ; Retorna de la función
