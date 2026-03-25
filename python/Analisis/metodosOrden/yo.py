import random

merge_checks = 0
merge_moves = 0

def bubble(lista):
    l = len(lista)
    checks = 0
    swaps = 0
    print(lista)
    for i in range(l):
        for j in range(l-1-i):
            checks += 1
            if lista[j] > lista[j+1]: 
                swaps += 1
                lista[j], lista[j+1] = lista[j+1], lista[j]
                
    print(f"\nBubble -> Checks: {checks} | Swaps: {swaps}\n")
    return lista

def merge(izquierda, derecha):
    global merge_checks, merge_moves
    final = []

    i, j = 0, 0

    while i < len(izquierda) and j < len(derecha):
        merge_checks += 1
        if izquierda[i] < derecha[j]:
            final.append(izquierda[i])
            i += 1
        else:
            final.append(derecha[j])
            j += 1
        merge_moves += 1
            
    merge_moves += len(izquierda[i:]) + len(derecha[j:])
    
    final.extend(izquierda[i:])
    final.extend(derecha[j:])

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

print(" BURBUJA ")
bubble(lista_original.copy())

print(" MERGE RECURSIVO ")
mergeRecursivo(lista_original.copy())
print(f"\nMerge  -> Checks: {merge_checks} | Swaps: {merge_moves}")