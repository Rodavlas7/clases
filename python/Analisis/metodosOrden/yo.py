import random

def sort(lista):
    l = len(lista)
    for i in range(l):
        for j in range(l-1-i):
            if lista[j] > lista[j+1]: lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista

def merge(lista):
    return

lista = []

for i in range(100):
    lista.append(i)

lista = random.sample(lista, len(lista))

print(lista)

lista = sort(lista)

print(lista)