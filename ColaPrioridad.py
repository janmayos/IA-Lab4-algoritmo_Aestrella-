class ColaPrioridad:
    def __init__(self):
        self.items = []

    def estaVacia(self):
        return len(self.items) == 0

    def insertar(self, item, prioridad):
        """Inserta un elemento con su prioridad en la cola."""
        # Agregar el elemento como una tupla (item, prioridad)
        self.items.append((item, prioridad))
        # Ordenar los elementos según la prioridad
        self.ordenar()

    def quitar(self):
        """Elimina y retorna el elemento de mayor prioridad."""
        if not self.estaVacia():
            # Quitar el primer elemento, ya que está ordenado por prioridad (ascendente)
            return self.items.pop(0)
        else:
            return None

    def tamano(self):
        return len(self.items)

    def existe_elemento(self, elemento):
        """Verifica si un elemento existe en la cola (sin tener en cuenta la prioridad)."""
        return any(item == elemento for item, _ in self.items)
    
    def obtener_coste(self,elemento):
        for item,coste in self.items:
            if item == elemento:
                return coste
        return None

    def sustituir_coste(self,elemento,coste):
        for i, tupla in enumerate(self.items):
            if tupla[0] == elemento:
                indice = i
            break  # Salir del bucle al encontrar el primer índice que coincida
        self.items[indice] = (elemento,coste)
                
        

    def ordenar(self):
        """Ordena la cola por prioridad en orden ascendente (mayor prioridad primero)."""
        # Ordenar por la segunda parte de la tupla que es la prioridad self.items.sort(key=lambda x: x[1])
        self.items.sort(key=lambda x: x[1])
        

    def mostrar(self):
        """Muestra la cola de prioridad."""
        print(self.items)
        



