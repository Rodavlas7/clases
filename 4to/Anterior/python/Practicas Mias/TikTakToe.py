from colorama import init, Fore, Style
import os

class Gato:
    def __init__(self):
        init(autoreset=True)
        self.m = self.crearMatrizTTT()

    def imprimir(self, matriz):
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

    def verificar(self, matriz):
        primer, segundo, tercer = None, None, None
        
        for i in range(len(matriz)):
            for j in range(len(matriz[i])):
                primer = segundo
                segundo = tercer
                tercer = matriz[i][j]
                if primer == segundo and segundo == tercer:
                    return True
        return False

    def turno(self, matriz, valor, posicion):
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

    def crearMatrizTTT(self):
        matriz = []
        for i in range(3):
            filas = []
            for j in range(3):
                filas.append("")
            matriz.append(filas)

        contador = 9
        for i in range(len(matriz)):
            for j in range(len(matriz[i])):
                matriz[i][j] = contador
                contador -= 1    
        return matriz

    def jugar(self):
        while True:
            os.system('clear')
            print(f'{Fore.YELLOW}Los numeros son las posiciones disponibles')
            while True:
                print(f'{Fore.RED}Juega {Style.BRIGHT}X{Style.NORMAL}:')
                self.imprimir(self.m)
                correcto = self.turno(self.m, "X", int(input("Posicion:")))
                if correcto == True:
                    if self.verificar(self.m) == True:
                        print("Gano X")
                    break
            
            os.system('clear')
            print(f'{Fore.YELLOW}Los numeros son las posiciones disponibles')
            while True:
                print(f'{Fore.BLUE}Juega {Style.BRIGHT}O{Style.NORMAL}:')
                self.imprimir(self.m)
                correcto = self.turno(self.m, "O", int(input("Posicion:")))
                if correcto == True:
                    break

if __name__ == "__main__":
    juego = Gato()
    juego.jugar()
