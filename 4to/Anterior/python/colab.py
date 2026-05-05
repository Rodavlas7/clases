class Rol():
    def __init__(self, nombre):
        self.__nombre = nombre
    
    @property
    def Nombre(self):
        return self.__nombre
    
    @Nombre.setter
    def Nombre(self, Nombre):
        self.__nombre = Nombre

    def __str__(self):
        return f"El rol es {self.__nombre}"

class Colaborador():
    def __init__(self, nombre):
        self.__nombre = nombre
    
    @property
    def Nombre(self):
        return self.__nombre
    
    @Nombre.setter
    def Nombre(self, Nombre):
        self.__nombre = Nombre

    def __str__(self):
        return f"El colabora se llama {self.__nombre}"
    

class Proyecto():
    def __init__(self, Nombre):
        self.__nombre = Nombre
        self.__integrantes = []
        self.__roles = []

    @property
    def Nombre(self):
        return self.__nombre
    
    @Nombre.setter
    def Nombre(self, Nombre):
        self.__nombre = Nombre

    def AgregarColaborador(self, Colaborador, Rol):
        self.__integrantes.append(Colaborador)
        self.__roles.append(Rol)
    
    def MostrarColaboradores(self):
            print(f"Proyecto: {self.__nombre}")
            for i in range(len(self.__integrantes)):
                print(f"{self.__integrantes[i].Nombre} con el rol de {self.__roles[i].Nombre}")


'''
Gestión de Proyecto con Colaboradores Externos
Objetivo: Diseñar una estructura en Python que modele un proyecto institucional que involucra colaboradores externos. 
El sistema debe permitir registrar proyectos, asignar colaboradores, definir roles, y visualizar la relación entre el proyecto y sus 
participantes.

Contexto: Este modelo puede aplicarse a iniciativas académicas, tecnológicas o de innovación donde se integran expertos externos, 
instituciones aliadas o consultores. Se busca representar la composición del equipo, sus funciones y el vínculo con el proyecto.

Requisitos:
Crear clases para Proyecto, Colaborador, y Rol.
Permitir agregar colaboradores externos a un proyecto.
Asociar cada colaborador con un rol específico dentro del proyecto.
Mostrar un resumen del proyecto con sus colaboradores y roles.
'''