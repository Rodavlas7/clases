'''
Ejercicio 6. Copiar un arreglo
Crea un arreglo ramdon (1 a 10), copia cada uno de sus elementos a una nueva lista
utilizando un ciclo.
'''

def recorredor(array): #agregado para comprobar
    if array == []:
        return
    for cosa in range(len(array)):
        print(array[cosa])

arreglo = [1,2,3,4,5,6,7,8,9,10]
arreglo2 = []

for i in range(len(arreglo)):
    arreglo2.append(arreglo[i])

recorredor(arreglo)
recorredor(arreglo2)
