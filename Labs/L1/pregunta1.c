//LABORATORIO 1 Nota 20
//PREGUNTA 1 
//NATALIA ESCUDERO LAY 20223377

#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int calcula_cant_multiplos(int numero, int lim_inf, int lim_sup){
    int cant_multiplos = 0;
    for(int i=lim_inf; i<lim_sup+1; i++){
        if(i%numero == 0){
            cant_multiplos++;
        }
    }
    return cant_multiplos;
}

int main(int argc, char *argv[]){
    int numero = atoi(argv[1]);
    int lim_inf = atoi(argv[2]);
    int lim_sup = atoi(argv[3]);
    int cant_multiplos = calcula_cant_multiplos(numero, lim_inf, lim_sup);
    printf("Hay %d múltiplos de %d en este rango\r\n", cant_multiplos, numero);
    return 1;
}
