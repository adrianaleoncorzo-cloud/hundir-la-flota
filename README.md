# hundir-la-flota
desarrollo hundir la flota game
Configuración del juego
En el archivo variables.py se han creado las variables que se utilizan en el juego.

TAMANO_TABLERO = 10 indica que el tablero tendrá 10 filas y 10 columnas.

barcos es un diccionario que contiene los barcos disponibles y su tamaño:

Cuatro barcos de longitud 1.
Tres barcos de longitud 2.
Dos barcos de longitud 3.
Un barco de longitud 4.
La clave identifica cada barco y el valor indica cuántas casillas ocupa.

Se han definido símbolos para representar el estado de las casillas:

AGUA = "A": casilla vacía.
AGUA_DISPARADA = "O": casilla vacía a la que ya se ha disparado.
BARCO = "B": casilla ocupada por un barco.
BARCO_TOCADO = "X": parte de un barco que ha recibido un disparo.
También se han creado mensajes para informar al jugador:

Cuando se dispara al agua.
Cuando se toca un barco.
Cuando se gana o se pierde la partida.

## Clase Tablero

En el archivo `clases.py` se ha creado la clase `Tablero`. Esta clase representa el tablero de cada jugador y reúne todos los datos y acciones relacionados con su partida.

Al crear un tablero, se guardan el identificador del jugador, el tamaño del tablero y los barcos disponibles. También se crean dos matrices con NumPy:

- `tablero`: contiene la posición de los barcos.
- `disparos`: guarda los disparos realizados contra ese tablero.

En estas matrices se usa `0` para indicar que una casilla está vacía o que todavía no se ha disparado, y otros números para representar barcos, agua disparada o barcos tocados.

La clase incluye las siguientes funciones:

- `colocar_barco`: intenta colocar un barco en una posición y con una orientación concretas. Comprueba que el barco exista, que no haya sido colocado antes y que todas sus casillas estén dentro del tablero y libres.
- `colocar_barcos_aleatorios`: coloca automáticamente todos los barcos en posiciones aleatorias.
- `recibir_disparo`: recibe las coordenadas de un disparo y determina si han acertado en el agua o en un barco.
- `comprobar_hundimiento`: revisa si todas las partes de un barco han sido tocadas y lo marca como hundido.
- `comprobar_fin_partida`: comprueba si se han hundido todos los barcos.
- `mostrar`: dibuja el tablero en la consola. También puede ocultar los barcos para que un jugador no vea los del rival.

## Funciones auxiliares

En el archivo `funciones.py` se han creado funciones que ayudan al jugador a interactuar con el juego.

- `mostrar_instrucciones`: muestra por pantalla las reglas principales del juego.
- `disparo`: pide al jugador una fila y una columna para realizar un disparo. Primero pide una letra de la `A` a la `J` y después un número del `0` al `9`. Si se introduce un valor incorrecto, vuelve a pedirlo hasta que sea válido. Después convierte la letra en un número y devuelve las coordenadas.
- `elegir_disparo_maquina`: elige aleatoriamente una fila y una columna para que dispare la máquina. Comprueba los disparos realizados anteriormente y evita repetir una posición.

Las coordenadas válidas se guardan en `letras_validas` y `numeros_validos`. La función `elegir_disparo_maquina` utiliza `random` para elegir posiciones aleatorias dentro del tamaño del tablero.

## Interfaz gráfica

En el archivo `interfaz.py` se ha creado la interfaz gráfica del juego con Tkinter. Esta configuración se ha realizado con ayuda de la IA para que la interfaz sea más sencilla y visual, especialmente durante el aprendizaje de cómo crear una aplicación con ventanas y botones.

Al abrir la interfaz se crean dos tableros:

- El tablero del jugador, donde se pueden ver sus barcos.
- El tablero enemigo, donde se eligen las casillas a las que se dispara.

La interfaz muestra letras de la `A` a la `J` en las columnas y números del `1` al `10` en las filas.

Los colores y símbolos permiten reconocer cada situación:

- `B`: barco propio.
- Espacio en blanco: casilla sin barco o sin descubrir.
- `O`: disparo que ha sido agua.
- `X`: disparo que ha acertado en un barco.

Cada casilla del tablero enemigo es un botón. Al pulsarla, se llama a la función `disparar`, que registra el disparo y actualiza el tablero. Cuando el jugador acierta puede volver a disparar; si falla, comienza el turno de la máquina.

La máquina elige disparos aleatorios con la función `elegir_disparo_maquina` y después vuelve a disparar si acierta. Si hunde todos los barcos del jugador o el jugador hunde todos los barcos de la máquina, la partida termina y se desactivan los botones para impedir nuevos disparos.