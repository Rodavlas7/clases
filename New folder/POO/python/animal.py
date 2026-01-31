class Animal:
    def __init__(self, especie, edad): 
        self.especie = especie
        self.edad = edad

    def hablar(self):
        pass

    def moverse(self):
        pass

    def describeme(self):
        print("Soy un animal de tipo", type(self).__name__)


class Perro(Animal):
    def __init__(self, especie, edad, dueño):
        super().__init__(especie, edad)
        self.dueño = dueño

    def hablar(self):
        print("Perro ladrando")

    def moverse(self):
        print("Perro caminando")

    def __str__(self):
        return f"Especie: {self.especie}, Edad: {self.edad} años, Dueño: {self.dueño}"


class Ballena(Animal):
    def hablar(self):
        print("Ballena cantando")

    def moverse(self):
        print("Ballena nadando")

    def __str__(self):
        return f"Especie: {self.especie}, Edad: {self.edad} años"


class Fenix(Animal):
    def __init__(self, especie, edad, picar):
        super().__init__(especie, edad)
        self.picar = picar

    def hablar(self):
        print("Fénix cantando")

    def moverse(self):
        print("Fénix volando")

    def __str__(self):
        return f"Especie: {self.especie}, Edad: {self.edad} años, Picar: {self.picar}"
    
def main():
    mi_perro = Perro("Mamífero", 5, "Salvador")
    mi_perro.describeme()
    print(mi_perro)
    mi_perro.hablar()
    mi_perro.moverse()

    print("\n")

    mi_ballena = Ballena("Mamífero", 25)
    mi_ballena.describeme()
    print(mi_ballena)
    mi_ballena.hablar()
    mi_ballena.moverse()

    print("\n")

    mi_fenix = Fenix("Ave Mítica", 1000, "Picar con fuerza")
    mi_fenix.describeme()
    print(mi_fenix)
    mi_fenix.hablar()
    mi_fenix.moverse()


if __name__ == "__main__":
    main()