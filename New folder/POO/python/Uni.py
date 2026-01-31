class Profesor:
    def __init__(self, nombre, materia):
        self.__Nombre = nombre
        self.__Materia = materia

    @property
    def Nombre(self):
        return self.__Nombre

    @property
    def Materia(self):
        return self.__Materia

    @Nombre.setter
    def Nombre(self, nombre):
        self.__Nombre = nombre

    @Materia.setter
    def Materia(self, materia):
        self.__Materia = materia

    def Mostrar(self):
        print(f"Profesor: {self.__Nombre} | Materia: {self.__Materia}")


class Universidad:
    def __init__(self, nombre):
        self.__Nombre = nombre
        self.__profesores = []

    @property
    def Nombre(self):
        return self.__Nombre

    @Nombre.setter
    def Nombre(self, nombre):
        self.__Nombre = nombre

    def AgregarProfesor(self, profesor):
        self.__profesores.append(profesor)

    def VerProfesores(self):
        print(f"Profesores en la Universidad '{self.__Nombre}':\n")
        for p in self.__profesores:
            p.Mostrar()


def main():
    prof1 = Profesor("Ana Pérez", "Programación Orientada a Objetos")
    prof2 = Profesor("Carlos Gómez", "Bases de Datos")
    prof3 = Profesor("Lucía Torres", "Redes de Computadoras")
    prof4 = Profesor("Miguel Ramírez", "Sistemas Operativos")
    prof5 = Profesor("Sofía Mendoza", "Desarrollo Web")

    universidad = Universidad("Universidad Tecnológica de Tijuana")

    universidad.AgregarProfesor(prof1)
    universidad.AgregarProfesor(prof2)
    universidad.AgregarProfesor(prof3)
    universidad.AgregarProfesor(prof4)
    universidad.AgregarProfesor(prof5)

    universidad.VerProfesores()


if __name__ == "__main__":
    main()
