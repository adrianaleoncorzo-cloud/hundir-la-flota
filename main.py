# Definamos jugar
import numpy as np 
import pandas as pd
from funciones import mostrar_instrucciones

from variables import TAMANO_TABLERO
from clases import Tablero

tablero_jugador = Tablero("Jugador", TAMANO_TABLERO, barcos)  #definir el tablero el cual nostros jugamos
tablero_maquina = Tablero("Maquina", TAMANO_TABLERO, barcos)  # definir tablero maquina

disparos_maquina = []  # para que la maquina no dispare al mismo lugar

# vamos a mostrar los tableros
while True:
    print(tablero_jugador)
    tablero_jugador.mostrar(ocultar_barcos = False)  # mostramos nuestro tablero con los barcos

    print(tablero_maquina)
    tablero_maquina.mostrar(ocultar_barcos = True)   # mostrabmos el tablero sin los barcos del contrario

# Bucle de turno del jugador

print("Tu turno:")
disparo_valido = False
while not dispare_valido:
    fila, col = disparo()
    disparo_valido = tablero_maquina.recibir_disparo(fila, columna)

    if tablero_maquina.comprobar_fin_partido():
        print("\n ¡VICTORIA!")
    break

# Bucle del tunro de la maquina

print("\n Turno de la maquina:")
fila_m, col_m = elegir_disparo_maquina(disparos_maquina)
tablero_jugador.recibir_disparos(fila_m, col_m)

if tablero_jugador.comprobar_fin_partida():
    print("\n ¡HAS PERDIDO!")
break

# Codigo hecho por IA
