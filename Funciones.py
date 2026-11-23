# Funciones Hudnir la flota
# import /from lo qe se necesite de clases y variables

Instrucciones = (
    "Bienvenido al Hundir la flota. El juego consiste en lo siguiente: \n" 
    "Hay 5 barcos por bando, debes de hundir los barcos del enemigo antes que el hunda los tuyos \n" 
    "E tablero consta de una medida de 10x10 casillas \n" 
    "Cada bando tiene un total de 5 barcos de diferentes medidas: \n" 
        "1 barco de 4 casillas de longitud, 1 de 3 casillas, 1 de 2 casillas y 2 de 1 casilla. \n" 
    "En cada turno se dispara una vez, si fallas, aparecerá AGUA y le toca al siguiente jugador. \n" 
    "Si aciertas, aparecerá TOCADO y seguirás disparando, cuando hundas un barco aparecerá HUNDIDO \n" 
    "Fácil ¿verdad? ¡PUES A JUGAR!")

def mostrar_instrucciones():
    print(Instrucciones)

import random

# rangos de letras y numeros donde se puede jugar
letras_validas = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]  # cambiar por tablero  
numeros_validos = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
                   
# Definimos pedir las coordenadas para el disparo 
def disparo():
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

#Pausa: me corrige la ia los fallos ortograficos

#definamos el disparo de la maquina
def elegir_disparo_maquina(disparos_hechos):
    fila = random.radint(0, tablero - 1)  ##necesito saber numero tablero
    columna = random.radint(0, tablero - 1)

    while (fila, columna) in disparos_hechos:  # comprobar disparos
        fila = random.radint(0, tablero -1)
        columna = random.radint(0, tablero -1)

    disparos_hechos.append((fila, columna)) 
    return fila, columna

