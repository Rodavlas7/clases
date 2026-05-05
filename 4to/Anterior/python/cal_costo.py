def mostrar_costo(consumo):
    if consumo < 100:
        print(f"El costo es: ${consumo * 0.5}")
    elif consumo <= 200:
        print(f"El costo es: ${consumo * 0.75}")
    else:
        print(f"El costo es: ${consumo * 1.2}")


consumo = float(input("Ingrese el consumo de luz en kW: "))
mostrar_costo(consumo)
