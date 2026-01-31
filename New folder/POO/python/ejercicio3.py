tipo = input("Tipo de uva (A o B): ").upper()
tama = int(input("Tamaño de uva (1 o 2): "))
kilo = float(input("Cantidad de kilos: "))
precio = float(input("Precio inicial por kilo: "))


if tipo == 'A':
    if tama == 1:
        precio += 0.20
    elif tama == 2:
        precio += 0.30
elif tipo == 'B':
    if tama == 1:
        precio -= 0.30
    elif tama == 2:
        precio -= 0.50


print(f"\nPrecio final por kilo: \t${precio}")
print(f"Total a recibir: \t${(kilo * precio):.2f}")