# Funciones Hudnir la flota
# import /from lo qe se necesite de clases y variables
# mostars instrucciones falta por hacer
import random

# rangos de letras y numeros donde se puede jugar
letras_validas = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
numeros_validos = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
                   
# Definimos pedir las coordenadas para el disparo 
def pedir_coordenadas():
    fila = input("elige una fila (A-J): ").upper() 
    while fila not in letras_validas:
        print("Eso no vale, escribe una letra de la A a la J")
        fila = input("Elige una fila (A-J): ").upper()

    columna = input("Elige una columna (0-9): ")
    while columna not in numeros_validos:
        print("Eso no vale, escribe un numero del 0 al 9")
        columna = input("Elige una columna (0-9): ")

    fila_numero = letras_validas.index(fila)
    columna_numero = int(columna)

    return fila_numero, columna_numero

#Pausa: me corrige la ia ofallos ortograficos

#definamos el disparo de la maquina
def eleigir_disparo_maquina(disparos_hechos):
    fila = random.radiint(0, tablero - 1)  ##necesito saber numeor tablero
    columna = random.radint(0, tablero - 1)

    while (fila, columna) in disparos_hechos:  # comrpobar disparos
        fila = random.radint(0, tablero -1)
        columna = random.radint(0, tablero -1)

    disparos_hechos.append((fila, caloumna)) 
    return fila, columna