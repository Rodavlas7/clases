def calcula_lista(lista):
    if len(lista) == 0:
        return

    contador = 0

    for i in range(len(lista)):
        contador += lista[i]
    return contador




numeros = [5, 8, 2, 10, 3, 9, 7]
print(calcula_lista(numeros))