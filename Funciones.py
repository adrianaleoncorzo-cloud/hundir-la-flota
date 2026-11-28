# Funciones de Hundir la flota

import random

from variables import TAMANO_TABLERO


Instrucciones = (
    "Bienvenido al Hundir la flota. El juego consiste en lo siguiente:\n"
    "Hay 5 barcos por bando, debes hundir los barcos del enemigo antes de que "
    "hunda los tuyos.\n"
    f"El tablero consta de {TAMANO_TABLERO}x{TAMANO_TABLERO} casillas.\n"
    "Cada bando tiene 5 barcos de diferentes medidas:\n"
    "1 barco de 4 casillas, 1 de 3 casillas, 1 de 2 casillas y 2 de 1 casilla.\n"
    "En cada turno se dispara una vez. Si fallas, aparecerá AGUA y cambia el turno.\n"
    "Si aciertas, aparecerá TOCADO y seguirás disparando. Cuando hundas un barco, "
    "aparecerá HUNDIDO.\n"
    "Fácil, ¿verdad? ¡PUES A JUGAR!")

def mostrar_instrucciones():
    print(Instrucciones)

# rangos de letras y numeros donde se puede jugar
letras_validas = [chr(ord("A") + indice) for indice in range(TAMANO_TABLERO)]
numeros_validos = [str(numero) for numero in range(TAMANO_TABLERO)]
                   
# Definimos pedir las coordenadas para el disparo 
def disparo():
    fila = input("Elige una fila (A-J): ").strip().upper()
    while fila not in letras_validas:
        print("Eso no vale, escribe una letra de la A a la J")
        fila = input("Elige una fila (A-J): ").strip().upper()

    columna = input("Elige una columna (0-9): ").strip()
    while columna not in numeros_validos:
        print("Eso no vale, escribe un numero del 0 al 9")
        columna = input("Elige una columna (0-9): ").strip()

    fila_numero = letras_validas.index(fila)
    columna_numero = int(columna)

    return fila_numero, columna_numero

# Definimos el disparo de la maquina
def elegir_disparo_maquina(disparos_hechos):
    disparos_realizados = set(disparos_hechos)

    if len(disparos_realizados) >= TAMANO_TABLERO * TAMANO_TABLERO:
        raise RuntimeError("No quedan casillas disponibles para disparar")

    fila = random.randint(0, TAMANO_TABLERO - 1)
    columna = random.randint(0, TAMANO_TABLERO - 1)

    while (fila, columna) in disparos_realizados:
        fila = random.randint(0, TAMANO_TABLERO - 1)
        columna = random.randint(0, TAMANO_TABLERO - 1)

    disparos_hechos.append((fila, columna))
    return fila, columna

