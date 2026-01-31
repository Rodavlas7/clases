def comparar_numeros(a, b):
    if a < 0 and b < 0:
        print("Los 2 son negativos")
    elif a > 0 and b < 0:
        print("a es positivo, b es negativo")
    elif a < 0 and b > 0:
        print("a es negativo, b es positivo")
    elif a > 0 and b > 0:
        print("Los 2 son positivos")
    else:
        print("Caso no contemplado (al menos uno es 0)")


a = int(input("Ingrese el valor de a: "))
b = int(input("Ingrese el valor de b: "))
comparar_numeros(a, b)
