import heapq

# Definir la heurística de Manhattan
def heuristica(a, b):
    """Calcula la distancia Manhattan entre dos puntos a y b."""
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

# Definir la función del algoritmo A*
def a_estrella(maze, start, end):
    """Implementación del algoritmo A* para encontrar el camino en un laberinto."""
    # Movimiento posible en 4 direcciones: arriba, abajo, izquierda, derecha
    movimientos = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    # Inicializar la cola de prioridad y agregar el nodo inicial con costo 0 y heurística calculada
    cola_prioridad = []
    heapq.heappush(cola_prioridad, (0, start))  # (prioridad, nodo)
    
    # Diccionarios para mantener el costo más bajo y la ruta hacia cada nodo
    g_cost = {start: 0}  # Costo desde el nodo inicial hasta el nodo actual
    padres = {start: None}  # Para reconstruir el camino

    while cola_prioridad:
        # Sacar el nodo con la menor prioridad de la cola
        _, nodo_actual = heapq.heappop(cola_prioridad)

        # Si hemos llegado a la posición de salida, reconstruir y retornar el camino
        if nodo_actual == end:
            camino = []
            while nodo_actual is not None:
                camino.append(nodo_actual)
                nodo_actual = padres[nodo_actual]
            return camino[::-1]  # Retornar el camino de inicio a fin

        # Explorar los nodos vecinos (arriba, abajo, izquierda, derecha)
        for mov in movimientos:
            # Calcular la posición del vecino
            vecino = (nodo_actual[0] + mov[0], nodo_actual[1] + mov[1])

            # Comprobar que el vecino esté dentro de los límites del laberinto y no sea una pared
            if 0 <= vecino[0] < len(maze) and 0 <= vecino[1] < len(maze[0]) and maze[vecino[0]][vecino[1]] == 0:
                # Calcular el costo g del vecino
                nuevo_costo = g_cost[nodo_actual] + 1  # Asumiendo que el costo de cada movimiento es 1

                # Si encontramos un camino más corto hacia el vecino o es un nodo nuevo
                if vecino not in g_cost or nuevo_costo < g_cost[vecino]:
                    g_cost[vecino] = nuevo_costo
                    prioridad = nuevo_costo + heuristica(vecino, end)  # f(n) = g(n) + h(n)
                    heapq.heappush(cola_prioridad, (prioridad, vecino))
                    padres[vecino] = nodo_actual

    return None  # Retornar None si no se encuentra un camino

# Definir el laberinto
maze = [
    [1, 0, 1, 1, 1],
    [1, 0, 0, 0, 1],
    [1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0],
    [1, 1, 1, 1, 1]
]

# Posiciones de inicio y fin
start = (0, 1)  # Coordenadas de inicio
end = (3, 4)    # Coordenadas de salida

# Ejecutar el algoritmo A* y obtener el camino
camino = a_estrella(maze, start, end)
if camino:
    print("Camino encontrado:", camino)
else:
    print("No se encontró un camino.")
