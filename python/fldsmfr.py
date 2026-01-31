from Empleado import Empleado
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