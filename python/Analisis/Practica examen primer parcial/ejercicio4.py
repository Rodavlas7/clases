'''
Ejercicio 4. Mutar un arreglo (operación matemática)
Crea un arreglo ramdon (1 a 10),, recorre el arreglo y multiplica cada elemento por 2,
guardando el resultado en el mismo arreglo.
'''
def mutadorOperacional(array):
    if array == []:
        return
    for i in range(len(array)):
        array[i] = array[i]*2
    return array

def recorredor(array): #agregado para comprobar
    for cosa in range(len(array)):
        print(array[cosa])

arreglo = [1,2,3,4,5,6,7,8,9,10]
arreglo = mutadorOperacional(arreglo)
recorredor(arreglo)