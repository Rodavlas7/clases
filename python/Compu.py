class CPU:
    def __init__(self, marca, velocidad_ghz, nucleos):
        self.__Marca = marca
        self.__VelocidadGHz = velocidad_ghz
        self.__Nucleos = nucleos

    def Describir(self):
        return f"CPU: {self.__Marca}, {self.__VelocidadGHz} GHz, {self.__Nucleos} núcleos"

class RAM:
    def __init__(self, capacidad_gb, tipo):
        self.__CapacidadGB = capacidad_gb
        self.__Tipo = tipo

    def Describir(self):
        return f"RAM: {self.__CapacidadGB} GB {self.__Tipo}"

class DiscoDuro:
    def __init__(self, capacidad_gb, tipo):
        self.__CapacidadGB = capacidad_gb
        self.__Tipo = tipo

    def Describir(self):
        return f"Disco Duro: {self.__CapacidadGB} GB ({self.__Tipo})"

class Computadora:
    def __init__(self, marca, modelo, cpu_marca, cpu_velocidad, cpu_nucleos, ram_capacidad, ram_tipo, disco_capacidad, disco_tipo):
        self.__Marca = marca
        self.__Modelo = modelo

        self.__CPU = CPU(cpu_marca, cpu_velocidad, cpu_nucleos)
        self.__RAM = RAM(ram_capacidad, ram_tipo)
        self.__DiscoDuro = DiscoDuro(disco_capacidad, disco_tipo)

    def MostrarConfiguracion(self):
        print(f"Computadora: {self.__Marca} {self.__Modelo}")
        print(self.__CPU.Describir())
        print(self.__RAM.Describir())
        print(self.__DiscoDuro.Describir())

def main():
    pc1 = Computadora("Dell","Inspiron 15","Intel Core i7",3.5,8,16,"DDR4",1000,"SSD")

    pc1.MostrarConfiguracion()
    
if __name__ == "__main__":
    main()
