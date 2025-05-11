class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

class ArbolBinario:
    def __init__(self):
        self.raiz = None

    def insertar(self, valor):
        if self.raiz is None:
            self.raiz = Nodo(valor)
            print(f"Ingresado {valor} como raíz")
        else:
            self._insertar_recursivo(self.raiz, valor)

    def _insertar_recursivo(self, nodo, valor):
        # Si el valor es menor, insertamos en la izquierda
        if valor < nodo.valor:
            if nodo.izquierda is None:
                nodo.izquierda = Nodo(valor)
                print(f"Ingresado {valor} en el subárbol izquierdo de {nodo.valor}")
            else:
                self._insertar_recursivo(nodo.izquierda, valor)
        # Si el valor es mayor o igual, insertamos en la derecha
        else:
            if nodo.derecha is None:
                nodo.derecha = Nodo(valor)
                print(f"Ingresado {valor} en el subárbol derecho de {nodo.valor}")
            else:
                self._insertar_recursivo(nodo.derecha, valor)

    def preorden(self, nodo):
        """Recorrido Preorden (Raíz → Izquierda → Derecha)"""
        if nodo:
            print(nodo.valor, end=" ")
            self.preorden(nodo.izquierda)
            self.preorden(nodo.derecha)

    def inorden(self, nodo):
        """Recorrido Inorden (Izquierda → Raíz → Derecha)"""
        if nodo:
            self.inorden(nodo.izquierda)
            print(nodo.valor, end=" ")
            self.inorden(nodo.derecha)

    def postorden(self, nodo):
        """Recorrido Postorden (Izquierda → Derecha → Raíz)"""
        if nodo:
            self.postorden(nodo.izquierda)
            self.postorden(nodo.derecha)
            print(nodo.valor, end=" ")

    def mostrar_recorridos(self):
        print("\nRecorrido Preorden: ", end="")
        self.preorden(self.raiz)
        print("\nRecorrido Inorden: ", end="")
        self.inorden(self.raiz)
        print("\nRecorrido Postorden: ", end="")
        self.postorden(self.raiz)
        print()

# --- Programa interactivo ---
if __name__ == "__main__":
    arbol = ArbolBinario()

    # Insertando nodos
    for valor in [10, 5, 15, 3, 7, 12, 18, 2, 6,4]:
        arbol.insertar(valor)

    # Mostramos los recorridos
    arbol.mostrar_recorridos()
