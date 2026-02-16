def crear_lista():
    lista = []
    while True:
        numero = input("Ingrese un número (o 's' para terminar): ")
        if numero.lower() == 's':
            break
        try:
            numero = int(numero)
            lista.append(numero)
        except ValueError:
            print("Por favor, ingrese un número válido.")
    return lista

def promedio_lista(lista):
    if len(lista) == 0:
        return

    contador = 0

    for i in range(len(lista)):
        contador += lista[i]
    return contador / len(lista)

print(promedio_lista(crear_lista()))