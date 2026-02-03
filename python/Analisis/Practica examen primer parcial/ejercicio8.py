'''
Ejercicio 8. Filtrar datos del arreglo
Crea un arreglo ramdon (1 a 10), recorre el arreglo y muestra únicamente aquellas que
sean mayores o iguales a 8.
'''

def recorredorFiltrado(array): #agregado para comprobar
    if array == []:
        return
    for cosa in range(len(array)):
        valor = array[cosa]
        if valor >= 8:
            print(valor)

arreglo = [1,2,3,4,5,6,7,8,9,10]
recorredorFiltrado(arreglo)