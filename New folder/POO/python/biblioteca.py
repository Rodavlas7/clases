class Libro():
    def __init__(self, titulo, autor):
        self.__Titulo = titulo    
        self.__Autor = autor

    @property
    def Titulo(self):
        return self.__Titulo
    
    @property 
    def Autor(self):
        return self.__Autor
    
    @Titulo.setter
    def Titulo(self, Titulo):
        self.__Titulo = Titulo

    @Autor.setter
    def Autor(self, Autor):
        self.__Autor = Autor

    def Mostrar(self):
        print(f"{self.__Titulo} escrito por {self.__Autor}")

class Biblioteca():
    def __init__(self, nombre):
        self.__Nombre = nombre
        self.__libros = []

    @property
    def Nombre(self):
        return self.__Nombre
    
    @Nombre.setter
    def Nombre(self, nombre):
        self.__Nombre = nombre

    def AgregarLibro(self, Libro):
        self.__libros.append(Libro)

    def VerLibros(self):
        print(f"Libros en la biblioteca '{self.__Nombre}':\n")
        for r in self.__libros:
            r.Mostrar()


biblioteca = Biblioteca("Black Library")

libro1 = Libro("Horus Rising", "Dan Abnett")
libro2 = Libro("False Gods", "Graham McNeill")
libro3 = Libro("Galaxy in Flames", "Ben Counter")
libro4 = Libro("The First Heretic", "Aaron Dembski-Bowden")
libro5 = Libro("Know No Fear", "Dan Abnett")

biblioteca.AgregarLibro(libro1)
biblioteca.AgregarLibro(libro2)
biblioteca.AgregarLibro(libro3)
biblioteca.AgregarLibro(libro4)
biblioteca.AgregarLibro(libro5)

biblioteca.VerLibros()