'''LABORATORIO 1 
PREGUNTA 4
NATALIA ESCUDERO LAY 20223377'''

import sys

def calcular_nota_min(arreglo):
    nota_min = 20
    for nota in arreglo:
        if nota < nota_min:
            nota_min = nota
    return nota_min

notas = []

for i in range(1, 6):
    notas.append(int(sys.argv[i]))

nota_min = calcular_nota_min(notas)

promedio = (sum(notas) - nota_min) / 4  
notas.sort()
mediana = notas[2]

print("El promedio de notas es", promedio)
print("La mediana es", mediana)
