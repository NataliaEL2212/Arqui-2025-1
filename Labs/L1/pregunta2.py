'''LABORATORIO 1 
PREGUNTA 2
NATALIA ESCUDERO LAY 20223377'''

import sys

def calcula_cant_multiplos(numero, lim_inf, lim_sup):
    cant_multiplos = 0
    for i in range(lim_inf, lim_sup+1):
        if(i % numero == 0):
            cant_multiplos = cant_multiplos + 1
    return cant_multiplos

numero = int(sys.argv[1])
lim_inf = int(sys.argv[2])
lim_sup = int(sys.argv[3])
cant_multiplos = calcula_cant_multiplos(numero, lim_inf, lim_sup)

print("Hay ", cant_multiplos, " múltiplos de ", numero, "en este rango\r\n")
