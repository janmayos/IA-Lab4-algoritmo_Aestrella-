from Cola import Cola
from Pila import Pila
from Lista import Lista

def mostrar_puzzle(puzzle):
    print(puzzle)

def crear_puzzle():
    puzzle = [1,3,2,4]
    #puzzle = [2,1,3,4]
    return puzzle

def mov_derecha(puzzle):
    nodo_hijo = []
    for elemento in puzzle:
        nodo_hijo.append(elemento)
    auxvalorx = nodo_hijo[3]
    auxvalory = nodo_hijo[2]
    nodo_hijo[3] = auxvalory
    nodo_hijo[2] = auxvalorx
    return nodo_hijo

def mov_izquierda(puzzle):    
    nodo_hijo = []
    for elemento in puzzle:
        nodo_hijo.append(elemento)
    auxvalorx = nodo_hijo[0]
    auxvalory = nodo_hijo[1]
    nodo_hijo[0] = auxvalory
    nodo_hijo[1] = auxvalorx
    return nodo_hijo

def mov_centro(puzzle):
    nodo_hijo = []
    for elemento in puzzle:
        nodo_hijo.append(elemento)
    auxvalorx = nodo_hijo[1]
    auxvalory = nodo_hijo[2]
    nodo_hijo[1] = auxvalory
    nodo_hijo[2] = auxvalorx
    return nodo_hijo

def alforitmo_dfs(puzzle):
    nodo_inicial = puzzle
    nodo_frontera = Cola()
    nodos_visitados = Lista()
    nodo_frontera.insertar(nodo_inicial)

    while not nodo_frontera.estaVacia():
        nodo_actual = nodo_frontera.quitar()
        #print(nodo_actual)
        #print(nodos_visitados)
        nodos_visitados.push(nodo_actual)

        if nodo_actual == [1,2,3,4]:
            nodos_visitados.imprimir_lista()
            return "Ya esta solucionado"
        
        
        nodo_hijo = mov_derecha(nodo_actual)
        
        if not nodos_visitados.existe_elemento(nodo_hijo) and not nodo_frontera.existe_elemento(nodo_hijo):
            #mostrar_puzzle(nodo_hijo)
            nodo_frontera.insertar(nodo_hijo)
        del(nodo_hijo)
        nodo_hijo = mov_centro(nodo_actual)
        if  not nodos_visitados.existe_elemento(nodo_hijo) and not nodo_frontera.existe_elemento(nodo_hijo):
            #mostrar_puzzle(nodo_hijo)
            nodo_frontera.insertar(nodo_hijo)
        del(nodo_hijo)
        nodo_hijo = mov_izquierda(nodo_actual)
        if not nodos_visitados.existe_elemento(nodo_hijo) and not nodo_frontera.existe_elemento(nodo_hijo): 
            #mostrar_puzzle(nodo_hijo)
            nodo_frontera.insertar(nodo_hijo)
        
        
def run_puzzle():
    puzzle = crear_puzzle()
    mostrar_puzzle(puzzle)
    print(alforitmo_dfs(puzzle))
    

if __name__ == '__main__':
    run_puzzle()
    
    #nodo_hijo  = mov_centro(puzzle)
    #mostrar_puzzle(nodo_hijo)

    

