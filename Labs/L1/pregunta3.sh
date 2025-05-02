#LABORATORIO 1 
#PREGUNTA 2
#NATALIA ESCUDERO LAY 20223377

#/avr/main/bash

mkdir Carpeta_C
chmod 777 Carpeta_C
mkdir Carpeta_Python
chmod 777 Carpeta_Python
cp pregunta1.c Carpeta_C
cp pregunta2.py Carpeta_Python
./pregunta1 2025 1 $1
python3 pregunta2.py 2025 1 $1