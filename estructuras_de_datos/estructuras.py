
class MiLista:
    def __init__(self):
        self.lista = []

    def agregar(self, elemento):
        self.lista.append(elemento)

    def eliminar(self, elemento):
        if elemento in self.lista:
            self.lista.remove(elemento)
        else:
            print(f"{elemento} no encontrado en la lista.")

    def mostrar(self):
        print("Lista actual:", self.lista)


def menu():
    mi_lista = MiLista()
    
    while True:
        print("\n--- MENÚ ---")
        print("1. Agregar elemento")
        print("2. Eliminar elemento")
        print("3. Mostrar lista")
        print("4. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            valor = input("Ingresa el elemento a agregar: ")
            mi_lista.agregar(valor)
            print(f"'{valor}' agregado.")
        elif opcion == "2":
            valor = input("Ingresa el elemento a eliminar: ")
            mi_lista.eliminar(valor)
        elif opcion == "3":
            mi_lista.mostrar()
        elif opcion == "4":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida, intenta de nuevo.")

# Ejecutar menú
if __name__ == "__main__":
    menu()
