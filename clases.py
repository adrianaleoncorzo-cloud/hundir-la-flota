
import numpy as np


class Tablero:

    # ==================================================
    # CONSTRUCTOR
    # ==================================================

    def __init__(self, id_jugador, dimensiones, barcos):

        # Guardar los datos del jugador y sus barcos
        self.id_jugador = id_jugador
        self.dimensiones = dimensiones
        self.barcos = barcos

        # Diccionario para guardar las posiciones de cada barco
        # Lista para registrar los barcos que ya han sido hundidos
        self.posiciones_barcos = {}
        self.barcos_hundidos = []

        # Crear las matrices del tablero
        # 0 = casilla vacía / sin disparar
        self.tablero = np.zeros((dimensiones, dimensiones))
        self.disparos = np.zeros((dimensiones, dimensiones))


    # ==================================================
    # COLOCAR BARCOS
    # ==================================================

    def colocar_barcos(self, barco, fila, columna, orientacion):

        # Comprobar que el barco existe en el diccionario
        if barco not in self.barcos:
            print("El barco no existe")
            return False

        # Comprobar que el barco todavía no está colocado
        if barco in self.posiciones_barcos:
            print("Este barco ya está colocado")
            return False

        # Obtener la longitud del barco
        eslora = self.barcos[barco]

        # Lista donde guardaremos las coordenadas que ocupará el barco
        posiciones = []

        # ----------------------------------------------
        # Comprobar coordenadas
        # ----------------------------------------------

        # Las coordenadas deben ser números enteros
        if not isinstance(fila, (int, np.integer)) or not isinstance(columna, (int, np.integer)):
            print("Las coordenadas deben ser enteros")
            return False

        # Las coordenadas no pueden ser negativas
        if fila < 0 or columna < 0:
            print("Coordenadas fuera del tablero")
            return False

        # ----------------------------------------------
        # Calcular posiciones según la orientación
        # ----------------------------------------------

        # Orientación horizontal: mantener la fila y avanzar por columnas
        if orientacion == "horizontal":

            # Comprobar que el barco no salga por el límite derecho
            if columna + eslora > self.tablero.shape[1]:
                print("El barco sale del tablero")
                return False

            # Generar las coordenadas que ocupará el barco
            for i in range(eslora):
                posiciones.append((fila, columna + i))

        # Orientación vertical: mantener la columna y avanzar por filas
        elif orientacion == "vertical":

            # Comprobar que el barco no salga por el límite inferior
            if fila + eslora > self.tablero.shape[0]:
                print("El barco sale del tablero")
                return False

            # Generar las coordenadas que ocupará el barco
            for i in range(eslora):
                posiciones.append((fila + i, columna))

        # Si la orientación no es válida, lanzar un error
        else:
            raise ValueError("La orientación debe ser horizontal o vertical")

        # ----------------------------------------------
        # Comprobar que las posiciones estén libres
        # ----------------------------------------------

        # Recorrer todas las coordenadas calculadas
        for x, y in posiciones:

            # Si alguna casilla está ocupada, cancelar la colocación
            if self.tablero[x, y] != 0:
                print("Ya hay un barco en esa posición")
                return False

        # ----------------------------------------------
        # Colocar el barco en el tablero
        # ----------------------------------------------

        # Marcar con un 1 todas las casillas ocupadas por el barco
        for x, y in posiciones:
            self.tablero[x, y] = 1

        # Guardar las coordenadas del barco en el diccionario
        self.posiciones_barcos[barco] = posiciones

        # Confirmar que el barco se ha colocado correctamente
        return True


    # ==================================================
    # RECIBIR DISPAROS
    # ==================================================

    def recibir_disparo(self, fila, columna):

        # Comprobar que las coordenadas sean números enteros
        if not isinstance(fila, (int, np.integer)) or not isinstance(columna, (int, np.integer)):
            print("Las coordenadas deben ser enteros")
            return False

        # Comprobar que el disparo esté dentro de los límites del tablero
        if fila < 0 or fila >= self.dimensiones or columna < 0 or columna >= self.dimensiones:
            print("Disparo fuera del tablero")
            return False

        # Comprobar que no se haya disparado anteriormente en esa casilla
        if self.disparos[fila, columna] != 0:
            print("Ya has disparado aquí")
            return False

        # ----------------------------------------------
        # Comprobar el resultado del disparo
        # ----------------------------------------------

        # Si la casilla está vacía, el disparo ha fallado
        if self.tablero[fila, columna] == 0:

            print("Agua")

            # Registrar el disparo con un 1
            self.disparos[fila, columna] = 1

        # Si hay un barco, el disparo ha acertado
        else:

            print("¡Tocado!")

            # Registrar el impacto con un 2
            self.disparos[fila, columna] = 2

            # Comprobar si el impacto ha hundido algún barco
            self.comprobar_hundimiento()

            # Comprobar si todos los barcos han sido hundidos
            if self.comprobar_fin_partida():
                print("¡Partida terminada! Has ganado.")

        # Confirmar que el disparo se ha realizado correctamente
        return True


    # ==================================================
    # COMPROBAR BARCOS HUNDIDOS
    # ==================================================

    def comprobar_hundimiento(self):

        # Recorrer todos los barcos y sus respectivas posiciones
        for barco, posiciones in self.posiciones_barcos.items():

            # Si el barco ya está hundido, pasar al siguiente
            # Así evitamos anunciar el mismo hundimiento varias veces
            if barco in self.barcos_hundidos:
                continue

            # Suponer inicialmente que el barco está hundido
            hundido = True

            # Comprobar todas las casillas que ocupa el barco
            for x, y in posiciones:

                # Si alguna casilla no ha recibido un impacto,
                # el barco todavía no está hundido
                if self.disparos[x, y] != 2:
                    hundido = False
                    break

            # Si todos los impactos están registrados, el barco está hundido
            if hundido:

                print(f"¡Has hundido el {barco}!")

                # Añadir el barco a la lista de barcos hundidos
                self.barcos_hundidos.append(barco)


    # ==================================================
    # COMPROBAR FIN DE PARTIDA
    # ==================================================

    def comprobar_fin_partida(self):

        # Si todavía no hay barcos colocados, la partida no ha terminado
        if not self.posiciones_barcos:
            return False

        # Recorrer todos los barcos colocados
        for barco, posiciones in self.posiciones_barcos.items():

            # Comprobar todas las posiciones de cada barco
            for x, y in posiciones:

                # Si alguna casilla no ha recibido un impacto,
                # todavía quedan barcos por hundir
                if self.disparos[x, y] != 2:
                    return False

        # Si todas las casillas de todos los barcos tienen impactos,
        # la partida ha terminado
        return True


    # ==================================================
    # MOSTRAR TABLERO
    # ==================================================

    def mostrar(self, ocultar_barcos=False):

        # Crear una copia del tablero para mostrarlo
        # De esta manera no modificamos la matriz original
        tablero_visual = self.tablero.copy()

        # Si queremos ocultar los barcos (por ejemplo, al mostrar
        # el tablero del adversario)
        if ocultar_barcos:

            # Ocultar las posiciones de los barcos
            tablero_visual[self.tablero == 1] = 0

            # Mostrar los disparos que han fallado
            tablero_visual[self.disparos == 1] = 2

            # Mostrar los disparos que han acertado
            tablero_visual[self.disparos == 2] = 3

        # Imprimir el tablero resultante
        print(tablero_visual)

