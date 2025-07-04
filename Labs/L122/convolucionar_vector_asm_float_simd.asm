global convolucionar_vector_asm_float_simd
    section .text
    ;rdi <- *xn
    ;rsi <- *hk
    ;rdx <- *yn
    ;rcx <- N
    ;r8  <- K
convolucionar_vector_asm_float_simd:
    xor r9,r9         ; nuestro contador n
    xor r10,r10       ; nuestro contador k 
    xorpd xmm2, xmm2  ; el valor yn anterior
    xorpd xmm3, xmm3  ; el valor yn actual  
confirmar_k:
    cmp r8, r10      ;revisamos si k llego a su limite
    je for_n
    cmp r9,r10       ;si n-k esta fuera del rango
    jge for_k        ;si esta en el rango procede a calcular yn
    inc r10          ;aumenta k
    jmp confirmar_k
for_k:
    xorpd xmm3, xmm3                  ;reiniciamos el valor yn actual
    movaps xmm0, [rdi]                ;x(n-k)
    movaps xmm1, [rsi]                ;h(k)
    movaps xmm2, [rdx]                ;y(n) anterior
    mulps xmm1, xmm0
    addps xmm3,	xmm1                  ;se suma x(n-k)*h(k)
    addps xmm3,	xmm2                  ;se suma el yn anterior
    movaps [rdx],xmm3                 ;guardamos yn
    inc r10                           ;aumenta k
    sub rdi, 16                       ;se desplaza al siguiente valor de x(n) (disminuyendo porque k se resta)
    add rsi, 16                       ;se desplaza al siguiente valor de h(k)
    jmp confirmar_k
for_n:
    xor r10,r10                       ;reiniciamos el contador k 
    mov rsi, 0                        ;volvemos al valor inicial de h(k)
    inc r9
    add rdx, 16                       ;nos movemos al siguiente valor de y(n)
    add rdi, 16                       ;nos movemos al siguiente valor de x(n)
    cmp r9, rcx                       ;revisamos si n llego a su limite
    jne confirmar_k 
    ret