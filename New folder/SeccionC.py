class vehiculo():
    def __init__(self, placas):
        self.__placas = placas
    
    def get_placas(self):
        return self.__placas

class ticket():
    def __init__(self, placas, estado, fechahora):
        self.__placas = placas
        self.__estado = estado #1 = activo, 2 = desactivado
        self.__fechahora = fechahora

    def get_placas(self):
        return self.__placas
    
    def get_estado(self):
        return self.__estado

class estacionamiento():
    def __init__(self, lugares):

        if lugares <= 0:
            return

        self.__lugares = lugares
        self.__tickets = []

    def lugares_disponibles(self):
        if self.__tickets == []:
            return self.__lugares
        
        contador = 0

        for i in range(len(self.__tickets)):
            if self.__tickets[i].get_estado() == 1:
                contador += 1

        return (self.__lugares - contador)

    def agregar_vehiculo(self, placas, fechahora):
        if self.__lugares == 0:
            return
        
        validado = False
        estadofinal = 0

        if self.lugares_disponibles() == 0:
            return
        
        elif self.__tickets == []:
            validado == True
            
        else:
            for i in range(len(self.__tickets)):
                for j in range(len(self.__tickets)):
                    estadofinal = self.__tickets[j].get_estado()
                    print(estadofinal)

                if self.__tickets[i].get_placas() == placas and estadofinal == 1:
                    validado = True
                    break

        print(validado)
        if validado == True:
            self.__tickets.append(ticket(placas,1,fechahora))


e = estacionamiento(10)
print(e.lugares_disponibles())


e.agregar_vehiculo("123456", '2026-02-03-08:45')
print(e.lugares_disponibles())