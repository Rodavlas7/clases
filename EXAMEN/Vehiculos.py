class Vehiculo():
    def __init__(self, matricula, modelo, potencia):
        self.__matricula = matricula
        self.__modelo = modelo
        self.__potencia = potencia


    def setMatricula(self, matricula):
        self.__matricula = matricula
    
    def setModelo(self, modelo):
        self.__modelo = modelo

    def setPotencia(self, potencia):
        if potencia > 0:
            self.__potencia = potencia
        else:
            self.__potencia = 0

    def getMatricula(self):
        return self.__matricula
    
    def getModelo(self):
        return self.__modelo
    
    def getPotencia(self):
        return self.__potencia
    

    def info(self):
        pass
    


class Taxi(Vehiculo):
    def __init__(self, matricula, modelo, potencia, num_licencia):
        self.__matricula = matricula
        self.__modelo = modelo
        self.__potencia = potencia
        self.__licencia = num_licencia
        self.__contador = 0
        self.__total = 0
        

    def setLicencia(self, licencia):
        self.__licencia = licencia

    def setContador(self, contador):
        
        if contador > 0:
            self.__contador = contador
        else: 
            self.__contador = 0
            
    def setPagoTotal(self, pago):
        self.__total = pago


    def getLicencia(self):
        return self.__licencia
    
    def getContador(self):
        return self.__contador
    
    def getPagoTotal(self):
        return self.__total
    

    def agregarViaje(self, viajes, coste):
        if viajes == "" and coste == "":
            viajes=0
            coste=0
        else:
            self.__contador += viajes
            self.__total += coste 

    def info(self):
        print(f"Modelo = {self.__modelo}")
        print(f"Matricula = {self.__matricula}")
        print(f"Potencia = {self.__potencia}")
        print(f"Num de Licencia = {self.__licencia}")
        print(f"Pago Total = {self.__total}")
        print(f"Viajes = {self.__contador}")



class Autobus(Vehiculo):
    def __init__(self, matricula, modelo, potencia, asientos):
            self.__matricula = matricula
            self.__modelo = modelo
            self.__potencia = potencia
            if asientos >= 0:
                self.__asientos = asientos
            else:
                self.__asientos = 0
            self.__contador = 0

    def setAsientos(self, asientos):
        if asientos >= 0:
            self.__asientos = asientos
        else:
            self.__asientos = 0

    def setContador(self, contador):
        if contador > 0:
            self.__contador = contador
        else: 
            self.__contador = 0


    def getAsientos(self):
        return self.__asientos
    
    def getContador(self):
        return self.__contador
    
    def getLibres(self):
        return (self.__asientos - self.__contador)

    def subirPersonas(self, numPersonas):
        if (self.getLibres() >= numPersonas):
            self.__contador = (self.__contador + numPersonas)
        else:
            print(f"No hay suficientes sitios libres ({self.getLibres()})")

    def info(self):
        print(f"Modelo = {self.__modelo}")
        print(f"Matricula = {self.__matricula}")
        print(f"Potencia = {self.__potencia}")
        print(f"Personas a Bordo = {self.__contador}")
        print(f"Sitios libres = {self.getLibres()}")