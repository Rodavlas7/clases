class Curso:
    def __init__(self, clave, nombre, max_alumnos):
        self.__Clave = clave
        self.__Nombre = nombre
        self.__MaxAlumnos = max_alumnos
        self.__Alumnos = []

    def InscribirAlumno(self, alumno):
        if len(self.__Alumnos) < self.__MaxAlumnos:
            if alumno not in self.__Alumnos:
                self.__Alumnos.append(alumno)

    def BajaAlumno(self, alumno):
        if alumno in self.__Alumnos:
            self.__Alumnos.remove(alumno)

    def CupoDisponible(self):
        return self.__MaxAlumnos - len(self.__Alumnos)



curso = Curso("ED4", "Estructura de datos para 4to", 16)

print(curso.CupoDisponible())  

curso.InscribirAlumno("Misael")
curso.InscribirAlumno("Fonseca")

print(curso.CupoDisponible())  

curso.BajaAlumno("Misael")
print(curso.CupoDisponible())  
