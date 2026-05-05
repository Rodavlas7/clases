class Empleado:
    def __init__(self, rfc="", nombre="", depto="", puesto=""):
        self.setRFC(rfc)
        self.setNombre(nombre)
        self.setDepto(depto)
        self.setPuesto(puesto)


    def setRFC(self, rfc):
        if rfc == "":
            self.__rfc = "SIN_RFC"
        else:
            self.__rfc = rfc

    def setNombre(self, nombre):
        if nombre == "":
            self.__nombre = "SIN_NOMBRE"
        else:
            self.__nombre = nombre

    def setDepto(self, depto):
        if depto == "":
            self.__depto = "SIN_DEPTO"
        else:
            self.__depto = depto

    def setPuesto(self, puesto):
        if puesto == "":
            self.__puesto = "SIN_PUESTO"
        else:
            self.__puesto = puesto


    def getRFC(self): return self.__rfc
    def getNombre(self): return self.__nombre
    def getDepto(self): return self.__depto
    def getPuesto(self): return self.__puesto


    def calcularSueldo(self):
        pass

    def info(self):
        print(f"Empleado: {self.getNombre()} ({self.getPuesto()})")
        print(f"RFC: {self.getRFC()} - Depto: {self.getDepto()}")
        print(f"Sueldo quincenal: {self.calcularSueldo()}\n")


class EmpAdmvo(Empleado):
    def __init__(self, rfc, nombre, depto, sueldoMensual):
        super().__init__(rfc, nombre, depto, "Administrativo")
        self.__sueldoMensual = sueldoMensual

    def calcularSueldo(self):
        return self.__sueldoMensual / 2


class EmpMecanico(Empleado):
    def __init__(self, rfc, nombre, depto, totalTrabajos):
        super().__init__(rfc, nombre, depto, "Mecánico")
        self.__totalTrabajos = totalTrabajos

    def calcularSueldo(self):
        return self.__totalTrabajos * 0.04


class EmpVendedor(Empleado):
    def __init__(self, rfc, nombre, depto, totalVentas, salarioMinimo=6000):
        super().__init__(rfc, nombre, depto, "Vendedor")
        self.__totalVentas = totalVentas
        self.__salarioMinimo = salarioMinimo

    def calcularSueldo(self):
        return self.__salarioMinimo + (self.__totalVentas * 0.02)


def main():
    a1 = EmpAdmvo("RFC123", "Ana", "Administración", 12000)
    m1 = EmpMecanico("RFC456", "Luis", "Taller", 50000)
    v1 = EmpVendedor("RFC789", "Marta", "Ventas", 80000)

    empleados = [a1, m1, v1]
    for e in empleados:
        e.info()


if __name__ == "__main__":
    main()
