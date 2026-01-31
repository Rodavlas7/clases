class Estudiante:
    def __init__(self, nombre, calificacion):
        self.__nombre = nombre
        self.__calificacion = calificacion


    @property
    def nombre(self):
        return self.__nombre
    
    @property
    def calificacion(self):
        return self.__calificacion


    @nombre.setter
    def nombre(self, nuevo_nombre):
        if nuevo_nombre.strip() != "":
            self.__nombre = nuevo_nombre
        else:
            print("Error: nombre inválido")

    @calificacion.setter
    def calificacion(self, nueva_calificacion):
        if 0 <= nueva_calificacion <= 100:
            self.__calificacion = nueva_calificacion
        else:
            print("La calificación debe estar entre 0 y 100")

    def aprobado(self):
        return self.__calificacion > 85
