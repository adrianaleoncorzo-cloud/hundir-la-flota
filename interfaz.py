import tkinter as tk

from Funciones import elegir_disparo_maquina
from variables import TAMANO_TABLERO, barcos
from clases import Tablero


def abrir_interfaz():
    tablero_jugador = Tablero("Jugador", TAMANO_TABLERO, barcos)
    tablero_maquina = Tablero("Maquina", TAMANO_TABLERO, barcos)
    tablero_jugador.colocar_barcos_aleatorios()
    tablero_maquina.colocar_barcos_aleatorios()

    disparos_maquina = []
    partida_terminada = False
    turno_jugador = True

    ventana = tk.Tk()
    ventana.title("Hundir la flota")
    ventana.resizable(False, False)

    tk.Label(
        ventana,
        text="Hundir la flota",
        font=("Arial", 16, "bold")
    ).pack(pady=8)

    estado = tk.StringVar(value="Elige una casilla del tablero enemigo.")
    tk.Label(ventana, textvariable=estado, font=("Arial", 11)).pack(pady=6)

    marco_tableros = tk.Frame(ventana)
    marco_tableros.pack(padx=10, pady=8)

    marco_jugador = tk.LabelFrame(marco_tableros, text="Tu tablero")
    marco_jugador.pack(side="left", padx=8)

    marco_maquina = tk.LabelFrame(marco_tableros, text="Tablero enemigo")
    marco_maquina.pack(side="left", padx=8)

    botones_jugador = {}
    botones_maquina = {}

    def crear_tablero(marco, es_enemigo):
        casillas = {}

        for columna in range(TAMANO_TABLERO):
            letra = chr(ord("A") + columna)
            tk.Label(marco, text=letra, width=2).grid(
                row=0, column=columna + 1
            )

        for fila in range(TAMANO_TABLERO):
            tk.Label(marco, text=str(fila + 1), width=2).grid(
                row=fila + 1, column=0
            )

            for columna in range(TAMANO_TABLERO):
                if es_enemigo:
                    casilla = tk.Button(
                        marco,
                        text=" ",
                        width=2,
                        height=1,
                        # Guardamos las coordenadas de esta casilla para el clic.
                        command=lambda f=fila, c=columna: disparar(f, c)
                    )
                else:
                    casilla = tk.Label(
                        marco,
                        text=" ",
                        width=2,
                        height=1,
                        relief="solid",
                        bg="white"
                    )

                casilla.grid(
                    row=fila + 1,
                    column=columna + 1,
                    padx=1,
                    pady=1
                )
                casillas[(fila, columna)] = casilla

        return casillas

    botones_jugador = crear_tablero(marco_jugador, False)
    botones_maquina = crear_tablero(marco_maquina, True)

    tk.Label(
        ventana,
        text="B = barco   O = agua   X = tocado"
    ).pack(pady=(0, 8))

    def actualizar_tablero(tablero, casillas, ocultar_barcos, bloquear_disparos=False):
        for (fila, columna), casilla in casillas.items():
            if tablero.disparos[fila, columna] == 1:
                texto = "O"
                color = "#9bd3e8"
            elif tablero.disparos[fila, columna] == 2:
                texto = "X"
                color = "#ed8b8b"
            elif not ocultar_barcos and tablero.tablero[fila, columna] == 1:
                texto = "B"
                color = "#b8b8b8"
            else:
                texto = " "
                color = "white"

            casilla.configure(text=texto, bg=color)

            if ocultar_barcos:
                ya_disparada = tablero.disparos[fila, columna] != 0
                if bloquear_disparos or ya_disparada:
                    casilla.configure(state=tk.DISABLED)
                else:
                    casilla.configure(state=tk.NORMAL)

    def terminar(mensaje):
        nonlocal partida_terminada
        partida_terminada = True
        estado.set(mensaje)

        for casilla in botones_maquina.values():
            casilla.configure(state=tk.DISABLED)

    def turno_maquina():
        nonlocal turno_jugador

        if partida_terminada:
            return

        # En la ventana, los mensajes se muestran en el texto de estado.
        fila, columna = elegir_disparo_maquina(disparos_maquina)
        resultado = tablero_jugador.recibir_disparo(
            fila,
            columna,
            mostrar_mensajes=False
        )

        if resultado is False:
            ventana.after(100, turno_maquina)
            return

        actualizar_tablero(tablero_jugador, botones_jugador, False)

        if tablero_jugador.comprobar_fin_partida():
            terminar("La maquina ha hundido todos tus barcos. Has perdido.")
        elif resultado == "tocado":
            estado.set("La maquina ha tocado un barco. Dispara otra vez.")
            ventana.after(700, turno_maquina)
        else:
            turno_jugador = True
            actualizar_tablero(
                tablero_maquina,
                botones_maquina,
                True,
                bloquear_disparos=False
            )
            estado.set("Tu turno: elige una casilla del tablero enemigo.")

    def disparar(fila, columna):
        nonlocal turno_jugador

        if partida_terminada or not turno_jugador:
            return

        resultado = tablero_maquina.recibir_disparo(
            fila,
            columna,
            mostrar_mensajes=False
        )

        if resultado is False:
            estado.set("No se pudo hacer ese disparo. Prueba otra casilla.")
            return

        actualizar_tablero(tablero_maquina, botones_maquina, True)

        if tablero_maquina.comprobar_fin_partida():
            terminar("¡Has hundido todos los barcos! Has ganado.")
        elif resultado == "tocado":
            estado.set("¡Tocado! Puedes volver a disparar.")
        else:
            turno_jugador = False
            actualizar_tablero(
                tablero_maquina,
                botones_maquina,
                True,
                bloquear_disparos=True
            )
            estado.set("Agua. Ahora juega la maquina.")
            ventana.after(700, turno_maquina)

    actualizar_tablero(tablero_jugador, botones_jugador, False)
    actualizar_tablero(tablero_maquina, botones_maquina, True)

    ventana.mainloop()
