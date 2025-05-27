section .data
    datos dw 10,10,10,20,30,30,30,30,30,40,10,10,20,10
    datos2 dw 10,20,30,40
section .bss
    histograma resw 4
section .text
    global_start

_start:
    mov rax, 14
    mov rdx, 0

lazo:
    mov bx, [datos+4*rdx]
    mov cx, [datos2]
    cmp bx, cx
    je salta1
    mov cx, [datos2+2]
    cmp bx, cx
    je salta2
    mov cx, [datos2+4]
    cmp bx, cx
    je salta3
    mov cx, [datos2+6]
    cmp bx, cx
    je salta4
vuelve1:
    inc rdx
    cmp rdx,rax
    jne lazo
    je _exit

salta1:
    mov r8, [histograma]
    inc r8
    mov [histograma], r8
    je vuelve1
salta2:
    mov r8, [histograma+2]
    inc r8
    mov [histograma+2], r8
    je vuelve1
salta3:
    mov r8, [histograma+4]
    inc r8
    mov [histograma+4], r8
    je vuelve1
salta4:
    mov r8, [histograma+6]
    inc r8
    mov [histograma+6], r8
    je vuelve1

exit:
    mov rax, 60
    mov rdi, 0
    syscall

