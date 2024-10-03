class Cola:
    def __init__(self):
        self.items = []

    def estaVacia(self):
        return self.items == []

    def insertar(self, item):
        self.items.insert(0,item)

    def quitar(self):
        return self.items.pop()

    def tamano(self):
        return len(self.items)
    
    def existe_elemento(self,elemento):
        return elemento in self.items