class Autor:
    def __init__(self, Nombre, Nacionalidad):
        self.__nombre = Nombre
        self.__nacion = Nacionalidad

    @property
    def Nombre(self):
        return self.__nombre
    
    @property
    def Nacion(self):
        return self.__nacion

    @Nombre.setter
    def Nombre(self, Nombre):
        self.__nombre = Nombre

    @Nacion.setter
    def Nacion(self, Nacionalidad):
        self.__nacion = Nacionalidad

    def __str__(self):
        return f"autor {self.__nombre} de {self.__nacion}"
    
class Libro:
    def __init__(self, Titulo, Autor, ISBN):
        self.__titulo = Titulo
        self.__autor = Autor
        self.__isbn = ISBN

    @property
    def Titulo(self):
        return self.__titulo
    
    @property
    def Autor(self):
        return self.__autor

    @property
    def ISBN(self):
        return self.__isbn

    @Titulo.setter
    def Nombre(self, Titulo):
        self.__titulo = Titulo

    @Autor.setter
    def Autor(self, Autor):
        self.__autor = Autor

    @ISBN.setter
    def ISBN(self, ISBN):
        self.__isbn = ISBN

    def __str__(self):
        return f"libro {self.__titulo} escrito por el {self.__autor}, con ISBN de {self.__isbn}"
    
class Biblioteca:
    def __init__(self, Nombre):
        self.__nombre = Nombre
        self.__libros = []

    @property
    def Nombre(self):
        return self.__nombre
    
    @Nombre.setter
    def Nombre(self, Nombre):
        self.__nombre = Nombre

    def agregar_libro(self, Libro):
        self.__libros.append(Libro)
    
    def eliminar_libro(self, isbn):
        encontrado = False
        for l in self.__libros:
            if l.ISBN == isbn:
                self.__libros.remove(l)
                encontrado = True
                print(f"Libro con el ISBN {isbn} eliminado")
        if not encontrado:    
            print(f"No se encontro libro con el ISBN {isbn}")
    
    def buscar_autor(self, nombre_autor):

        if len(self.__libros) == 0:
            print("No hay libros para buscar")
            return
        
        encontrado = False
        
        print(f"Libros de {nombre_autor}")

        for l in self.__libros:
            if l.Autor.Nombre == nombre_autor:
                print(f"{l}")
                encontrado = True

        if not encontrado:
            print(f"No hay libros con el autor {nombre_autor}")
        

    def catalogo(self):
        
        if len(self.__libros) == 0:
            print (f"No hay libros para en la biblioteca {self.__nombre}")
            return

        print(f"Libro en la biblioteca {self.__nombre}")
        for lib in self.__libros:
            print(f"- {lib}")



A1 = Autor("Jose", "Chile")
A2 = Autor("Graham Mcneill" , "Inglaterra")

L1 = Libro("Jujui" , A1, "123")
L2 = Libro("Fin y la guerra",A2, "321")
L3 = Libro("Sol negro", A2, "312")

B = Biblioteca("San Perez del Olmo")

B.catalogo()

print("\n")

B.agregar_libro(L1)
B.agregar_libro(L2)
B.agregar_libro(L3)

B.catalogo()

print("\n")

B.buscar_autor("Jose")

print("\n")

B.eliminar_libro("123")

print("\n")

B.catalogo()