from Cola import Cola
from Pila import Pila
from Lista import Lista

# Representación del laberinto

# 0 = camino, 1 = pared
def generar_laberinto():

    maze = [
        [1, 0, 1, 1, 1],
        [1, 0, 0, 0, 1],
        [1, 1, 1, 0, 1],
        [1, 0, 0, 0, 0],
        [1, 1, 1, 1, 1]
    ]

    return maze

def mostrar_laberinto(laberinto):
    for fila in laberinto:
        print(fila)

def validar_posiciones_entrada_salida(laberinto,start,end):
    if laberinto[start[0]][start[1]] == 1:
        print("Posición de inicio no valida es pared")
        return False
    if laberinto[end[0]][end[1]] == 1:
        print("Posición final no valida es pared")
        return False
    return True

def mov_derecha(start_nodo,laberinto):
    nodo_hijo = (start_nodo[0],start_nodo[1]+1)
    if nodo_hijo[1] >= 0 and nodo_hijo[1]<=len(laberinto[0]):
        if laberinto[nodo_hijo[0]][nodo_hijo[1]] != 1:
            return nodo_hijo
    return None

def mov_izquierda(start_nodo,laberinto):    
    nodo_hijo = (start_nodo[0],start_nodo[1]-1)
    if nodo_hijo[1] >= 0 and nodo_hijo[1]<=len(laberinto[0]):
        if laberinto[nodo_hijo[0]][nodo_hijo[1]] != 1:
            return nodo_hijo
    return None

def mov_arriba(start_nodo,laberinto):    
    nodo_hijo = (start_nodo[0]-1,start_nodo[1])
    if nodo_hijo[0] >= 0 and nodo_hijo[1]<=len(laberinto):
        if laberinto[nodo_hijo[0]][nodo_hijo[1]] != 1:
            return nodo_hijo
    return None

def mov_abajo(start_nodo,laberinto):    
    nodo_hijo = (start_nodo[0]+1,start_nodo[1])
    if nodo_hijo[0] >= 0 and nodo_hijo[1]<=len(laberinto):
        if laberinto[nodo_hijo[0]][nodo_hijo[1]] != 1:
            return nodo_hijo
    return None

def es_solucion(start_mov,end):
    return start_mov == end

def alforitmo_dfs(laberinto,start,end):
    nodo_inicial = start
    nodo_frontera = Cola()
    nodos_visitados = Lista()
    nodo_frontera.insertar(nodo_inicial)

    while not nodo_frontera.estaVacia():
        nodo_actual = nodo_frontera.quitar()
        #print(nodo_actual)
        #print(nodos_visitados)
        nodos_visitados.push(nodo_actual)
        if es_solucion(nodo_actual,end):
            nodos_visitados.imprimir_lista()
            return "Ya esta solucionado"
        
    
        nodo_hijo = mov_derecha(nodo_actual,laberinto)
        
        if nodo_hijo != None and not nodos_visitados.existe_elemento(nodo_hijo) and not nodo_frontera.existe_elemento(nodo_hijo):
            #mostrar_puzzle(nodo_hijo)
            nodo_frontera.insertar(nodo_hijo)
        del(nodo_hijo)
        nodo_hijo = mov_izquierda(nodo_actual,laberinto)
        if  nodo_hijo != None and  not nodos_visitados.existe_elemento(nodo_hijo) and not nodo_frontera.existe_elemento(nodo_hijo):
            #mostrar_puzzle(nodo_hijo)
            nodo_frontera.insertar(nodo_hijo)
        del(nodo_hijo)
        nodo_hijo = mov_arriba(nodo_actual,laberinto)
        if nodo_hijo != None and  not nodos_visitados.existe_elemento(nodo_hijo) and not nodo_frontera.existe_elemento(nodo_hijo): 
            #mostrar_puzzle(nodo_hijo)
            nodo_frontera.insertar(nodo_hijo)
        del(nodo_hijo)
        nodo_hijo = mov_abajo(nodo_actual,laberinto)

        if nodo_hijo != None and  not nodos_visitados.existe_elemento(nodo_hijo) and not nodo_frontera.existe_elemento(nodo_hijo): 
            #mostrar_puzzle(nodo_hijo)
            nodo_frontera.insertar(nodo_hijo)

def run_laberinto():
    # Posición de inicio y salida
    start = (0, 1)  # Coordenadas (fila, columna) de inicio
    end = (3, 4)    # Coordenadas (fila, columna) de salida
    laberinto = generar_laberinto()
    mostrar_laberinto(laberinto)
    if validar_posiciones_entrada_salida(laberinto,start,end):
        print("Empezamos")
        print(alforitmo_dfs(laberinto,start,end))
    else:
        print("Modificar valores de star y end")
    #print(alforitmo_dfs(puzzle))



if __name__ == '__main__':
    run_laberinto()        
