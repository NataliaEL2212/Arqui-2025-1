    global arreglo_escalar_asm_float  ; Hacer que la función sea accesible desde otros archivos (como C o Python)

    section .text     ; Define que este código es ejecutable (sección de texto)

    ; rdi <- *arreglo          ; El primer argumento: puntero al arreglo de entrada
    ; xmm0 <- escalar          ; El escalar a multiplicar (se pasa en xmm0)
    ; rsi <- *arreglo_salida   ; El segundo argumento: puntero al arreglo de salida
    ; rdx <- N                 ; El número de elementos (N)

arreglo_escalar_asm_float:
    xor r8, r8                ; Inicializamos el índice (r8 = 0), que será el contador del bucle

lazo:
    movss xmm1, [rdi + 4*r8]  ; Cargar un valor de tipo float desde el arreglo de entrada (arreglo) en xmm1
    mulss xmm1, xmm0          ; Multiplicar el valor cargado (xmm1) por el escalar (xmm0)
    movss [rsi + 4*r8], xmm1  ; Guardar el resultado de la multiplicación en el arreglo de salida (arreglo_salida)

    inc r8                    ; Incrementamos el índice (r8 = r8 + 1) para procesar el siguiente elemento
    cmp r8, rdx               ; Comparamos el índice con el número total de elementos (N)
    jnz lazo                  ; Si no hemos procesado todos los elementos (r8 < N), volvemos al inicio del bucle

    ret                       ; Terminamos la función y retornamos al llamador
