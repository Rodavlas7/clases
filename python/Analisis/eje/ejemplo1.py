class Libro:
    def __init__(self, id_libro, titulo, autor):
        self.__Id = id_libro
        self.__Titulo = titulo
        self.__Autor = autor
        self.__Reservado = False

    @property
    def Disponible(self):
        return not self.__Reservado

    def Reservar(self):
        if not self.__Reservado:
            self.__Reservado = True

    def CancelarReserva(self):
        self.__Reservado = False


class Biblioteca:
    def __init__(self):
        self.__Libros = []

    def AgregarLibro(self, libro):
        self.__Libros.append(libro)

    def ReservarLibro(self, id_libro):
        for libro in self.__Libros:
            if libro.Id == id_libro:
                libro.Reservar()

    def ConsultarDisponibilidad(self, id_libro):
        for libro in self.__Libros:
            if libro.Id == id_libro:
                return libro.Disponible

    def CancelarReserva(self, id_libro):
        for libro in self.__Libros:
            if libro.Id == id_libro:
                libro.CancelarReserva()


libro = Libro(1, "El Fin y la guerra, I", "Dan Abnett")

print(libro.Disponible)
libro.Reservar()
print(libro.Disponible)
libro.CancelarReserva()
print(libro.Disponible)
