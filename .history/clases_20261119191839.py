import numpy as np

class Tablero:

    # ==================================================
    # CONSTRUCTOR
    # ==================================================

    def __init__(self, id_jugador, dimensiones, barcos):

        self.id_jugador = id_jugador
        self.dimensiones = dimensiones
        self.barcos = barcos

        self.posiciones_barcos = {}
        self.barcos_hundidos = []

        # Tablero interno: 0 = agua, 1 = barco
        self.tablero = np.zeros((dimensiones, dimensiones), dtype=int)

        # Disparos: 0 = sin disparar, 1 = agua, 2 = barco tocado
        self.disparos = np.zeros((dimensiones, dimensiones), dtype=int)


    # ==================================================
    # COLOCAR BARCOS
    # ==================================================

    def colocar_barcos(self, barco, fila, columna, orientacion):

        # Comprobar que el barco existe
        if barco not in self.barcos:
            print("El barco no existe")
            return False

        # Comprobar que el barco no está colocado
        if barco in self.posiciones_barcos:
            print("Este barco ya está colocado")
            return False

        # Obtener la longitud del barco
        eslora = self.barcos[barco]

        # Comprobar que las coordenadas son enteros
        if not isinstance(fila, (int, np.integer)) or not isinstance(columna, (int, np.integer)):
            print("Las coordenadas deben ser enteros")
            return False

        # Comprobar que las coordenadas están dentro del tablero
        if fila < 0 or columna < 0 or fila >= self.dimensiones or columna >= self.dimensiones:
            print("Coordenadas fuera del tablero")
            return False

        posiciones = []

        # Calcular las posiciones según la orientación
        if orientacion == "N":

            if fila - eslora + 1 < 0:
                print("El barco sale del tablero")
                return False

            for i in range(eslora):
                posiciones.append((fila - i, columna))

        elif orientacion == "S":

            if fila + eslora > self.dimensiones:
                print("El barco sale del tablero")
                return False

            for i in range(eslora):
                posiciones.append((fila + i, columna))

        elif orientacion == "E":

            if columna + eslora > self.dimensiones:
                print("El barco sale del tablero")
                return False

            for i in range(eslora):
                posiciones.append((fila, columna + i))

        elif orientacion == "O":

            if columna - eslora + 1 < 0:
                print("El barco sale del tablero")
                return False

            for i in range(eslora):
                posiciones.append((fila, columna - i))

        else:
            raise ValueError("La orientación debe ser N, S, E u O")

        # Comprobar que ninguna posición está ocupada
        for x, y in posiciones:

            if self.tablero[x, y] != 0:
                print("Ya hay un barco en esa posición")
                return False

        # Colocar el barco
        for x, y in posiciones:
            self.tablero[x, y] = 1

        # Guardar las posiciones del barco
        self.posiciones_barcos[barco] = posiciones

        return True


    # ==================================================
    # RECIBIR DISPARO
    # ==================================================

    def recibir_disparo(self, fila, columna):

        # Comprobar que las coordenadas son enteros
        if not isinstance(fila, (int, np.integer)) or not isinstance(columna, (int, np.integer)):
            print("Las coordenadas deben ser enteros")
            return False

        # Comprobar que las coordenadas están dentro del tablero
        if fila < 0 or columna < 0 or fila >= self.dimensiones or columna >= self.dimensiones:
            print("Disparo fuera del tablero")
            return False

        # Comprobar si ya se ha disparado en esa posición
        if self.disparos[fila, columna] != 0:
            print("Ya has disparado en esa posición")
            return False

        # Comprobar si el disparo ha alcanzado un barco
        if self.tablero[fila, columna] == 0:

            self.disparos[fila, columna] = 1

            print("¡Agua!")

            return "agua"

        else:

            self.disparos[fila, columna] = 2

            print("¡Tocado!")

            self.comprobar_hundimiento()

            if self.comprobar_fin_partida():
                print(f"¡El jugador {self.id_jugador} ha hundido todos los barcos!")

            return "tocado"


    # ==================================================
    # COMPROBAR HUNDIMIENTO
    # ==================================================

    def comprobar_hundimiento(self):

        for barco, posiciones in self.posiciones_barcos.items():

            # Comprobar que el barco todavía no está hundido
            if barco not in self.barcos_hundidos:

                hundido = True

                # Comprobar si todas sus posiciones han sido alcanzadas
                for x, y in posiciones:

                    if self.disparos[x, y] != 2:
                        hundido = False
                        break

                # Registrar el barco hundido
                if hundido:
                    self.barcos_hundidos.append(barco)
                    print(f"¡Has hundido el barco {barco}!")


    # ==================================================
    # COMPROBAR FIN DE PARTIDA
    # ==================================================

    def comprobar_fin_partida(self):
        
        #   Comprobar que todos los barcos están colocados
        if len(self.posiciones_barcos) != len(self.barcos):
            return False

        # Comprobar que todos los barcos están hundidos
        for barco, posiciones in self.posiciones_barcos.items():

            for x, y in posiciones:

                if self.disparos[x, y] != 2:
                    return False

        return True


    # ==================================================
    # MOSTRAR TABLERO
    # ==================================================

    def mostrar(self, ocultar_barcos=False):

        print("  A B C D E F G H I J")

        for fila in range(self.dimensiones):

            print(f"{fila + 1:2}", end=" ")

            for columna in range(self.dimensiones):

                # Agua disparada
                if self.disparos[fila, columna] == 1:
                    print(AGUA_DISPARADA, end=" ")

                # Barco tocado
                elif self.disparos[fila, columna] == 2:
                    print(BARCO_TOCADO, end=" ")

                # Barco sin descubrir
                elif self.tablero[fila, columna] == 1 and not ocultar_barcos:
                    print(BARCO, end=" ")

                # Agua sin descubrir o barco oculto
                else:
                    print(AGUA, end=" ")

            print()
