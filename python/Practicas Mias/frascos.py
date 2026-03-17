from colorama import init, Fore, Back, Style

print("⬤")

#Juegos de los frascos de colores usando pilas

class Bola:
    def __init__(self, color):
        self.__color = color

class Frasco:
    def __init__(self, capacidad):
        self.__capacidad = capacidad
        self.__contenido = []

    @property
    def capacidad(self):
        return self.__capacidad
    
    @capacidad.setter
    def capacidad(self, capacidad):
        self.__capacidad =  capacidad

    def agregar_contenido(self, bola):
        return