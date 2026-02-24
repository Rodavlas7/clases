import random

def imprimir(m):
    for i in range(len(m)):
        for j in range(len(m[i])):
            print(f"{m[i][j]}\t", end="")
        print()

m = []
fila = 3
columna = 3

for i in range(fila):
    filas = []
    for j in range(columna):
        filas.append(random.randint(1, 99))
    m.append(filas)

imprimir(m)