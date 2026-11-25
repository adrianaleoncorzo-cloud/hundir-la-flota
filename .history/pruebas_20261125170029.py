

from clases import Tablero
from variables import TAMANO_TABLERO, barcos
from Funciones import mostrar_instrucciones, disparo, disparo_maquina

mostrar_instrucciones()

tablero_jugador = Tablero("Jugador", TAMANO_TABLERO, barcos)
tablero_maquina = Tablero("Maquina", TAMANO_TABLERO, barcos)

tablero_jugador.colocar_barcos_aleatorios()
tablero_maquina.colocar_barcos_aleatorios()


disparos_maquina = []

partida_terminada = False


# ==========================================
# 6. BUCLE PRINCIPAL DEL JUEGO
# ==========================================

while partida_terminada == False:

    # --------------------------------------
    # MOSTRAR LOS TABLEROS
    # --------------------------------------

    print("\n========== TABLERO DEL JUGADOR ==========")
    tablero_jugador.mostrar(ocultar_barcos=False)

    print("\n========== TABLERO DE LA MÁQUINA ==========")
    tablero_maquina.mostrar(ocultar_barcos=True)


    # ======================================
    # 7. TURNO DEL JUGADOR
    # ======================================

    print("\n========== TURNO DEL JUGADOR ==========")

    while True:

        # Solicitar coordenadas del disparo
        fila, columna = disparo()

        # Realizar el disparo contra la máquina
        resultado = tablero_maquina.recibir_disparo(fila, columna)

        # Si el disparo no es válido, volver a intentarlo
        if resultado == False:
            continue

        # Comprobar si el jugador ha ganado
        if tablero_maquina.comprobar_fin_partida():
            print("\n¡ENHORABUENA! HAS GANADO LA PARTIDA.")
            partida_terminada = True
            break

        # Si toca un barco, conserva el turno
        if resultado == "tocado":
            print("¡Has acertado! Puedes volver a disparar.")
            continue

        # Si dispara al agua, termina su turno
        if resultado == "agua":
            print("Has fallado. Turno de la máquina.")
            break


    # Si el jugador ha ganado, no juega la máquina
    if partida_terminada:
        break


    # ======================================
    # 8. TURNO DE LA MÁQUINA
    # ======================================

    print("\n========== TURNO DE LA MÁQUINA ==========")

    while True:

        # Generar coordenadas aleatorias
        fila, columna = disparo_maquina(disparos_maquina, TAMANO_TABLERO)

        print(f"\nLa máquina dispara en la fila {fila + 1}, columna {chr(65 + columna)}")

        # Realizar el disparo contra el jugador
        resultado = tablero_jugador.recibir_disparo(fila, columna)

        # Si el disparo no es válido, generar otro
        if resultado == False:
            continue

        # Comprobar si la máquina ha ganado
        if tablero_jugador.comprobar_fin_partida():
            print("\nHAS PERDIDO. LA MÁQUINA HA GANADO.")
            partida_terminada = True
            break

        # Si toca un barco, la máquina conserva el turno
        if resultado == "tocado":
            print("La máquina ha acertado y vuelve a disparar.")
            continue

        # Si dispara al agua, termina su turno
        if resultado == "agua":
            print("La máquina ha fallado. Vuelve a jugar el jugador.")
            break


# ==========================================
# 9. FINAL DE LA PARTIDA
# ==========================================

print("\n========== FIN DE LA PARTIDA ==========")

print("\nTablero final del jugador:")
tablero_jugador.mostrar(ocultar_barcos=False)

print("\nTablero final de la máquina:")
tablero_maquina.mostrar(ocultar_barcos=False)
