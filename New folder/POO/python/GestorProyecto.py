class Rol:
    def __init__(self, nombre):
        self.__nombre = nombre

    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    def __str__(self):
        return self.__nombre


class Colaborador:
    def __init__(self, nombre):
        self.__nombre = nombre
    
    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre
    
    def __str__(self):
        return f"Colaborador: {self.__nombre}"


class Proyecto:
    def __init__(self, nombre):
        self.__nombre = nombre
        self.__colaboradores = []
        self.__roles = []
    
    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    def agregarColaborador(self, colaborador, rol):
        self.__colaboradores.append(colaborador)
        self.__roles.append(rol)

    def __str__(self):
        if self.__colaboradores == []:
            return f"Proyecto: {self.__nombre} (sin colaboradores)"
        
        texto = f"Proyecto: {self.__nombre}\nColaboradores:\n"
        for i in range(len(self.__colaboradores)):
            texto += f"\t{self.__colaboradores[i].nombre} ({self.__roles[i].nombre})\n"
        return texto.strip()

c1 = Colaborador("Salvador")
c2 = Colaborador("Misael")
c3 = Colaborador("Fernando")
c4 = Colaborador("Hemilton")

r1 = Rol("BackEnd")
r2 = Rol("FrontEnd")
r3 = Rol("Documentador")
r4 = Rol("Presentador")

p1 = Proyecto("Rutas Baja Express")
p1.agregarColaborador(c1, r1)
p1.agregarColaborador(c2, r2)
p1.agregarColaborador(c3, r3)
p1.agregarColaborador(c4, r4)

print(p1)

#Proyecto: Rutas Baja Express
#Colaboradores:
#        Salvador (BackEnd)
#        Misael (FrontEnd)
#        Fernando (Documentador)
#        Hemilton (Presentador)