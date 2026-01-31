class Habitacion():
    def __init__(self, Nombre, Area):
        self.__nombre = Nombre

        if float(Area) <= 0:
            self.__area = 1
        
        self.__area = float(Area)

    @property
    def Nombre(self):
        return self.__nombre
    
    @property
    def Area(self):
        return self.__area

    @Area.setter
    def Area(self, Nombre):
        self.__nombre = Nombre

    @Area.setter
    def Area(self, Area):
        self.__area = Area

    def __str__(self):
        return f"habitacion {self.__nombre} con {self.__area} m2"

class Casa:
    def __init__(self, Direccion):
        self.__direccion = Direccion
        self.__habitaciones = []

    @property
    def Direccion(self):
        return self.__direccion
    
    @Direccion.setter
    def Direccion(self, Direccion):
        self.__direccion =  Direccion

    def agregar_habitacion(self, Nombre, Area):
        self.__habitaciones.append(Habitacion(Nombre, Area))

    def calcular_area(self):
        if len(self.__habitaciones) == 0:
            print(f"No hay habitaciones para medir el area")
        
        total = 0

        for h in self.__habitaciones:
            total += h.Area
        return total
    
    def Habitaciones(self):
        if len(self.__habitaciones) == 0:
            print(f"No hay habitaciones en la casa")
            return

        for h in self.__habitaciones:
            print(f"{h}")

    def __str__(self):
        return f"casa en {self.__direccion}"

    def __del__(self):
        print(f"Eliminando {self}")
        self.__habitaciones.clear()

c = Casa("Indepencia #7")
c.agregar_habitacion("Cocina",15)
c.agregar_habitacion("Baño",5)
c.agregar_habitacion("Habitacion",10)

c.Habitaciones()

print(c.calcular_area())

c.__del__()

c.Habitaciones()