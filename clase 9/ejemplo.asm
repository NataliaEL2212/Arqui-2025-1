section .data
    label1 db 10,14
    label2 dw 300,1000
    label3 dq 5000,6500

section .text

global_start

_start:
    mov al, [label1]
    mov ah, [label1+1]

    mov rdx, [label3]
    mov rcx, [label3+8]

    mov rax, 60
    mov rdi, 0
    syscall