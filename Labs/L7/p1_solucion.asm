section .data
    arreglo dd 12, -3, 7, 22, 45, 63, 78, 91, 24, 33  ; Definición del arreglo de 10 enteros
    N equ 10                                          ; Tamaño del arreglo (N = 10)
    mediana dd 0                                      ; Espacio reservado para almacenar la mediana

section .text
    global _start                                      ; Definir el punto de inicio del programa

; ecx:  contador externo
_start:
    mov ecx, N                                          ; Carga el valor de N (10) en ecx
    dec ecx                                              ; Decrementa ecx para que sea N - 1 (la última posición del arreglo)

; edx:  contador interno
; esi:  puntero al elemento i del arreglo
bucle_externo:                                         ; Bucle externo (para hacer varias pasadas del algoritmo de ordenación)
    mov edx, ecx                                        ; Copia el valor de ecx en edx (contador para el bucle interno)
    mov esi, arreglo                                    ; Carga la dirección del arreglo en esi

; eax: elemento i-ésimo
; ebx: elemento i+1
bucle_interno:                                          ; Bucle interno (compara y cambia los elementos del arreglo)
    mov eax, [esi]                                      ; Carga el valor del arreglo[i] en eax
    mov ebx, [esi+4]                                    ; Carga el valor del arreglo[i+1] en ebx
    cmp eax, ebx                                        ; Compara el valor de arreglo[i] con arreglo[i+1]
    jle siguiente                                        ; Si arreglo[i] <= arreglo[i+1], salta a 'siguiente'
    
    ; Alternar elementos si están desordenados
    mov [esi], ebx                                      ; Guarda el valor de arreglo[i+1] en arreglo[i]
    mov [esi+4], eax                                    ; Guarda el valor de arreglo[i] en arreglo[i+1]

siguiente:
    add esi, 4                                          ; Incrementa el puntero 'esi' para pasar al siguiente elemento (4 bytes por entero)
    dec edx                                              ; Decrementa el contador interno
    jnz bucle_interno                                    ; Si el contador interno (edx) no es cero, sigue en el bucle interno
    
    loop bucle_externo                                   ; Decrementa ecx y repite el bucle externo si ecx != 0

; Aquí comienza el cálculo de la mediana
calc_mediana:
    mov eax, N                                          ; Carga el tamaño del arreglo (N) en eax
    mov edx, 0                                          ; Limpia el registro edx
    mov ebx, 2                                          ; Carga el valor 2 en ebx (para calcular N / 2)
    div ebx                                              ; Realiza N / 2 y guarda el resultado en eax (cociente) y N % 2 en edx
    cmp edx, 0                                           ; Compara el residuo con 0 (verificar si N es par o impar)
    jne impar                                            ; Si el residuo es distinto de cero, N es impar, salta a la etiqueta 'impar'

    ; Caso cuando N es par (se calcula la media entre los dos valores centrales)
    mov esi, arreglo                                    ; Carga la dirección base del arreglo en esi
    mov ecx, eax                                        ; Guarda el valor de N / 2 en ecx
    dec ecx                                              ; Decrementa en 1 para obtener el índice del primer elemento central (N/2 - 1)

    mov eax, [esi + ecx*4]                              ; Carga el valor central menor (arreglo[N/2 - 1])
    add eax, [esi + (ecx+1)*4]                          ; Suma el valor central mayor (arreglo[N/2])
    
    ; Otra forma de dividir entre 2: desplazamiento aritmético a la derecha (sar)
    sar eax, 1                                           ; Realiza un desplazamiento aritmético a la derecha (eax / 2)
    jmp guardar_resultado                               ; Salta a la etiqueta 'guardar_resultado' para guardar el resultado

impar:
    ; Caso cuando N es impar (se toma directamente el valor central)
    mov esi, arreglo                                    ; Carga la dirección base del arreglo en esi
    mov eax, [esi + eax*4]                              ; Carga el valor central (arreglo[N/2])

guardar_resultado:
    mov [mediana], eax                                  ; Guarda el valor de la mediana en la variable 'mediana'

fin:
    mov rax, 60                                         ; Código de salida del sistema (sys_exit)
    mov rdi, 0                                          ; Código de salida (0 indica que el programa terminó sin errores)
    syscall                                              ; Realiza la llamada al sistema para terminar el programa
