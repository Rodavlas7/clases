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

def imprimir_lista_mayor(lista, numero):
    if len(lista) == 0:
        return
    for elemento in lista:
        if elemento > numero:
            print(elemento)

imprimir_lista_mayor(lista_random(20, 1, 10), 5)