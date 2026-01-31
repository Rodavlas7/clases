class Figura:
    def area(self):
        pass

    def perimetro(self):
        pass

    def info(self):
        pass



class Rectangulo(Figura):
    def __init__(self, base=1, altura=1):
        self.setAltura(altura)
        self.serBase(base)

    def setAltura(self, alto):
        if 0 < alto:
            self.__alto = alto
        else:
            self.__alto = 1

    def serBase(self, base):
        if 0 < base:
            self.__base = base
        else:
            self.__base = 1

    def getAltura(self):
        return self.__alto

    def getBase(self):
        return self.__base

    def area(self):
        return self.__alto * self.__base


    def perimetro(self):
        if (2 * (self.__alto + self.__base))<=50:
            return 2 * (self.__alto + self.__base)
        else:
            return"Rectangulo de grandes dimensiones (perimetro mayor a 50)"


    def info(self):
        print(f"Rectángulo:")
        print(f"Alto        = {self.getAltura()}")
        print(f"base        = {self.getBase()}")
        print(f"Area        = {self.area()}")
        print(f"Perimetro   = {self.perimetro()}")


class Triangulo(Figura):
    def __init__(self, base=1, altura=1, tipo="Escaleno"):
        self.serBase(base)
        self.setAltura(altura)
        self.__tipo = tipo

    def serBase(self, base):
        if 0 < base:
            self.__base = base
        else:
            self.__base = 1

    def setAltura(self, altura):
        if 0 < altura:
            self.__altura = altura
        else:
            self.__altura = 1

    def getBase(self):
        return self.__base

    def getAltura(self):
        return self.__altura

    def getTipo(self):
        return self.__tipo

    def area(self):
        if ((self.__base*self.__altura)/2) <= 30:
            return (self.__base * self.__altura) / 2
        else:
            return "Triangulo de grandes dimensiones"

            
    def info(self):
        print(f"Triángulo ({self.__tipo}):")
        print(f"Base        = {self.getBase()}")
        print(f"Altura      = {self.getAltura()}")
        print(f"Area        = {self.area()}")

        

def main(): 
    t1 = Triangulo(5,7,"Escaleno")
    t2 = Triangulo(10,15,"Isoceles")
    t1.info()
    t2.info()
    print("\n\n")
    r1 = Rectangulo(7,10)
    r2 = Rectangulo(15,20)
    r1.info()
    r2.info()

if __name__ == "__main__": main()