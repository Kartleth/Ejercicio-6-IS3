# Función para imprimir el tablero del juego
def imprimir_tablero(tablero):
    print("-------------")
    for fila in tablero:
        print("| " + " | ".join(fila) + " |")
        print("-------------")

# Función para verificar si alguien ha ganado el juego
def verificar_ganador(tablero, jugador):
    # Verificar filas
    for fila in tablero:
        if all([celda == jugador for celda in fila]):
            return True

    # Verificar columnas
    for i in range(3):
        if all([fila[i] == jugador for fila in tablero]):
            return True

    # Verificar diagonales
    if all([tablero[i][i] == jugador for i in range(3)]) or all([tablero[i][2 - i] == jugador for i in range(3)]):
        return True

    return False

# Función principal del juego
def juego_gato():
    tablero = [[" " for _ in range(3)] for _ in range(3)]
    jugadores = ["X", "O"]
    turno = 0

    while True:
        jugador_actual = jugadores[turno % 2]
        imprimir_tablero(tablero)
        fila = int(input(f"Jugador {jugador_actual}, ingresa el número de fila (0, 1, 2): "))
        columna = int(input(f"Jugador {jugador_actual}, ingresa el número de columna (0, 1, 2): "))

        if tablero[fila][columna] == " ":
            tablero[fila][columna] = jugador_actual
            if verificar_ganador(tablero, jugador_actual):
                imprimir_tablero(tablero)
                print(f"¡Jugador {jugador_actual} ha ganado!")
                break
            turno += 1
        else:
            print("¡Esa casilla ya está ocupada! Inténtalo de nuevo.")

# Llamar a la función principal del juego
juego_gato()