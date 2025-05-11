
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

# Pila (LIFO)
class Pila:
    def __init__(self):
        self.pila = []

    def apilar(self, item):
        self.pila.append(item)
    
    def desapilar(self):
        if not self.esta_vacia():
            return self.pila.pop()
        else:
            print("La pila está vacía.")

    def esta_vacia(self):
        return len(self.pila) == 0

    def mostrar(self):
        print("Pila (LIFO):", self.pila)

# ==== PRUEBA DE USO ====
if __name__ == "__main__":
    print("== Prueba de Cola (FIFO) ==")
    c = Cola()
    c.encolar("A")
    c.encolar("B")
    c.encolar("C")
    c.desencolar()
    c.mostrar()

    print("\n== Prueba de Pila (LIFO) ==")
    p = Pila()
    p.apilar(1)
    p.apilar(2)
    p.apilar(3)
    p.desapilar()
    p.mostrar()
