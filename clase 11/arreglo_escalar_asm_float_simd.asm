    global arreglo_escalar_asm_float_simd  ; Hacer que la función sea accesible desde otros archivos (como C o Python)

    section .text     ; Define que este código es ejecutable (sección de texto)

    ; rdi <- *arreglo          ; El primer argumento: puntero al arreglo de entrada
    ; xmm0 <- escalar          ; El escalar a multiplicar (se pasa en xmm0)
    ; rsi <- *arreglo_salida   ; El segundo argumento: puntero al arreglo de salida
    ; rdx <- N                 ; El número de elementos (N)

arreglo_escalar_asm_float_simd:
    xor r8, r8                ; Inicializamos el índice (r8 = 0)
    mov rax, 4                ; Inicializamos rax con 4 (procesamos 4 elementos a la vez, ya que usamos xmm0, que puede contener 4 floats)
    shufps xmm0, xmm0, 00000000b  ; Aseguramos que el escalar (en xmm0) esté en la posición correcta para multiplicar con los floats (lo mueve a todos los elementos de xmm0)

lazo:
    movaps xmm1, [rdi]        ; Cargar 4 elementos de tipo float desde el arreglo de entrada (arreglo) en xmm1
    mulps xmm1, xmm0          ; Multiplicar cada uno de los 4 elementos en xmm1 por el escalar (en xmm0)
    movaps [rsi], xmm1        ; Guardar los resultados en el arreglo de salida (arreglo_salida)
    
    add rdi, 16               ; Avanzamos el puntero al arreglo de entrada 16 bytes (4 floats de 4 bytes)
    add rsi, 16               ; Avanzamos el puntero al arreglo de salida 16 bytes (4 floats de 4 bytes)
    
    inc r8                    ; Incrementamos el índice (r8 = r8 + 1)
    mul r8                    ; Multiplicamos r8 por sí mismo (esto parece un error de código y no tiene sentido en este contexto)
    
    cmp rax, rdx              ; Comparamos el índice con el número total de elementos (N)
    jnz lazo                  ; Si no hemos procesado todos los elementos (r8 < N), volvemos al inicio del bucle

    ret                       ; Retorno de la función
