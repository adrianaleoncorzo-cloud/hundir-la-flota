from Funciones import mostrar_instrucciones, disparo, elegir_disparo_maquina
from variables import TAMANO_TABLERO, barcos
from clases import Tablero


def jugar_consola():
    tablero_jugador = Tablero("Jugador", TAMANO_TABLERO, barcos)
    tablero_maquina = Tablero("Maquina", TAMANO_TABLERO, barcos)

    # Colocamos los barcos antes de empezar para que haya barcos que hundir.
    tablero_jugador.colocar_barcos_aleatorios()
    tablero_maquina.colocar_barcos_aleatorios()

    disparos_maquina = []
    partida_terminada = False

    mostrar_instrucciones()

    # La partida sigue hasta que se hundan todos los barcos de alguien.
    while not partida_terminada:
        print("\n" + "-" * 30)
        print("Tablero del jugador")
        tablero_jugador.mostrar(ocultar_barcos=False)

        print("\nTablero de la maquina")
        tablero_maquina.mostrar(ocultar_barcos=True)

        print("Tu turno:")
        while True:
            fila, columna = disparo()
            resultado = tablero_maquina.recibir_disparo(fila, columna)

            if resultado is False:
                continue

            if tablero_maquina.comprobar_fin_partida():
                print("\n¡VICTORIA!")
                partida_terminada = True
                break

            # Si fue agua, el turno termina; si acertamos, podemos disparar otra vez.
            if resultado == "agua":
                break

        if partida_terminada:
            break

        print("\nTurno de la maquina:")
        while True:
            fila_m, col_m = elegir_disparo_maquina(disparos_maquina)
            resultado = tablero_jugador.recibir_disparo(fila_m, col_m)

            if resultado is False:
                continue

            if tablero_jugador.comprobar_fin_partida():
                print("\n¡HAS PERDIDO!")
                partida_terminada = True
                break

            # La maquina tambien sigue disparando si ha tocado un barco.
            if resultado == "agua":
                break


def main():
    respuesta = input("¿Quieres abrir la interfaz grafica? (s/n): ").strip().lower()

    while respuesta not in ("s", "si", "sí", "n", "no"):
        respuesta = input("Escribe s para la interfaz o n para la consola: ").strip().lower()

    if respuesta in ("s", "si", "sí"):
        # La interfaz solo se importa si se elige, para dejar la consola independiente.
        from interfaz import abrir_interfaz

        abrir_interfaz()
    else:
        jugar_consola()


if __name__ == "__main__":
    main()
