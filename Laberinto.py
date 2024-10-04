from ColaPrioridad import ColaPrioridad
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

def generar_laberinto_grande():

    maze = [
        [0, 0, 1, 1, 1, 1, 0, 1, 1, 1],
        [1, 0, 0, 0, 1, 1, 0, 0, 0, 1],
        [1, 1, 1, 0, 1, 1, 1, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
        [1, 0, 0, 0, 1, 1, 0, 0, 0, 1],
        [1, 1, 1, 0, 1, 1, 1, 1, 0, 1],
        [1, 0, 1, 1, 1, 1, 0, 1, 0, 1],
        [1, 0, 0, 0, 1, 1, 0, 0, 0, 1],
        [1, 0, 0, 0, 1, 1, 0, 0, 0, 0]
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
    if nodo_hijo[1] >= 0 and nodo_hijo[1]<len(laberinto[0]):
        if laberinto[nodo_hijo[0]][nodo_hijo[1]] != 1:
            return nodo_hijo
    return None

def mov_izquierda(start_nodo,laberinto):    
    nodo_hijo = (start_nodo[0],start_nodo[1]-1)
    if nodo_hijo[1] >= 0 and nodo_hijo[1]<len(laberinto[0]):
        if laberinto[nodo_hijo[0]][nodo_hijo[1]] != 1:
            return nodo_hijo
    return None

def mov_arriba(start_nodo,laberinto):    
    nodo_hijo = (start_nodo[0]-1,start_nodo[1])
    if nodo_hijo[0] >= 0 and nodo_hijo[0]<len(laberinto):
        if laberinto[nodo_hijo[0]][nodo_hijo[1]] != 1:
            return nodo_hijo
    return None

def mov_abajo(start_nodo,laberinto):    
    nodo_hijo = (start_nodo[0]+1,start_nodo[1])
    if nodo_hijo[0] >= 0 and nodo_hijo[0]<len(laberinto):
        if laberinto[nodo_hijo[0]][nodo_hijo[1]] != 1:
            return nodo_hijo
    return None

def es_solucion(start_mov,end):
    return start_mov == end

def heuristica(nodo_actual, meta):
    """Calcula la distancia Manhattan entre dos puntos a y b."""
    return abs(nodo_actual[0] - meta[0]) + abs(nodo_actual[1] - meta[1])

def recalcular_coste_nodos(nodo_frontera,nuevocosto,end):
    #print("Nuevo costo")
    #nodo_frontera.mostrar()
    nodo_frontera_aux = ColaPrioridad()
    while not nodo_frontera.estaVacia():
        #print("Aqui")
        nodo_actual = nodo_frontera.quitar()
        prioridad = nuevocosto + heuristica(nodo_actual[0], end)
        nodo_frontera_aux.insertar(nodo_actual[0],prioridad)
    while not nodo_frontera_aux.estaVacia():
        nodo_actual = nodo_frontera_aux.quitar()
        nodo_frontera.insertar(nodo_actual[0],nodo_actual[1])

def alforitmo_a_estrella(laberinto,start,end):
    nodo_inicial = start
    nodo_frontera = ColaPrioridad()
    nodos_visitados = Lista()
    nodo_frontera.insertar(nodo_inicial,0)
    nuevo_costo = 1
    while not nodo_frontera.estaVacia():
        #Calcular el valor F(n) = g(n)+h(n) para cada nodo frontera
        #Ordenar la lista nodos_frontera según f(n)
        if not nodo_frontera.estaVacia(): 
            recalcular_coste_nodos(nodo_frontera,0,end)
        nodo_frontera.ordenar()

        nodo_actual = nodo_frontera.quitar()
        #print(nodo_actual)
        #nodos_visitados.imprimir_lista()
        nodos_visitados.push(nodo_actual[0])
        
        if es_solucion(nodo_actual[0],end):
            nodos_visitados.imprimir_lista()
            return "Ya esta solucionado"
        
    
        nodo_hijo = mov_derecha(nodo_actual[0],laberinto)
        
        nuevo_costo += 1  # Asumiendo que el costo de cada movimiento es 1
        
        if  nodo_hijo != None and not nodos_visitados.existe_elemento(nodo_hijo):
            if nodo_frontera.existe_elemento(nodo_hijo):
                #si coste de nodo_hijo < nodo en nodos_frontera:
                if nuevo_costo < nodo_frontera.obtener_coste(nodo_hijo):
                #Sustituir nodo_hijo en nodos frontera
                    prioridad = nuevo_costo + heuristica(nodo_hijo, end)
                    nodo_frontera.sustituir_coste(nodo_hijo,prioridad)
            else:
                prioridad = nuevo_costo + heuristica(nodo_hijo, end)
                nodo_frontera.insertar(nodo_hijo,prioridad)

        del(nodo_hijo)

        nuevo_costo += 1
        nodo_hijo = mov_izquierda(nodo_actual[0],laberinto)
        if  nodo_hijo != None and not nodos_visitados.existe_elemento(nodo_hijo):
            
            if nodo_frontera.existe_elemento(nodo_hijo):
                #si coste de nodo_hijo < nodo en nodos_frontera:
                if nuevo_costo < nodo_frontera.obtener_coste(nodo_hijo):
                #Sustituir nodo_hijo en nodos frontera
                    nodo_frontera.sustituir_coste(nodo_hijo,nuevo_costo)
            else:
                nodo_frontera.insertar(nodo_hijo,nuevo_costo)
        del(nodo_hijo)
        nuevo_costo += 1
        nodo_hijo = mov_arriba(nodo_actual[0],laberinto)
        if  nodo_hijo != None and not nodos_visitados.existe_elemento(nodo_hijo):
            if nodo_frontera.existe_elemento(nodo_hijo):
                #si coste de nodo_hijo < nodo en nodos_frontera:
                if nuevo_costo < nodo_frontera.obtener_coste(nodo_hijo):
                #Sustituir nodo_hijo en nodos frontera
                    nodo_frontera.sustituir_coste(nodo_hijo,nuevo_costo)
            else:
                nodo_frontera.insertar(nodo_hijo,nuevo_costo)
        del(nodo_hijo)
        nuevo_costo += 1
        nodo_hijo = mov_abajo(nodo_actual[0],laberinto)
        #print(nodo_hijo)
        #nodos_visitados.imprimir_lista()
        if  nodo_hijo != None and not nodos_visitados.existe_elemento(nodo_hijo):
            
            if nodo_frontera.existe_elemento(nodo_hijo):
                #si coste de nodo_hijo < nodo en nodos_frontera:
                if nuevo_costo < nodo_frontera.obtener_coste(nodo_hijo):
                #Sustituir nodo_hijo en nodos frontera
                    nodo_frontera.sustituir_coste(nodo_hijo,nuevo_costo)
            else:
                
                nodo_frontera.insertar(nodo_hijo,nuevo_costo)
        #nodo_frontera.mostrar()
        #input("ciclo: ")
        #nodo_frontera.mostrar()
        

def run_laberinto():
    # Posición de inicio y salida
    start =  (0, 1)  # Coordenadas (fila, columna) de inicio
    end = (3, 4)    # Coordenadas (fila, columna) de salida
    laberinto = generar_laberinto()
    mostrar_laberinto(laberinto)
    if validar_posiciones_entrada_salida(laberinto,start,end):
        print("Empezamos")
        valores = alforitmo_a_estrella(laberinto,start,end)
        if valores != None:
            print(valores)
        else:
            print("No hay camino hacia la meta")
    else:
        print("Modificar valores de start y end")

def run_laberinto_grande():
    # Posición de inicio y salida
    start =  (0,0)# (0, 1)  # Coordenadas (fila, columna) de inicio
    end = (9,9) #(3, 4)    # Coordenadas (fila, columna) de salida
    laberinto = generar_laberinto_grande()
    mostrar_laberinto(laberinto)
    if validar_posiciones_entrada_salida(laberinto,start,end):
        print("Empezamos")
        valores = alforitmo_a_estrella(laberinto,start,end)
        if valores != None:
            print(valores)
        else:
            print("No hay camino hacia la meta")
    else:
        print("Modificar valores de start y end")


if __name__ == '__main__':
    run_laberinto()        
