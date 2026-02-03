'''
Ejercicio 5. Mostrar información del arreglo
Crea un arreglo ramdon (1 a 10), muestra todos los elementos del arreglo y
posteriormente indica cuántos elementos contiene.
'''

def informador(array):
    if array == []:
        return
    for elemento in range(len(array)):
        print(array[elemento])
    print(f"El numero de elmentos dentro del arreglo es: {len(array)}")
    

arreglo = [1,2,3,4,5,6,7,8,9,10]
informador(arreglo)