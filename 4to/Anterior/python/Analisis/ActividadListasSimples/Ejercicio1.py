def imprimir_lista(lista):
    if len(lista) == 0:
        return
    for elemento in lista:
        print(elemento)


numeros = [5, 8, 2, 10, 3, 9, 7]
imprimir_lista(numeros)