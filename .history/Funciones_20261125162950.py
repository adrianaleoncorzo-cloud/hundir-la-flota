# Funciones Hudnir la flota
from clases import Tablero
from variables import TAMANO_TABLERO, barcos
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
tablero_jugador = Tablero("Jugador", TAMANO_TABLERO, barcos)  #definir el tablero el cual nostros jugamos
tablero_maquina = Tablero("Maquina", TAMANO_TABLERO, barcos)  # definir tablero maquina
# rangos de letras y numeros donde se puede jugar
letras_validas = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]  # cambiar por tablero  
numeros_validos = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
                   
# Definimos pedir las coordenadas para el disparo 
def disparo():
    columna = input("Elige una letra (A-J): ").strip().upper() 
    while columna not in letras_validas:
        print("Eso no vale, escribe una letra de la A a la J")
        columna = input("Elige una letra (A-J): ").strip().upper()

    fila = input("Elige un numero (1-10): ").strip()
    while fila not in numeros_validos:
        print("Eso no vale, escribe un numero del 1 al 10")
        fila = input("Elige una numero (1-10): ").strip()

    fila_numero = letras_validas.index(columna)
    columna_numero = int(fila) - 1

    return columna_numero, fila_numero

#Pausa: me corrige la ia los fallos ortograficos

#definamos el disparo de la maquina
def disparo_maquina(disparos_hechos):
    fila = random.randint(0, tablero_jugador.dimensiones - 1)  ##necesito saber numero tablero
    columna = random.randint(0, tablero_jugador.dimensiones - 1)

    while (fila, columna) in disparos_hechos:  # comprobar disparos
        fila = random.randint(0, tablero_jugador.dimensiones -1)
        columna = random.randint(0, tablero_jugador.dimensiones -1)

    disparos_hechos.append((fila, columna)) 
    return fila, columna

