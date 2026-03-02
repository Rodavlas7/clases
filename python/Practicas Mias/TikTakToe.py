def imprimir(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(f"{matriz[i][j]}\t", end="")
        print("\n")
    print("\n")

def vefificar(matriz):
    primer, segundo, tercer = None
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            tercer = matriz
    return False

def turno(matriz, valor, posicion):
    if posicion > 9 and posicion < 1:
        print("la posicion debe estar disponible y ser un numero dentro de la lista")
        return False

    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == posicion:
                matriz[i][j] = valor
                return True
    print("la posicion debe estar disponible y ser un numero dentro de la lista")
    return False

def crearMatrizTTT():
    matriz = []
    for i in range(3):
        filas = []
        for j in range(3):
            filas.append("")
        matriz.append(filas)

    contador = 1
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            matriz[i][j] = contador
            contador += 1    
    return matriz



print('Los numeros son las posiciones disponibles')
m = crearMatrizTTT()
while True:
    while True:
        print('Juega X:')
        imprimir(m)
        correcto = turno(m, "X", int(input("Posicion:")))
        if correcto == True:
            break
    while True:
        print('Juega O:')
        imprimir(m)
        correcto = turno(m, "O", int(input("Posicion:")))
        if correcto == True:
            break