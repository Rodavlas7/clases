class Platillo:
    def __init__(self, nombre, precio, disponible):
        self.__Nombre = nombre
        self.__Precio = precio
        self.__Disponible = disponible

    def EstaDisponible(self):
        return self.__Disponible

    def Precio(self):
        return self.__Precio

class Pedido:
    def __init__(self):
        self.__Platillos = []
        self.__Estado = "abierto"

    def AgregarPlatillo(self, platillo):
        if self.__Estado == "abierto" and platillo.EstaDisponible():
            self.__Platillos.append(platillo)

    def EliminarPlatillo(self, nombre):
        if self.__Estado == "abierto":
            for p in self.__Platillos:
                if p._Platillo__Nombre == nombre:
                    self.__Platillos.remove(p)
                    break

    def CalcularTotal(self):
        total = 0
        for p in self.__Platillos:
            total += p.Precio()
        return total

    def CerrarPedido(self):
        if self.__Estado == "abierto":
            self.__Estado = "cerrado"


p1 = Platillo("Taco de Asada", 35, True)
p2 = Platillo("Refresco", 30, True)

pedido = Pedido()

pedido.AgregarPlatillo(p1)
pedido.AgregarPlatillo(p1)
pedido.AgregarPlatillo(p1)
pedido.AgregarPlatillo(p2)

print(pedido.CalcularTotal()) 

pedido.EliminarPlatillo("Taco de Asada")
print(pedido.CalcularTotal()) 

pedido.CerrarPedido()
