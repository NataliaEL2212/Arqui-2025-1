section .data
    entrada      db  "Arquitectura de computadoras",0
    longitud    equ $-entrada

section .bss
    salida   resb  longitud

section .text
    global _start

; rsi:  puntero al elemento actual en entrada
; rdi:  puntero al elemento actual en la salida
; rcx:  puntero a la primera letra de cada palabra
_start:
    mov rsi, entrada
    mov rdi, salida
    mov rcx, entrada
    sub rsi, 1
buscar_espacio:
    add rsi, 1
    mov al, [rsi]
    cmp al, 0       ; la palabra tambien puede terminar en 0
    je  fin_palabra
    cmp al, ' '
    je  fin_palabra
    jmp buscar_espacio

fin_palabra:
    mov rbx, rsi        ; rbx: puntero al espacio en entrada
invertir_palabra:
    dec rsi
    mov r8b, [rsi]      ; r8b: registro extra para leer y escribir a memoria
    mov [rdi], r8b
    inc rdi
    cmp rsi, rcx        ; se verifica si se ha llegado al primer caracter
    jne invertir_palabra

siguiente_palabra:
    cmp al, 0           ; fin de string
    je  fin
    mov byte [rdi], ' '
    inc rdi
    mov rsi, rbx
    inc rsi
    mov rcx, rsi        ; nueva primera letra
    jmp buscar_espacio

fin:
    mov rdi, 0
	mov	rax, 60
	mov	rdi, 0
	syscall
