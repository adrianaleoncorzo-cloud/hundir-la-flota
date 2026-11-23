
import numpy as np
from variables import AGUA, AGUA_DISPARADA, BARCO, BARCO_TOCADO


class Tablero:
    
    """
    Representa el tablero de un jugador en el juego Hundir la Flota.
    """

    def __init__(self, id_jugador, dimensiones, barcos):
        
        """
        Inicializa el tablero y sus datos.

        Parametros:
            id_jugador: Identificador del jugador.
            dimensiones: Tamaño del tablero.
            barcos: Diccionario con los nombres y las esloras de los barcos.
        """

        self.id_jugador = id_jugador
        self.dimensiones = dimensiones
        self.barcos = barcos

        self.posiciones_barcos = {}
        self.barcos_hundidos = []

        # 0 = agua, 1 = barco
        self.tablero = np.zeros((dimensiones, dimensiones), dtype=int)

        # 0 = sin disparar, 1 = agua, 2 = barco tocado
        self.disparos = np.zeros((dimensiones, dimensiones), dtype=int)


    def colocar_barcos(self, barco, fila, columna, orientacion):
        """
        Coloca un barco en el tablero según su posición y orientación.

        Parametros:
            barco: Nombre del barco que se va a colocar.
            fila: Fila inicial del barco.
            columna: Columna inicial del barco.
            orientacion: Dirección del barco (N, S, E u O).

        Returns:
            True si el barco se coloca correctamente, False si no es posible.
        """

        if barco not in self.barcos:
            print("El barco no existe")
            return False

        if barco in self.posiciones_barcos:
            print("Este barco ya está colocado")
            return False

        eslora = self.barcos[barco]

        if not isinstance(fila, (int, np.integer)) or not isinstance(columna, (int, np.integer)):
            print("Las coordenadas deben ser enteros")
            return False

        if fila < 0 or columna < 0 or fila >= self.dimensiones or columna >= self.dimensiones:
            print("Coordenadas fuera del tablero")
            return False

        posiciones = []

        # Calcular las posiciones según la orientación
        if orientacion == "N":

            if fila - (eslora - 1) < 0:  # (eslora - 1)Para que empiece a contar en la primera posición
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

            if columna - (eslora - 1) < 0:
                print("El barco sale del tablero")
                return False

            for i in range(eslora):
                posiciones.append((fila, columna - i))

        else:
            raise ValueError("La orientación debe ser N, S, E u O")

        # Comprobar que las posiciones están libres
        for x, y in posiciones:

            if self.tablero[x, y] != 0:
                print(f"Estás pisando un barco en la posición ({x}, {y})")
                return False

        # Colocar el barco
        for x, y in posiciones:
            self.tablero[x, y] = 1

        self.posiciones_barcos[barco] = posiciones

        return True


    def recibir_disparo(self, fila, columna):
        """
        Registra un disparo y comprueba si alcanza un barco.

        Parametros:
            fila: Fila donde se realiza el disparo.
            columna: Columna donde se realiza el disparo.

        Returns:
            'agua' si alcanza el agua, 'tocado' si alcanza un barco
            o False si el disparo no es válido.
        """

        if not isinstance(fila, (int, np.integer)) or not isinstance(columna, (int, np.integer)):
            print("Las coordenadas deben ser enteros")
            return False

        if fila < 0 or columna < 0 or fila >= self.dimensiones or columna >= self.dimensiones:
            print("Disparo fuera del tablero")
            return False

        if self.disparos[fila, columna] != 0:
            print("Ya has disparado en esa posición")
            return False

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


    def comprobar_hundimiento(self):
        """
        Comprueba si alguno de los barcos ha recibido todos sus impactos.

        Los barcos hundidos se guardan en la lista barcos_hundidos.
        """

        for barco, posiciones in self.posiciones_barcos.items():

            if barco not in self.barcos_hundidos:

                hundido = True

                for x, y in posiciones:

                    if self.disparos[x, y] != 2:
                        hundido = False
                        break

                if hundido:
                    self.barcos_hundidos.append(barco)
                    print(f"¡Has hundido el barco {barco}!")


    def comprobar_fin_partida(self):
        """
        Comprueba si todos los barcos están colocados y hundidos.

        Returns:
            True si todos los barcos están hundidos, False en caso contrario.
        """

        if len(self.posiciones_barcos) != len(self.barcos):
            return False

        for barco, posiciones in self.posiciones_barcos.items():

            for x, y in posiciones:

                if self.disparos[x, y] != 2:
                    return False

        return True


    def mostrar(self, ocultar_barcos=False):
        """
        Muestra el tablero por consola.

        Parametros:
            ocultar_barcos: Si es True, oculta los barcos que no han sido tocados.
        """

        print("  A B C D E F G H I J")

        for fila in range(self.dimensiones):

            print(f"{fila + 1:2}", end=" ")

            for columna in range(self.dimensiones):

                if self.disparos[fila, columna] == 1:
                    print(AGUA_DISPARADA, end=" ")

                elif self.disparos[fila, columna] == 2:
                    print(BARCO_TOCADO, end=" ")

                elif self.tablero[fila, columna] == 1 and not ocultar_barcos:
                    print(BARCO, end=" ")

                else:
                    print(AGUA, end=" ")

            print()
