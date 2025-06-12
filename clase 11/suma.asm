    global suma_asm   ; Hacer que la función suma_asm sea accesible desde otros archivos (por ejemplo, C)

    section .text     ; Sección de código, donde se ubican las instrucciones

    ; rdi <- a        ; El primer argumento (a) se pasa en el registro rdi
    ; rsi <- b        ; El segundo argumento (b) se pasa en el registro rsi

suma_asm:
    add rdi, rsi      ; Sumar el valor de rsi (b) a rdi (a), resultado se guarda en rdi
    mov rax, rdi      ; Mover el resultado de la suma (almacenado en rdi) a rax (registro de retorno)
    ret               ; Retornar al llamador, el resultado está en rax
