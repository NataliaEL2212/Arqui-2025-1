global moda_asm   ; Declaración de la función 'moda_asm' como global, accesible desde otras partes

section .text     ; Sección de código

moda_asm:
    ; Los registros reciben los siguientes valores al principio:
    ; rdi <- dirección del arreglo
    ; rsi <- tamaño del arreglo (N)
    
    xor r8, r8    ; r8 = 0, este registro será utilizado para almacenar el contador máximo (cont_max)
    xor r9, r9    ; r9 = 0, este registro será utilizado para almacenar el contador de ocurrencias (cont_int)
    xor r10, r10  ; r10 = 0, este registro almacenará el valor de la moda (moda_value)
    xor r11, r11  ; r11 = 0, índice 'i' para iterar sobre el arreglo
    xor r13, r13  ; r13 = 0, índice 'j' para comparar con cada elemento
    xor rbx, rbx  ; Limpiamos rbx, que no se usará en este fragmento del código

; Bucle principal (for_i): Recorre todo el arreglo.
for_i:
    xor r9, r9    ; r9 = 0, reiniciamos el contador de ocurrencias (cont_int) para el valor de 'i' actual
    xor r13, r13  ; r13 = 0, reiniciamos el índice 'j' para la comparación con el resto de elementos

; Bucle interno (for_j): Compara el valor en la posición 'i' con todos los valores posteriores.
for_j:
    mov eax, [rdi + 4 * r11]   ; Carga el valor de la posición 'i' del arreglo en eax (arreglo[i])
    mov ebx, [rdi + 4 * r13]   ; Carga el valor de la posición 'j' del arreglo en ebx (arreglo[j])
    cmp eax, ebx               ; Compara el valor de 'arreglo[i]' con 'arreglo[j]'
    je update_cont_int         ; Si son iguales, significa que hay una coincidencia, y se incrementa el contador de ocurrencias (cont_int)
    
go_j:
    inc r13                    ; Incrementa 'j' para comparar con el siguiente elemento
    cmp r13, rsi               ; Si 'j' ha alcanzado el tamaño del arreglo, termina el bucle 'for_j'
    jne for_j                  ; Si 'j' < N, sigue el bucle 'for_j'

; Después de comparar todos los elementos con 'arreglo[i]', verificamos si el contador de ocurrencias (cont_int) es mayor que el contador máximo (cont_max)
    cmp r9, r8                 ; Si cont_int (r9) > cont_max (r8), actualizamos la moda
    jg update_cont_max         ; Si es mayor, vamos a actualizar el contador máximo y el valor de la moda
    
go_i:
    inc r11                    ; Incrementa 'i' para comprobar el siguiente valor del arreglo
    cmp r11, rsi               ; Si 'i' ha alcanzado el tamaño del arreglo, termina el bucle 'for_i'
    jne for_i                  ; Si 'i' < N, sigue el bucle 'for_i'

salida:
    mov eax, r10d              ; Coloca el valor de la moda (almacenado en r10) en eax
    ret                         ; Retorna el valor de la moda (en eax)

; Si encontramos una coincidencia entre 'arreglo[i]' y 'arreglo[j]', incrementamos el contador de ocurrencias (cont_int)
update_cont_int:
    inc r9                     ; Incrementa cont_int (r9) ya que se encontró una coincidencia
    jmp go_j                   ; Vuelve a comparar con el siguiente valor de 'j'

; Si se encontró un nuevo máximo para el contador de ocurrencias, actualizamos el contador máximo (cont_max) y la moda
update_cont_max:
    mov r8, r9                 ; Actualiza cont_max con el valor actual de cont_int (r9)
    mov r10d, eax              ; Actualiza la moda con el valor de 'arreglo[i]' que se encuentra en eax
    jmp go_i                   ; Continúa al siguiente valor de 'i'
