def max(lista):
    if len(lista) == 0:
        return
    
    for i in range(len(lista)):
        elemento = lista[i]
        if i == 0:
            numero = elemento
        elif numero < elemento:
            numero = elemento
    return numero

def min(lista):
    if len(lista) == 0:
        return
    
    for i in range(len(lista)):
        elemento = lista[i]
        if i == 0:
            numero = elemento
        elif numero > elemento:
            numero = elemento
    return numero

numeros = [5, 8, 2, 10, 3,9,7]
print(min(numeros))
print(max(numeros))
