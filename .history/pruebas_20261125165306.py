from clases import Tablero
from variables import TAMANO_TABLERO, barcos
from Funciones import mostrar_instrucciones, disparo, disparo_maquina


# 2. Mostrar las instrucciones del juego
mostrar_instrucciones()


# 3. Crear los tableros de ambos participantes
tablero_jugador = Tablero("Jugador", TAMANO_TABLERO, barcos)
tablero_maquina = Tablero("Maquina", TAMANO_TABLERO, barcos)


# 4. Colocar los barcos aleatoriamente
tablero_jugador.colocar_barcos_aleatorios()
tablero_maquina.colocar_barcos_aleatorios()


# 5. Inicializar el registro de disparos de la máquina
disparos_maquina = []
