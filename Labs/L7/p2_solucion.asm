section .data
    entrada      db  "Arquitectura de computadoras",0  ; Definición de la cadena de texto de entrada
    longitud     equ $ - entrada                        ; Calcula la longitud de la cadena

section .bss
    salida   resb longitud  ; Reserva espacio para la cadena de salida, con la misma longitud que la entrada

section .text
    global _start           ; Define el punto de entrada del programa (para sistemas Linux)

; rsi: puntero al elemento actual en la entrada
; rdi: puntero al elemento actual en la salida
; rcx: puntero a la primera letra de cada palabra
_start:
    mov rsi, entrada          ; rsi apunta al inicio de la cadena de entrada
    mov rdi, salida           ; rdi apunta al inicio de la cadena de salida
    mov rcx, entrada          ; rcx guarda el puntero al inicio de la cadena de entrada
    sub rsi, 1                ; Decrementa rsi en 1 para apuntar al primer caracter de la cadena

buscar_espacio:
    add rsi, 1                ; Incrementa rsi para mover al siguiente carácter de la cadena
    mov al, [rsi]             ; Carga el byte apuntado por rsi (carácter actual) en al
    cmp al, 0                 ; Compara si hemos llegado al final de la cadena (carácter nulo)
    je  fin_palabra           ; Si es 0 (fin de la cadena), salta a fin_palabra
    cmp al, ' '               ; Compara si el carácter actual es un espacio
    je  fin_palabra           ; Si es un espacio, salta a fin_palabra
    jmp buscar_espacio        ; Si no es un espacio ni fin de cadena, sigue buscando un espacio

fin_palabra:
    mov rbx, rsi              ; Guarda el puntero al espacio (fin de la palabra actual) en rbx

invertir_palabra:
    dec rsi                    ; Decrementa rsi para apuntar al carácter anterior (de la palabra)
    mov r8b, [rsi]             ; Carga el carácter en r8b
    mov [rdi], r8b            ; Copia el carácter a la posición actual de la salida
    inc rdi                    ; Incrementa rdi para avanzar en la cadena de salida
    cmp rsi, rcx               ; Compara si rsi ha llegado al principio de la palabra
    jne invertir_palabra       ; Si no es el inicio de la palabra, sigue invirtiendo

siguiente_palabra:
    cmp al, 0                  ; Compara si hemos llegado al final de la cadena (fin del texto)
    je  fin                    ; Si es el fin de la cadena, salta a fin
    mov byte [rdi], ' '        ; Si no hemos llegado al fin de la cadena, agrega un espacio a la salida
    inc rdi                    ; Incrementa el puntero de salida
    mov rsi, rbx               ; Restaura rsi al puntero del inicio de la siguiente palabra
    inc rsi                    ; Avanza el puntero rsi para saltar el espacio
    mov rcx, rsi               ; Actualiza rcx para que apunte al primer carácter de la siguiente palabra
    jmp buscar_espacio         ; Vuelve a buscar el siguiente espacio para continuar con la siguiente palabra

fin:
    mov rdi, 0                 ; Prepara rdi para terminar el programa
    mov rax, 60                ; Código de salida del sistema (sys_exit)
    mov rdi, 0                 ; Código de salida (0 = sin errores)
    syscall                    ; Llama a la syscall para salir del programa
