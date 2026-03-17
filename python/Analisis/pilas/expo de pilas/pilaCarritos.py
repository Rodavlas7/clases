class PilaCarritos:

    def __init__(self, capacidad):
        self.capacidad = capacidad
        self.pila = []
        self.tope = -1

    def esta_vacia(self):
        return self.tope == -1

    def esta_llena(self):
        return self.tope == self.capacidad - 1

    def push(self, carrito):
        if self.esta_llena():
            return False
        else:
            self.pila.append(carrito)
            self.tope += 1
            return True

    def pop(self):
        if self.esta_vacia():
            return None
        else:
            self.tope -= 1
            return self.pila.pop()

    def mostrar(self):
        if self.esta_vacia():
            print("No hay carritos registrados.")
        else:
            for c in self.pila:
                print(c)

    def total(self):
        return len(self.pila)