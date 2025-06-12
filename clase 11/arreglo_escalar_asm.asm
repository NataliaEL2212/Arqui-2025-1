    global arreglo_escalar_asm
    section .text

    ; rdi <- *arreglo      ; Dirección base del arreglo de entrada
    ; rsi <- escalar       ; Valor escalar con el que multiplicar cada elemento del arreglo
    ; rdx <- *arreglo_salida ; Dirección base del arreglo de salida
    ; rcx <- N             ; Número de elementos en el arreglo

arreglo_escalar_asm:
    xor r8, r8            ; Inicializar el índice (r8 = 0)
    mov r10, rcx          ; Guardar N (número de elementos) en r10
    mov r12, rdx          ; Guardar la dirección de salida en r12

lazo:
    mov rax, [rdi + 8 * r8] ; Cargar el elemento del arreglo en rax (8 * r8 para acceso de 64 bits)
    mul rsi                ; Multiplicar el valor del arreglo por el escalar (rax = rax * rsi)
    mov [r12 + 8 * r8], rax ; Almacenar el resultado en el arreglo de salida
    inc r8                 ; Incrementar el índice (r8 = r8 + 1)
    cmp r8, r10            ; Comparar el índice con N
    jnz lazo               ; Si el índice no es igual a N, saltar al inicio del bucle

    ret                    ; Retornar al llamador
