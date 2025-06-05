global asmFloatInnerProd_v2     ; Declaramos la función 'asmFloatInnerProd_v2' como global para que sea accesible desde otras partes del programa
section .text                  ; Sección de código

asmFloatInnerProd_v2:          ; Inicio de la función

    xorpd   xmm0, xmm0        ; Limpia el registro xmm0 (pone a cero) para almacenar el resultado parcial del producto
    xorpd   xmm1, xmm1        ; Limpia el registro xmm1 (pone a cero) para cargar los elementos de los vectores
    xorpd   xmm2, xmm2        ; Limpia el registro xmm2 (pone a cero) para acumular el resultado del producto punto

    cmp     rdx, 0            ; Compara el número de elementos (almacenado en rdx) con 0
    je      done              ; Si no hay elementos (rdx == 0), salta a la etiqueta 'done' para finalizar la función

next:                          ; Bucle principal (iteración sobre cada elemento de los vectores)

    movss   xmm0, [rdi]       ; Carga el valor de la posición 'i' del primer arreglo en xmm0 (arreglo 1)
    movss   xmm1, [rsi]       ; Carga el valor de la posición 'i' del segundo arreglo en xmm1 (arreglo 2)
    mulss   xmm0, xmm1        ; Multiplica los valores en xmm0 (del primer arreglo) y xmm1 (del segundo arreglo), y guarda el resultado en xmm0
    addss   xmm2, xmm0        ; Suma el resultado de la multiplicación (almacenado en xmm0) al acumulador xmm2

    add     rdi, 4            ; Incrementa el puntero 'rdi' para apuntar al siguiente valor en el primer arreglo (4 bytes por 'float')
    add     rsi, 4            ; Incrementa el puntero 'rsi' para apuntar al siguiente valor en el segundo arreglo (4 bytes por 'float')
    sub     rdx, 1            ; Decrementa el número de elementos restantes (almacenado en rdx)
    jnz     next              ; Si rdx no es cero, repite el bucle 'next' para procesar el siguiente par de elementos

done:                          ; Fin del bucle, cuando ya no quedan elementos

    movss   xmm0, xmm2        ; Mueve el valor acumulado (en xmm2) a xmm0 para devolver el resultado final
    ret                         ; Retorna de la función con el valor de la moda (en xmm0)

