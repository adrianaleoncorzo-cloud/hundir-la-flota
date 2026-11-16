
# ============================================================
# VARIABLES Y CONSTANTES DEL JUEGO
# ============================================================

# Tamaño del tablero.
# El tablero tendrá 10 filas y 10 columnas.
TAMANO_TABLERO = 10


# Diccionario que contiene todos los barcos de la partida.
# Cada clave representa el nombre de un barco y su valor
# indica su eslora (número de casillas que ocupa).
#
# En total hay 10 barcos que ocupan 20 casillas.
BARCOS = {
    "lancha_1": 1,
    "lancha_2": 1,
    "lancha_3": 1,
    "lancha_4": 1,
    "crucero_1": 2,
    "crucero_2": 2,
    "crucero_3": 2,
    "submarino_1": 3,
    "submarino_2": 3,
    "buque_1": 4
}


# ============================================================
# SÍMBOLOS DEL TABLERO
# ============================================================

# Cada constante representa un estado posible de una casilla.
AGUA = "A"             # Casilla vacía sin disparar
AGUA_DISPARADA = "O"   # Casilla vacía donde ya se ha disparado
BARCO = "B"            # Casilla ocupada por un barco
BARCO_TOCADO = "X"     # Casilla de un barco que ha recibido un impacto
