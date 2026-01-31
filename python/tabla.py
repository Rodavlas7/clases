def operaciones(num1, num2):
    suma = num1 + num2
    resta = num1 - num2
    multiplicacion = num1 * num2
    division = num1 / num2
    residuo = num1 % num2

    print(f"La suma de {num1} + {num2} = {suma}")
    print(f"La resta de {num1} - {num2} = {resta}")
    print(f"La multiplicación de {num1} * {num2} = {multiplicacion}")
    print(f"La división de {num1} / {num2} = {division:.2f}")  # solo 2 decimales
    print(f"El residuo de {num1} % {num2} = {residuo}")


def main():
    n1 = int(input("Deme un número: "))
    n2 = int(input("Deme otro número: "))
    operaciones(n1, n2)


if __name__ == "__main__":
    main()
