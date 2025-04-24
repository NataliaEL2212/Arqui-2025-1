#Programa para calcular el promedio del curso de Arquitectura de Computadoras

'''
if __name__ == "__main__":
    notas_nombres = [f"lab {idx + 1}" for idx in range (12)]
    notas_nombres.append("examen 1")
    notas_nombres.append("examen 2")
    notas = list()

    for nombre in notas_nombres:
        nota = input(f"Por favor ingrese la nota de {nombre}: ")
        nota = int(nota)
        notas.append(nota)

    print(f"Notas: {notas}")

    notas_labs = notas[:12] #todas las notas de laboratorio
    e1 = notas[12]
    e2 = notas[13]

    lab = sum(notas_labs) / len(notas_labs)

    nota_final = (5 * lab + 2 * e1 + 2 * e2) / 10

    print(f"Nota final: {nota_final}")
'''

#Ahora utilizando la libreria time para contar el tiempo

'''
import time

if __name__ == "__main__":
    inicio = time.perf_counter()
    notas_nombres = [f"lab {idx + 1}" for idx in range (12)]
    notas_nombres.append("examen 1")
    notas_nombres.append("examen 2")
    notas = list()

    for nombre in notas_nombres:
        nota = input(f"Por favor ingrese la nota de {nombre}: ")
        nota = int(nota)
        notas.append(nota)

    print(f"Notas: {notas}")

    notas_labs = notas[:12] #todas las notas de laboratorio
    e1 = notas[12]
    e2 = notas[13]

    lab = sum(notas_labs) / len(notas_labs)

    nota_final = (5 * lab + 2 * e1 + 2 * e2) / 10

    fin = time.perf_counter()

    t_ejecucion = fin - inicio

    print(f"Nota final: {nota_final}")
    print(f"Tiempo de ejecucion: {t_ejecucion}") #ponemos los prints despues del t_ejecucion porque no tienen impacto real en el programa
'''

    #Los inputs son factores externos que no permiten monitorear por completo el desarrollo del programa, ya que depende de la velocidad del usuario
    #Para determinar el tiempo del programa, ponemos la entrada del inicio despues de ingresa

'''
import time

if __name__ == "__main__":
    inicio = time.perf_counter()
    notas_nombres = [f"lab {idx + 1}" for idx in range (12)]
    notas_nombres.append("examen 1")
    notas_nombres.append("examen 2")
    notas = list()

    for nombre in notas_nombres:
        nota = input(f"Por favor ingrese la nota de {nombre}: ")
        nota = int(nota)
        notas.append(nota)

    print(f"Notas: {notas}")

    inicio_cpu = time.perf_counter()

    notas_labs = notas[:12] #todas las notas de laboratorio
    e1 = notas[12]
    e2 = notas[13]

    lab = sum(notas_labs) / len(notas_labs)

    nota_final = (5 * lab + 2 * e1 + 2 * e2) / 10

    fin = time.perf_counter()

    t_ejecucion = fin - inicio
    t_cpu = fin - inicio_cpu

    print(f"Nota final: {nota_final}")
    print(f"Tiempo de ejecucion de cpu: {t_cpu} segundos y de la ejecucion: {t_ejecucion}") #ponemos los prints despues del t_ejecucion porque no tienen impacto real en el programa
'''

    #Tiempo de ejecucion de cpu: 1.3749000117968535e-05 segundos y de la ejecucion: 6.90231781500006
    #Ante estos resultados, podemos saber que el tiempo del cpu es muy corto a comparacion del tiempo total de ejecucion
    #De todas maneras, cada time.perf_counter() aumenta el tiempo de ejecución del programa. La mayoria de profilers tienen este problema, aunque el tiempo puede ser despreciable, igual es importante tomarlo en cuenta
