'''
Ejercicio 9. Reemplazar valores del arreglo
Crea un arreglo ramdon (1 a 10), recorre el arreglo y reemplaza ciertos valores por otros
según una condición establecida.
'''

def remplazador(array):
    if array == []:
        return
    for i in range(len(array)):
        if array[i] % 2 == 0:
            array[i] = array[i] * 2
        else:
            array[i] = array[i] + 1
    return array

def recorredor(array): #agregado para comprobar
    for cosa in range(len(array)):
        print(array[cosa])

arreglo = [1,2,3,4,5,6,7,8,9,10]
remplazado = remplazador(arreglo)
recorredor(remplazado)