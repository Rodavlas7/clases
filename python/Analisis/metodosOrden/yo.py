import random
import time
from colorama import Fore, Style

merge_checks = 0
merge_moves = 0

def bubble(lista):
    l = len(lista)
    checks = 0
    swaps = 0
    for i in range(l):
        for j in range(l-1-i):
            checks += 1
            if lista[j] > lista[j+1]: 
                swaps += 1
                lista[j], lista[j+1] = lista[j+1], lista[j]
                print(lista)
                time.sleep(0.01)
                
    print(f"\nBubble -> Checks: {checks} | Swaps: {swaps}\n")
    return lista

def merge(izquierda, derecha):
    global merge_checks, merge_moves
    final = []

    i, j = 0, 0

    print("\n\n",izquierda, derecha)
    print()

    while i < len(izquierda) and j < len(derecha):
        merge_checks += 1
        if izquierda[i] < derecha[j]:
            final.append(izquierda[i])
            i += 1
        else:
            final.append(derecha[j])
            j += 1
        merge_moves += 1
        print("Final", final)
        time.sleep(0.01)
            
    merge_moves += len(izquierda[i:]) + len(derecha[j:])
    
    final.extend(izquierda[i:])
    final.extend(derecha[j:])

    print("Final", final)

    return final

def mergeRecursivo(lista):
    if len(lista) <= 1: 
        return lista
        
    mitad = len(lista) // 2
    izquierda = mergeRecursivo(lista[:mitad])
    derecha   = mergeRecursivo(lista[mitad:])

    return merge(izquierda, derecha)


lista = []
for i in range(20): lista.append(i) 

lista_original = random.sample(lista, len(lista))

print("Lista original:")
print(lista_original)

print(" BURBUJA ")
print(bubble(lista_original.copy()))

print()
print()

print(" MERGE RECURSIVO ")
print(mergeRecursivo(lista_original.copy()))
print(f"\nMerge  -> Checks: {merge_checks} | Swaps: {merge_moves}")