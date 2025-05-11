# Pila (LIFO)
class Pila:
    def __init__(self):
        self.items = []
    
    def apilar(self, item):
        self.items.append(item)
    
    def desapilar(self):
        if not self.esta_vacia():
            return self.items.pop()
        else:
            print("La pila está vacía.")
    
    def esta_vacia(self):
        return len(self.items) == 0

    def mostrar(self):
        print("Pila (LIFO):", self.items)


# Cola (FIFO)
class Cola:
    def __init__(self):
        self.cola = []
    
    def encolar(self, item):
        self.cola.append(item)
    
    def desencolar(self):
        if not self.esta_vacia():
            return self.cola.pop(0)
        else:
            print("La cola está vacía.")
    
    def esta_vacia(self):
        return len(self.cola) == 0

    def mostrar(self):
        print("Cola (FIFO):", self.cola)


# ==== PRUEBA DE USO ====
if __name__ == "__main__":
    # Prueba de Pila (LIFO)
    print("== Prueba de Pila (LIFO) ==")
    p = Pila()
    p.apilar(10)
    p.apilar(20)
    p.apilar(30)
    p.desapilar()  # Elimina el 30
    p.mostrar()

    # Prueba de Cola (FIFO)
    print("\n== Prueba de Cola (FIFO) ==")
    c = Cola()
    c.encolar("A")
    c.encolar("B")
    c.encolar("C")
    c.desencolar()  # Elimina el "A"
    c.mostrar()
