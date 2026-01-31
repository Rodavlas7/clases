tra = int(input("Numero de trabajadores: "))
pago = int(input("Cuanto sera el pago/hora: "))
texto = ""
contador = 0

for i in range(1, tra + 1):
    print(f"\n Para el trabajor #{i}")
    dia = int(input("Numero de dias trbajados: "))

    for j in range(1, dia + 1):
        horas =  int(input(f"Cuantas horas se trabajo el dia {j}: "))
        contador += horas
    texto = texto + f"\nEl trabajador {i} trabajo {horas} horas por un sueldo de ${pago*horas}"

print(texto)
print(f"\tEl total pagado a {tra} trabajadores fue ${(horas*pago)}")