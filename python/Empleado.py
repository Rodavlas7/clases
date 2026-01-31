class Empleado:
    def __init__(self, nombre, apellido, edad, salario):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.salario = salario

    def info(self):
        print(f"{self.nombre} {self.apellido} tiene {self.edad} años de edad y un salario de {self.salario} monedas")

    def aumento(self):
        if self.edad >= 40:
            self.salario *= 1.10
            print(f"{self.nombre} {self.apellido} obtuvo un aumento del 10%, nuevo sueldo: {self.salario} monedas")
        else:
            print(f"{self.nombre} {self.apellido} no es apto para el aumento")

    def get_nombre(self):
        return self.nombre

    def get_apellido(self):
        return self.apellido

    def get_edad(self):
        return self.edad

    def get_salario(self):
        return self.salario


    def set_nombre(self, nombre):
        self.nombre = nombre

    def set_apellido(self, apellido):
        self.apellido = apellido

    def set_edad(self, edad):
        self.edad = edad

    def set_salario(self, salario):
        self.salario = salario

def main():
    emp1 = Empleado("Jose", "Martinez", 40, 1500)
    emp1.aumento()
    emp1.info

    emp2 = Empleado("Ana", "Lopez", 39, 2000)
    emp2.aumento()
    emp2.set_edad(40)
    emp2.aumento()
    emp2.info()

if __name__ == "__main__":
    main()