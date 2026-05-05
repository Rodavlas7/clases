'''
Ejercicio 2. Recorrer un arreglo usando índices
Crea un arreglo ramdon (1 a 10), recorre el arreglo utilizando sus posiciones e imprime
cada elemento indicando su índice correspondiente.
'''

def recorredor_con_indices(array):
    for i in range(len(array)):
        print(f"Posicion: {i}\nValor: {array[i]}\n")


arreglo = [1,2,3,4,5,6,7,8,9,10]
recorredor_con_indices(arreglo)