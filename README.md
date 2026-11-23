# hundir-la-flota
desarrollo hundir la flota game
    HUNDIR LA FLOTA
    1.VARIABLES.PY
    En este apartado se ha definido las variables globales para la configuración inicial del juego.
    Se ha creado -TAMANO_TABLERO- que en este caso es de 10, el cual determina las dimensiones de este y será 10x10 casillas en total.
    Luego se ha definido el diccionario -barcos-, ahí se guardan los barcos que participarán en la partida. Cada barco se ha identificado de forma única y con un valor que indica la cantidad de casillas que va a ocupar. La flota se compone de 10 barcos y hay 3 tamaños.
    - 4 barcos del tamño 1 
    - 3 barcos del tamaño 2
    - 1 barco del tamaño 4
    Luego se representan cuatro valores que indican los estados de las casillas:
    A=agua(casilla vacía sin disparo aún)
    0=agua afectada(casilla de agua en la que ya se ha realizado un disparo)
    B=barco(casilla ocupada por un barco)
    X=barco_tocado(casilla ocupada por un barco disparado)
    