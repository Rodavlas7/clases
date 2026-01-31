class PlanTrabajo:
    def __init__(self, Objetivos, Actividades):
        self.Objetivos = Objetivos
        self.Actividades = Actividades

    def MostrarPlan(self):
        print("Plan de Trabajo:")
        print(f"Objetivos: {self.Objetivos}")
        print(f"Actividades: {self.Actividades}")


class Docente:
    def __init__(self, Nombre, Grupo):
        self.Nombre = Nombre
        self.Grupo = Grupo
        self.PlanTrabajo = None

    def CrearPlan(self, Objetivos, Actividades):
        self.PlanTrabajo = PlanTrabajo(Objetivos, Actividades)

    def MostrarDocente(self):
        print(f"Docente: {self.Nombre} | Grupo: {self.Grupo}")
        if self.PlanTrabajo:
            self.PlanTrabajo.MostrarPlan()
        else:
            print("Sin plan de trabajo asignado")

    def __del__(self):
        print(f"El docente {self.Nombre} ha sido eliminado, junto con su plan de trabajo.")
        del self.PlanTrabajo


class RecursoDigital:
    def __init__(self, Tipo, Url):
        self.Tipo = Tipo
        self.Url = Url

    def MostrarRecurso(self):
        print(f"- {self.Tipo}: {self.Url}")


class Curso:
    def __init__(self, Nombre, Docente):
        self.Nombre = Nombre
        self.Docente = Docente
        self.Recursos = []

    def AgregarRecurso(self, Recurso):
        self.Recursos.append(Recurso)

    def MostrarCurso(self):
        print(f"Curso: {self.Nombre}")
        print(f"Docente: {self.Docente.Nombre}")
        print("Recursos Digitales:")
        if self.Recursos:
            for R in self.Recursos:
                R.MostrarRecurso()
        else:
            print("No hay recursos añadidos")


Docente1 = Docente("Salvador Bojórquez", "DSM-301")
Docente1.CrearPlan("Enseñar POO con ejemplos", "Practicar clases y objetos")

Curso1 = Curso("Programación Orientada a Objetos", Docente1)
Curso1.AgregarRecurso(RecursoDigital("Video", "https://youtu.be/abc123"))
Curso1.AgregarRecurso(RecursoDigital("PDF", "https://uttt.edu/poo.pdf"))

Docente1.MostrarDocente()
print("")
Curso1.MostrarCurso()

del Docente1
