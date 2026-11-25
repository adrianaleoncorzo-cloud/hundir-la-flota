# Definimos jugar

from variables import barcos, TAMANO_TABLERO
from clases import Tablero
from funciones import disparo, disparo_maquina, mostrar_instrucciones

mostrar_instrucciones()

tablero_jugador = Tablero("Jugador", TAMANO_TABLERO, barcos)
tablero_maquina = Tablero("Maquina", TAMANO_TABLERO, barcos)

tablero_jugador.colocar_barcos_aleatorios()
tablero_maquina.colocar_barcos_aleatorios()

disparos_maquina: list[tuple[int, int]] = []


# Bucle principal del juego
while True:

    # Mostrar los tableros
    print("\nTu tablero:")
    tablero_jugador.mostrar(ocultar_barcos=False)

    print("\nTablero de la máquina:")
    tablero_maquina.mostrar(ocultar_barcos=True)

    # Bucle de turno del jugador
    print("\nTu turno:")

    while True:
        fila, col = disparo()
        resultado = tablero_maquina.recibir_disparo(fila, col)

        if resultado == False:
            continue

        if tablero_maquina.comprobar_fin_partida():
            print("\n¡VICTORIA!")
            break

        if resultado == "tocado":
            print("¡Has acertado! Puedes volver a disparar.")
            continue

        if resultado == "agua":
            print("Has fallado. Turno de la máquina.")
            break

    # Si el jugador ha ganado, terminar la partida
    if tablero_maquina.comprobar_fin_partida():
        break

    # Bucle de turno de la máquina
    print("\nTurno de la máquina:")

    while True:
        fila_m, col_m = disparo_maquina(disparos_maquina)
        resultado = tablero_jugador.recibir_disparo(fila_m, col_m)

        # Comprobar si la máquina ha ganado
        if tablero_jugador.comprobar_fin_partida():
            print("\n¡HAS PERDIDO!")
            break

        # Si toca un barco, conserva el turno
        if resultado == "tocado":
            print("La máquina ha acertado y vuelve a disparar.")
            continue

        # Si dispara al agua, termina su turno
        if resultado == "agua":
            print("La máquina ha fallado. Vuelve a jugar el jugador.")
            break

    # Si la máquina ha ganado, terminar la partida
    if tablero_jugador.comprobar_fin_partida():
        break