def mostrar_lista(lista):
    if len(lista) == 0:
        print("La lista está vacía.")
        return
    for elemento in lista:
        print(elemento)

def buscar_elemento(lista, elemento):
    if len(lista) == 0:
        print("La lista está vacía.")
        return False
    for i in range(len(lista)):
        if lista[i] == elemento:
            return True
    return False

def calcular_promedio(lista):
    if len(lista) == 0:
        print("La lista está vacía.")
        return
    contador = 0
    for i in range(len(lista)):
        contador += lista[i]
    return contador / len(lista)

def eliminar_elemento(lista, elemento):
    if len(lista) == 0:
        print("La lista está vacía.")
        return
    for i in range(len(lista)):
        if lista[i] == elemento:
            del lista[i]
            return
        
def main():
    lista = []
    while True:
        print("\n\nMenú:")
        print("1) Agregar elemento")
        print("2) Eliminar elemento")
        print("3) Mostrar lista")
        print("4) Buscar elemento")
        print("5) Mostrar promedio")
        print("6) Salir")
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            elemento = int(input("Ingrese el elemento a agregar: "))
            lista.append(elemento)
        elif opcion == "2":
            elemento = int(input("Ingrese el elemento a eliminar: "))
            eliminar_elemento(lista, elemento)
        elif opcion == "3":
            mostrar_lista(lista)
        elif opcion == "4":
            elemento = int(input("Ingrese el elemento a buscar: "))
            if buscar_elemento(lista, elemento):
                print("Elemento encontrado.")
            else:
                print("Elemento no encontrado.")
        elif opcion == "5":
            promedio = calcular_promedio(lista)
            if promedio is not None:
                print(f"El promedio es: {promedio}")
        elif opcion == "6":
            break
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()