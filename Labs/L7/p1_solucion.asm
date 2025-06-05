section .data
    arreglo dd 12, -3, 7, 22, 45, 63, 78, 91, 24, 33
    N equ 10
    mediana dd 0

section .text
    global _start

; ecx:  contador externo
_start:
    mov ecx, N
    dec ecx                     

; edx:  contador interno
; esi:  puntero al elemento i del arreglo
bucle_externo:
    mov edx, ecx
    mov esi, arreglo

; eax: elemento i-esimo
; ebx: elemento i+1
bucle_interno:
    mov eax, [esi]             
    mov ebx, [esi+4]           
    cmp eax, ebx
    jle siguiente
    
    ; Alternar elementos
    mov [esi], ebx
    mov [esi+4], eax

siguiente:
    add esi, 4                  
    dec edx
    jnz bucle_interno              
    
    loop bucle_externo

; Se usa la instruccion DIV para verificar si N es par o impar y 
; para hallar el elemento central
calc_mediana:
    mov eax, N
    mov edx, 0
    mov ebx, 2
    div ebx         ; eax: N/2, edx: N%2
    cmp edx, 0 
    jne impar             

    ; Caso par
    mov esi, arreglo
    mov ecx, eax                ; N/2
    dec ecx                     ; N/2 - 1
    
    mov eax, [esi + ecx*4]      ; Elemento central menor
    add eax, [esi + (ecx+1)*4]  ; Elemento central mayor
    
    ; Otra forma de dividir entre 2: Aritmethic Shift Right (eax<<1)
    sar eax, 1
    jmp guardar_resultado

impar:
    ; Solo toma el elemento central
    mov esi, arreglo
    mov eax, [esi + eax*4]      

guardar_resultado:
    mov [mediana], eax

fin:
	mov	rax, 60
	mov	rdi, 0
	syscall
