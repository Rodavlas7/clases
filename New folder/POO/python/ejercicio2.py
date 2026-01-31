meses = int(input("A cuantos meses desea pagarlo: "))
costo = int(input("Que coste tiene el articulo  : "))

for i in range(1, meses + 1):
    print(f"Mes {i} \tse tiene que pagar un importe de ${costo}")
    costo *= 2