

from clases import Tablero
from variables import TAMANO_TABLERO, barcos
from funciones import mostrar_instrucciones, disparo, disparo_maquina

mostrar_instrucciones()

tablero_jugador = Tablero("Jugador", TAMANO_TABLERO, barcos)
tablero_maquina = Tablero("Maquina", TAMANO_TABLERO, barcos)
tablero_jugador.colocar_barcos_aleatorios()
tablero_maquina.colocar_barcos_aleatorios()
disparos_maquina: list[tuple[int, int]] = []
partida_terminada = False


while partida_terminada == False:
    
    print("\nTu tablero:")
    tablero_jugador.mostrar(ocultar_barcos=False)

    print("\nTablero maquina")
    tablero_maquina.mostrar(ocultar_barcos=True)

    print("\nTu turno:")

    while True:

        fila, columna = disparo()
        resultado = tablero_maquina.recibir_disparo(fila, columna)

        if resultado == False:
            continue

        if tablero_maquina.comprobar_fin_partida():
            print("\n¡ENHORABUENA! HAS GANADO LA PARTIDA.")
            partida_terminada = True
            break

        if resultado == "tocado":
            print("¡Has acertado! Puedes volver a disparar.")
            continue

        if resultado == "agua":
            print("Has fallado. Turno de la máquina.")
            break

    if partida_terminada:
        break

    print("\n========== TURNO DE LA MÁQUINA ==========")

    while True:

        fila, columna = disparo_maquina(disparos_maquina)

        print(f"\nLa máquina dispara en la fila {fila + 1}, columna {chr(65 + columna)}")

        resultado = tablero_jugador.recibir_disparo(fila, columna)

        if resultado == False:
            continue

        if tablero_jugador.comprobar_fin_partida():
            print("\nHAS PERDIDO. LA MÁQUINA HA GANADO.")
            partida_terminada = True
            break

        if resultado == "tocado":
            print("La máquina ha acertado y vuelve a disparar.")
            continue

        if resultado == "agua":
            print("La máquina ha fallado. Vuelve a jugar el jugador.")
            break

print("\n========== FIN DE LA PARTIDA ==========")

print("\nTablero final del jugador:")
tablero_jugador.mostrar(ocultar_barcos=False)

print("\nTablero final de la máquina:")
tablero_maquina.mostrar(ocultar_barcos=False)
