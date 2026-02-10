def promedio(array):
    contador = 0

    if array == []:
        return

    for i in range(len(array)):
        contador += array[i]

    return (contador/len(array))

def aprobatorio(array):
    contador = 0

    if array == []:
        return

    for i in range(len(array)):
        if array[i] >= 7:
            contador += 1

    return (contador)

array = [10,6,8,9,7,5,7,10]
print(promedio(array))
print(aprobatorio(array))