class Cita:
    def __init__(self, fecha, hora, descripcion):
        self.__Fecha = fecha
        self.__Hora = hora
        self.__Descripcion = descripcion

    def Clave(self):
        return (self.__Fecha, self.__Hora)

class Agenda:
    def __init__(self):
        self.__Citas = []

    def AgendarCita(self, cita):
        for c in self.__Citas:
            if c.Clave() == cita.Clave():
                return
        self.__Citas.append(cita)

    def CancelarCita(self, fecha, hora):
        for c in self.__Citas:
            if c.Clave() == (fecha, hora):
                self.__Citas.remove(c)
                break

    def ConsultarCitas(self):
        return self.__Citas

agenda = Agenda()

c1 = Cita("2026-01-15", "10:00", "Revision")
c2 = Cita("2026-01-15", "11:00", "Consulta")
c3 = Cita("2026-01-15", "10:00", "Consulta")

agenda.AgendarCita(c1)
agenda.AgendarCita(c2)
agenda.AgendarCita(c3)  

print(len(agenda.ConsultarCitas())) 

agenda.CancelarCita("2026-01-15", "10:00")
print(len(agenda.ConsultarCitas())) 
