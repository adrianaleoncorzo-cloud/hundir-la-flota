# Hundir la flota

Este proyecto desarrolla el juego Hundir la flota. Se ha organizado en tres
módulos principales para separar los datos, las funciones y la representación
del tablero.

## 1. `variables.py`

Este módulo guarda la configuración global del juego.

### Tamaño del tablero

`TAMANO_TABLERO = 10` crea un tablero de 10 filas por 10 columnas.
Las variables permiten reutilizar este dato sin repetir el número 10.

### Barcos

El diccionario `barcos` relaciona el nombre de cada barco con su longitud:

- 4 barcos de 1 casilla;
- 3 barcos de 2 casillas;
- 2 barcos de 3 casillas;
- 1 barco de 4 casillas.

En total participan 10 barcos.

### Estados de las casillas

- `AGUA = "A"`: agua sin disparar.
- `AGUA_DISPARADA = "O"`: agua ya alcanzada.
- `BARCO = "B"`: barco visible.
- `BARCO_TOCADO = "X"`: barco alcanzado.

También existen variables para los mensajes de tocado, agua, victoria y derrota.
Usar nombres claros hace que el código sea más fácil de entender y modificar.

## 2. `Funciones.py`

Este módulo agrupa acciones que se pueden reutilizar.

### Mostrar las instrucciones

`Instrucciones` guarda el texto de ayuda y `mostrar_instrucciones()` lo muestra
por pantalla con `print()`.

### Pedir coordenadas

`letras_validas` contiene las letras y `numeros_validos` contiene las columnas
disponibles. Ambas listas dependen de `TAMANO_TABLERO`.

La función `disparo()` pide una fila y una columna, valida las respuestas y
repite la pregunta mientras sean incorrectas.

```python
fila = input("Elige una fila (A-J): ").strip().upper()
columna = input("Elige una columna (0-9): ").strip()
```

Después, convierte la letra en un índice y el texto de la columna en entero:

```python
fila_numero = letras_validas.index(fila)
columna_numero = int(columna)
return fila_numero, columna_numero
```

`strip()` elimina espacios sobrantes y `upper()` convierte letras minúsculas
en mayúsculas.

### Disparo aleatorio de la máquina

`elegir_disparo_maquina(disparos_hechos)` usa `random.randint()` para elegir una
fila y una columna dentro del tablero.

La función convierte los disparos anteriores en un conjunto y evita repetir una
posición. Cuando encuentra una casilla nueva, la añade a la lista y la devuelve
como `(fila, columna)`.

Si ya están ocupadas todas las casillas, avisa mediante un `RuntimeError`.

## 3. `clases.py`

Este módulo define la clase `Tablero`, que representa el tablero de un jugador.
Una clase agrupa datos y acciones relacionadas.

### Constructor

El método `__init__()` se ejecuta al crear un objeto. Inicializa el jugador,
las dimensiones, los barcos y las posiciones utilizadas:

```python
tablero_jugador = Tablero("Jugador", TAMANO_TABLERO, barcos)
tablero_maquina = Tablero("Maquina", TAMANO_TABLERO, barcos)
```

`self` permite que cada objeto conserve sus propios datos.

### Matrices del tablero

La clase utiliza matrices de `numpy`:

- `tablero`: coloca los barcos, usando `0` para agua y `1` para barco.
- `disparos`: registra los impactos, usando `0`, `1` y `2`.
- `posiciones_barcos`: relaciona cada barco con sus casillas.
- `barcos_hundidos`: guarda los barcos que ya han sido hundidos.

### Colocación de barcos

`colocar_barco()` comprueba si el barco existe, si ya está colocado, si las
coordenadas son válidas y si todas sus casillas están libres.

Acepta estas orientaciones:

- `N`: norte;
- `S`: sur;
- `E`: este;
- `O`: oeste.

Devuelve `True` si consigue colocarlo y `False` si no es posible.

`colocar_barcos_aleatorios()` coloca todos los barcos eligiendo posición y
orientación al azar. Si no encuentra sitio, vuelve a probar.

### Disparos

`recibir_disparo()` valida las coordenadas y evita disparos repetidos:

- devuelve `"agua"` si no alcanza ningún barco;
- devuelve `"tocado"` si alcanza una casilla de barco;
- devuelve `False` si el disparo no es válido.

`comprobar_hundimiento()` revisa si todas las casillas de un barco han sido
alcanzadas. Entonces añade el barco a `barcos_hundidos`.

`comprobar_fin_partida()` devuelve `True` cuando todos los barcos están
colocados y han sido completamente hundidos.

### Mostrar el tablero

`mostrar()` dibuja las casillas en la consola. Las columnas se identifican con
letras y las filas con números.

Con `ocultar_barcos=True`, los barcos sin tocar no se muestran. Así el jugador
puede ver el tablero enemigo sin conocer sus posiciones.

