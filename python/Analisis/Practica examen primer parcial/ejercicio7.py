'''
Ejercicio 7. Copiar un arreglo con modificación
Crea un arreglo ramdon (1 a 10), copia sus valores en una nueva lista, pero aplicando
una operación matemática a cada elemento.
'''

def recorredor(array): #agregado para comprobar
    if array == []:
        return
    for cosa in range(len(array)):
        print(array[cosa])

arreglo = [1,2,3,4,5,6,7,8,9,10]
arreglo2 = []

for i in range(len(arreglo)):
    arreglo2.append((arreglo[i] * 10)/2)

recorredor(arreglo2)