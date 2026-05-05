import random

def lista_random(longitud,minimo, maximo):
    if minimo > maximo:
        return
    if minimo < 0 or maximo < 0:
        return
    if longitud <= 0:
        return
    
    lista = []
    for i in range(longitud):
        numero = random.randint(minimo, maximo)
        lista.append(numero)
    return lista

def contador_pares(lista):
    if len(lista) == 0:
        return
    contador = 0
    for i in range(len(lista)):
        if (lista[i] % 2) == 0:
            contador += 1
    return contador

print(contador_pares(lista_random(20, 1, 10)))