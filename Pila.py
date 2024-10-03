class Pila:
     def __init__(self):
         self.items = []

     def estaVacia(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def inspeccionar(self):
         return self.items[len(self.items)-1]

     def tamano(self):
         return len(self.items)
     
     def existe_elemento(self,elemento):
         return elemento in self.items
        
     def imprimir_pila(self):
        print(self.items)