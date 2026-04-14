import colorama

#Reset automaticamente el color despues de cada print
colorama.init(autoreset=True)

ar1 = [1, 2, 3, 4, 5]
ar2 = [1, 2, 3, 5, 4]

print(colorama.Fore.GREEN + "Arreglo 1: ", ar1)
print(colorama.Fore.RED + "Arreglo 2: ", ar2)

def comparador(ar1, ar2):
    texto = ''
    for i in ar1:
            if ar1[i] != ar2[i]: