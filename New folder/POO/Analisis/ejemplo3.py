class Producto:
    def __init__(self, id_producto, nombre, precio, disponible):
        self.__Id = id_producto
        self.__Nombre = nombre
        self.__Precio = precio
        self.__Disponible = disponible

    def EstaDisponible(self):
        return self.__Disponible

    def Precio(self):
        return self.__Precio

class Carrito:
    def __init__(self):
        self.__Productos = []

    def AgregarProducto(self, producto):
        if producto.EstaDisponible():
            self.__Productos.append(producto)

    def EliminarProducto(self, id_producto):
        for p in self.__Productos:
            if p._Producto__Id == id_producto:
                self.__Productos.remove(p)
                break

    def ConsultarTotal(self):
        total = 0
        for p in self.__Productos:
            total += p.Precio()
        return total

    def VaciarCarrito(self):
        self.__Productos.clear()


p1 = Producto(1, "Pringles", 50, True)
p2 = Producto(2, "DVD Batman", 500, True)
p3 = Producto(3, "Miel", 60, False)


carrito = Carrito()

carrito.AgregarProducto(p1)
carrito.AgregarProducto(p2)
carrito.AgregarProducto(p3)

print(carrito.ConsultarTotal())  

carrito.EliminarProducto(1)
print(carrito.ConsultarTotal())  

carrito.VaciarCarrito()
print(carrito.ConsultarTotal()) 
