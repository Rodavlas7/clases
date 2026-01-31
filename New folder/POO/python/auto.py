class Auto:
    def __init__(self, modelo, velocidad_maxima, potencia, marcha):
        self.modelo = modelo
        self.__velocidad_maxima = velocidad_maxima  
        self.__potencia = potencia                  
        self.__marcha = marcha                      
        self.encendido = False
        self.acelerando = False


    def get_velocidad_maxima(self):
        return self.__velocidad_maxima

    def get_potencia(self):
        return self.__potencia

    def get_marcha(self):
        return self.__marcha


    def set_velocidad_maxima(self, nueva_velocidad):
        if nueva_velocidad > 0:
            self.__velocidad_maxima = nueva_velocidad
        else:
            print("La velocidad máxima debe ser mayor a 0")

    def set_potencia(self, nueva_potencia):
        if nueva_potencia > 0:
            self.__potencia = nueva_potencia
        else:
            print("La potencia debe ser mayor a 0")

    def set_marcha(self, nueva_marcha):
        if nueva_marcha > 0:
            self.__marcha = nueva_marcha
        else:
            print("La marcha debe ser mayor a 0")

    
    def encender(self):
        if not self.encendido:
            self.encendido = True
            print(f"{self.modelo} ahora está encendido")
        else:
            print(f"{self.modelo} ya estaba encendido")

    def apagar(self):
        if self.encendido:
            if self.acelerando:
                print(f"No puedes apagar {self.modelo} mientras está acelerando")
            else:
                self.encendido = False
                print(f"{self.modelo} ahora está apagado")
        else:
            print(f"{self.modelo} ya estaba apagado")

    def acelerar(self):
        if self.encendido:
            if not self.acelerando:
                self.acelerando = True
                print(f"{self.modelo} está acelerando 🚀")
            else:
                print(f"{self.modelo} ya estaba acelerando")
        else:
            print(f"No puedes acelerar {self.modelo} porque está apagado")

    def frenar(self):
        if self.acelerando:
            self.acelerando = False
            print(f"{self.modelo} ha frenado 🛑")
        else:
            print(f"{self.modelo} no está acelerando, no puede frenar")

    def info(self):
        estado = "encendido" if self.encendido else "apagado"
        movimiento = "acelerando" if self.acelerando else "detenido"
        print(f"Auto: {self.modelo} | Velocidad Máx: {self.__velocidad_maxima} km/h | ")
        print(f"Potencia: {self.__potencia} HP | Marcha: {self.__marcha} | ")
        print(f"Estado: {estado} | Movimiento: {movimiento}")

def main():
    auto1 = Auto("Toyota Supra MK4", 250, 330, "Manual 6")
    auto2 = Auto("Nissan GT-R R34", 280, 320, "Manual 6")

    auto1.encender()
    auto1.acelerar()
    auto1.frenar()
    auto1.apagar()

    print()

    auto2.encender()
    auto2.acelerar()
    auto2.frenar()
    auto2.apagar()


if __name__ == "__main__":
    main()