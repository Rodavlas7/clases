'''
Ejercicio 3. Mutar un arreglo (incrementar valores)
Crea un arreglo ramdon (1 a 10),, recorre el arreglo y aumenta en una unidad cada valor,
modificando la lista original.
'''

def mutador1(array):
    nuevo = []
    if array == []:
        return
    for i in range(len(array)):
        nuevo.append(array[i]+1)
    return nuevo

def mutador2(array):
    if array == []:
        return
    for i in range(len(array)):
        array[i] = array[i] + 1
    return array

def recorredor(array): #agregado para comprobar
    for cosa in range(len(array)):
        print(array[cosa])

arreglo = [1,2,3,4,5,6,7,8,9,10]
arreglo = mutador2(arreglo)
recorredor(arreglo)