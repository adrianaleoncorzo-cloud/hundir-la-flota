
import numpy as np
from variables import AGUA, AGUA_DISPARADA, BARCO, BARCO_TOCADO


class Tablero:
    """
    Representa el tablero de juego de un jugador.

    Attributes:
        id_jugador (str): Identificador del jugador.
        dimensiones (int): Tamaño del tablero (dimensiones x dimensiones).
        barcos (dict): Diccionario con los nombres y tamaños de los barcos.
        tablero (np.ndarray): Tablero donde se colocan los barcos.
        disparos (np.ndarray): Tablero donde se registran los disparos recibidos.
        posiciones_barcos (dict): Posiciones que ocupa cada barco.
        barcos_hundidos (list): Lista de barcos que han sido hundidos.
    """

    def __init__(self, id_jugador, dimensiones, barcos):
        """
        Inicializa el tablero y guarda los datos del jugador y sus barcos.

        Atributos:
            id_jugador (str): Identificador del jugador.
            dimensiones (int): Tamaño del tablero.
            barcos (dict): Diccionario con los nombres y tamaños de los barcos.
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


    def colocar_barco(self, barco, fila, columna, orientacion):
        """
        Comprueba si el barco se puede colocar y lo coloca en el tablero.

        Atributos:
            barco (str): Nombre del barco que se quiere colocar.
            fila (int): Fila donde comienza el barco.
            columna (int): Columna donde comienza el barco.
            orientacion (str): Orientación del barco (N, S, E u O).

        Returns:
            bool: True si se coloca correctamente, False si no es posible.
        """

        if barco not in self.barcos:
            return False

        if barco in self.posiciones_barcos:
            return False

        eslora = self.barcos[barco]

        if not isinstance(fila, (int, np.integer)) or not isinstance(columna, (int, np.integer)):
            return False

        if fila < 0 or columna < 0 or fila >= self.dimensiones or columna >= self.dimensiones:
            return False

        posiciones = []

        # Calcular las posiciones según la orientación
        if orientacion == "N":

            if fila - (eslora - 1) < 0:
                return False

            for i in range(eslora):
                posiciones.append((fila - i, columna))

        elif orientacion == "S":

            if fila + eslora > self.dimensiones:
                return False

            for i in range(eslora):
                posiciones.append((fila + i, columna))

        elif orientacion == "E":

            if columna + eslora > self.dimensiones:
                return False

            for i in range(eslora):
                posiciones.append((fila, columna + i))

        elif orientacion == "O":

            if columna - (eslora - 1) < 0:
                return False

            for i in range(eslora):
                posiciones.append((fila, columna - i))

        else:
            return False

        # Comprobar que todas las posiciones están libres
        for x, y in posiciones:
            if self.tablero[x, y] != 0:
                return False

        # Colocar el barco
        for x, y in posiciones:
            self.tablero[x, y] = 1

        self.posiciones_barcos[barco] = posiciones

        return True


    def colocar_barcos_aleatorios(self):
        """
        Coloca todos los barcos en posiciones y orientaciones aleatorias.
        """

        for barco in self.barcos:

            colocado = False
            intentos = 0
            num_intentos = 1000

            while colocado == False and intentos < num_intentos:

                # Generar coordenadas aleatorias
                fila = np.random.randint(0, self.dimensiones)
                columna = np.random.randint(0, self.dimensiones)

                # Elegir una orientación aleatoria
                orientacion = np.random.choice(["N", "S", "E", "O"])

                # Intentar colocar el barco
                colocado = self.colocar_barco(
                    barco,
                    fila,
                    columna,
                    orientacion
                )

                intentos += 1

            if colocado == False:
                raise RuntimeError(
                    f"No se pudo colocar el barco {barco} "
                    f"después de {num_intentos} intentos"
                )


    def recibir_disparo(self, fila, columna):
        """
        Comprueba el disparo y registra si ha tocado agua o un barco.

        Atributos:
            fila (int): Fila donde se realiza el disparo.
            columna (int): Columna donde se realiza el disparo.

        Returns:
            str or bool: 'agua' si alcanza el agua, 'tocado' si alcanza
            un barco o False si el disparo no es válido.
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
        Comprueba si algún barco ha recibido todos sus impactos.

        Actualiza la lista de barcos hundidos cuando corresponde.
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
        Comprueba si todos los barcos están hundidos.

        Returns:
            bool: True si todos los barcos están hundidos, False en caso contrario.
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
        Muestra el tablero y permite ocultar los barcos del rival.

        Atributos:
            ocultar_barcos (bool): Si es True, oculta los barcos que no han sido tocados.
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
