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
  

    # Verificar diagonales
    if all([tablero[i][i] == jugador for i in range(3)]) or all([tablero[i][2 - i] == jugador for i in range(3)]):
        return True

    return False

# Función principal del juego
def juego_gato():
    tablero = [[" " for _ in range(3)] for _ in range(3)]
    jugadores = ["X", "O"]
    turno = 0

    

# Llamar a la función principal del juego
juego_gato()