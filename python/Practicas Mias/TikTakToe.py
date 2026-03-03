from colorama import init, Fore, Style
init(autoreset=True)
import os

def imprimir(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == "X":
                print(f"{Style.BRIGHT}{Fore.RED}{matriz[i][j]}\t", end="")
            elif matriz[i][j] == "O":
                print(f"{Style.BRIGHT}{Fore.BLUE}{matriz[i][j]}\t", end="")
            else:
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

m = crearMatrizTTT()

while True:
    os.system('clear')
    print(f'{Fore.YELLOW}Los numeros son las posiciones disponibles')
    while True:
        print(f'{Fore.RED}Juega {Style.BRIGHT}X{Style.NORMAL}:') # Texto fijo en Cian
        imprimir(m)
        correcto = turno(m, "X", int(input("Posicion:")))
        if correcto == True:
            break
    
    os.system('clear')
    print(f'{Fore.YELLOW}Los numeros son las posiciones disponibles')
    while True:
        print(f'{Fore.BLUE}Juega {Style.BRIGHT}O{Style.NORMAL}:') # Texto fijo en Magenta
        imprimir(m)
        correcto = turno(m, "O", int(input("Posicion:")))
        if correcto == True:
            break