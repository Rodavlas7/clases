'''Ejercicio 1. Recorrer un arreglo
Crea un arreglo ramdon (1 a 10), recorre el arreglo y muestra cada uno de sus elementos en pantalla.
'''
def recorredor(array):
    for cosa in range(len(array)):
        print(array[cosa])


arreglo = [4,2,3,4,5,6,7,]
recorredor(arreglo)