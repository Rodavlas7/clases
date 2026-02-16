def revertir_lista(lista):
    if len(lista) == 0:
        return
    lista_revertida = []
    n = len(lista)
    for i in range(n):
        elemento = n-i-1
        lista_revertida.append(lista[elemento])
    return lista_revertida

def imprimir_lista(lista):
    if len(lista) == 0:
        return
    for elemento in lista:
        print(elemento)

lista = [5, 8, 2, 10, 3,9,7]
imprimir_lista(revertir_lista(lista))