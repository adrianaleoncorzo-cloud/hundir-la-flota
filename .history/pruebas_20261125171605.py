
# Definimos jugar

from variables import barcos, TAMANO_TABLERO
from clases import Tablero
from funciones import disparo, disparo_maquina, mostrar_instrucciones


# Mostrar instrucciones
mostrar_instrucciones()


# Crear los tableros
tablero_jugador = Tablero("Jugador", TAMANO_TABLERO, barcos)
tablero_maquina = Tablero("Maquina", TAMANO_TABLERO, barcos)

# Colocar los barcos aleatoriamente
tablero_jugador.colocar_barcos_aleatorios()
tablero_maquina.colocar_barcos_aleatorios()

# Registrar los disparos de la máquina
disparos_maquina = []


# Bucle principal del juego
while True:

    # Mostrar los tableros
    print("\nTu tablero:")
    tablero_jugador.mostrar(ocultar_barcos=False)

    print("\nTablero de la máquina:")
    tablero_maquina.mostrar(ocultar_barcos=True)


    # Bucle de turno del jugador

    print("\nTu turno:")

    disparo_valido = False

    while not disparo_valido:
        fila, col = disparo()
        resultado = tablero_maquina.recibir_disparo(fila, col)

        if resultado != False:
            disparo_valido = True

    if tablero_maquina.comprobar_fin_partida():
        print("\n¡VICTORIA!")
        break


    # Bucle de turno de la máquina

    print("\nTurno de la máquina:")

    fila_m, col_m = disparo_maquina(disparos_maquina)

    tablero_jugador.recibir_disparo(fila_m, col_m)

    if tablero_jugador.comprobar_fin_partida():
        print("\n¡HAS PERDIDO!")
        break
