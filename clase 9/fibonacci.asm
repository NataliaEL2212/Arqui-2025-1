section .data
    label1 dd 0,1 ;valores iniciales
    label2 dd 0
    termino db 12 ;contador
 
section .bss
    label3 resd 1 ;se guarda en la ram

section .text
    global_start

_start:
    mov al, [termino]
    mov bl, 2
    div bl ;residuo en ah

mem:    
    mov r8d, [label1] ;obtenemos el valor de la ram
    mov r10d, [label1 + 4] ;como dd es de 4B, nos movemos al registro inicial del siguiente valor

lazo:
    add r8d, r10d ;el resultado se suma en eax
    add r10d, r8d

    dec al
    cmp al,0 ;cmp es para comparar, dl tiene el valor actual y estara comparando
    jne lazo ;salta el lazo si no es igual "jump no equal" lazo se ejecuta hasta que sea igual

    cmp ah,0
    jne impar2

par2:
    mov [label3], r8d ;primer termino

impar2:
    mov [label3], r10d ;segundo termino

exit:
    mov rax, 60
    mov rdi, 0
    syscall