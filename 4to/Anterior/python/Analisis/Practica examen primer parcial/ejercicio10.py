'''
Ejercicio 10. Contar elementos del arreglo
Crea un arreglo ramdon (1 a 10), recorre el arreglo y determina cuántos elementos son
menores a 5.
'''

def contadorMenor(array):
    if array == []:
        return
    contador = 0
    for i in range(len(array)):
        if array[i] < 5:
            contador += 1
    return contador

arreglo = [1,2,3,4,5,6,7,8,9,10]
print(contadorMenor(arreglo))