global convolucionar_vector_asm_float
    section .text
    ;rdi <- *xn
    ;rsi <- *hk
    ;rdx <- *yn
    ;rcx <- N
    ;r8  <- K
convolucionar_vector_asm_float:
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
    movss xmm0, [rdi+4*r9]            
    subss xmm0, [4*r10]               ;x(n-k)
    movss xmm1, [rsi+4*r10]           ;h(k)
    movss xmm2, [rdx+4*r9]            ;y(n) anterior
    mulss xmm1, xmm0
    addss xmm3,	xmm1                  ;se suma x(n-k)*h(k)
    addss xmm3,	xmm2                  ;se suma el yn anterior
    movss [rdx+4*r9],xmm3             ;guardamos yn
    inc r10                           ;aumenta k
    jmp confirmar_k
for_n:
    xor r10,r10                       ;reiniciamos el contador k 
    inc r9
    cmp r9, rcx                       ;revisamos si n llego a su limite
    jne confirmar_k 
    ret