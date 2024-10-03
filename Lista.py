class Lista:
    def __init__(self):
        self.items = []

    def estaVacia(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()
    
    def buscar_pos(self,pos):
        if len(self.items <= pos):
            return self.items[pos]
        return None

    def tamano(self):
        return len(self.items)
    
    def existe_elemento(self,elemento):
        
        return elemento in self.items
    def imprimir_lista(self):
        print(self.items)