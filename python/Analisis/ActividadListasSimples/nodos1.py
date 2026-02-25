import random

class nodo:
    def __init__(self, dato, siguiente = None, posicion = None, anterior = None):
        self.__dato = dato
        self.__siguiente = siguiente
        self.__posicion = posicion
        self.__anterior = anterior

    @property
    def posicion(self):
        return self.__posicion
    
    @posicion.setter
    def posicion(self, posicion):
        self.__posicion = posicion

    @property
    def siguiente(self):
        return self.__siguiente
    
    @siguiente.setter
    def siguiente(self, siguiente):
        self.__siguiente = siguiente

    @property
    def anterior(self):
        return self.__anterior
    
    @anterior.setter
    def anterior(self, anterior):
        self.__anterior = anterior

    @property
    def dato(self):
        return self.__dato
    
    @dato.setter
    def dato(self, dato):
        self.__dato = dato

    def __str__(self):
        return f"Tiene valor de: {self.__dato} \n Tiene posicion de: {self.__posicion} \n Tiene siguiente: {self.__siguiente}\n Tiene anterior: {self.__anterior}\n"

class memoria: 
    def __init__(self): 
        self.__raiz = None
        self.__nodos = []
        self.__cantidad = 0
        self.__posicionmax = 0


    def agregar_final(self, nodo):
        nodo.posicion = self.__posicionmax
        self.__posicionmax = nodo.posicion + 1
        
        if self.__cantidad == 0:
            self.__raiz = nodo
            self.__nodos.append(nodo)
            self.__cantidad += 1
            return  
        else:
            self.__nodos.append(nodo)
            self.__nodos[self.__cantidad - 1].siguiente = nodo.posicion
            nodo.anterior = self.__nodos[self.__cantidad - 1].posicion
            self.__cantidad += 1
            return
        
        
    def mostrar(self):
        if self.__cantidad == 0:
            return
        nodo_actual = self.__raiz
        while nodo_actual is not None:
            print(nodo_actual)
            nodo_actual = self.buscar(nodo_actual.siguiente)

    
    def buscar(self, posicion):
        if self.__cantidad == 0:
            return None
        for i in self.__nodos:
            if i.posicion == posicion:
                return i
        return None
    

    def eliminar(self, posicion):
        if self.__cantidad == 0:
            return "Lista vacía"

        eliminado = None

        # buscar nodo a eliminar
        for elim in self.__nodos:
            if elim.posicion == posicion:
                eliminado = elim
                break

        if eliminado is None:
            return "No se encontró el nodo"

        for anterior in self.__nodos:

            if anterior.siguiente == posicion:

                for siguiente in self.__nodos:

                    if siguiente.anterior == posicion:

                        anterior.siguiente = eliminado.siguiente
                        siguiente.anterior = eliminado.anterior



        # si es la raíz
        if eliminado == self.__raiz:
            self.__raiz = self.buscar(eliminado.siguiente)

        # si es último
        if eliminado.siguiente is None:
            for anterior in self.__nodos:
                if anterior.siguiente == posicion:
                    anterior.siguiente = None

        eliminado.siguiente = None
        eliminado.anterior = None

        self.__nodos.remove(eliminado)
        self.__cantidad -= 1   

        return "Nodo eliminado"




    def agregar_despues(self, posicion, nodo):
        base = self.buscar(posicion)
        if base is None:
            return "Posición no encontrada"

        nodo.posicion = self.__posicionmax
        self.__posicionmax += 1

        siguiente = self.buscar(base.siguiente)

        nodo.anterior = base.posicion
        nodo.siguiente = base.siguiente

        base.siguiente = nodo.posicion

        if siguiente:
            siguiente.anterior = nodo.posicion

        self.__nodos.append(nodo)
        self.__cantidad += 1

        return "Nodo insertado"



# -----------------------------------------------------
# Ejercicio 1
# Insertar 10, 20, 30 y mostrar
# -----------------------------------------------------
def ejercicio1():
    m = memoria()
    for x in [10, 20, 30]:
        m.agregar_final(nodo(x))
    m.mostrar()


# -----------------------------------------------------
# Ejercicio 2
# Insertar 5 números y mostrar
# -----------------------------------------------------
def ejercicio2():
    m = memoria()
    for x in [5, 8, 2, 9, 1]:
        m.agregar_final(nodo(x))
    m.mostrar()


# -----------------------------------------------------
# Ejercicio 3
# Insertar 1..5 y eliminar el 3
# -----------------------------------------------------
def ejercicio3():
    m = memoria()
    for x in [1, 2, 3, 4, 5]:
        m.agregar_final(nodo(x))

    for n in m._memoria__nodos:
        if n.dato == 3:
            m.eliminar(n.posicion)
            break

    m.mostrar()


# -----------------------------------------------------
# Ejercicio 4
# Buscar el número 14
# -----------------------------------------------------
def ejercicio4():
    m = memoria()
    for x in [7, 14, 21]:
        m.agregar_final(nodo(x))

    encontrado = False
    for n in m._memoria__nodos:
        if n.dato == 14:
            encontrado = True

    print("Encontrado" if encontrado else "No encontrado")


# -----------------------------------------------------
# Ejercicio 5
# Eliminar en lista vacía
# -----------------------------------------------------
def ejercicio5():
    m = memoria()
    print(m.eliminar(0))


# -----------------------------------------------------
# Ejercicio 6
# Eliminar primer nodo
# -----------------------------------------------------
def ejercicio6():
    m = memoria()
    for x in [100, 200, 300]:
        m.agregar_final(nodo(x))

    m.eliminar(m._memoria__raiz.posicion)
    m.mostrar()


# -----------------------------------------------------
# Ejercicio 7
# Eliminar último nodo
# -----------------------------------------------------
def ejercicio7():
    m = memoria()
    for x in [8, 16, 24, 32]:
        m.agregar_final(nodo(x))

    ultimo = m._memoria__nodos[-1]
    m.eliminar(ultimo.posicion)
    m.mostrar()


# -----------------------------------------------------
# Ejercicio 8
# Buscar número inexistente
# -----------------------------------------------------
def ejercicio8():
    m = memoria()
    for x in [1, 2, 3, 4, 5, 6]:
        m.agregar_final(nodo(x))

    print(m.buscar(999))


# -----------------------------------------------------
# Ejercicio 9
# Mostrar solo pares
# -----------------------------------------------------
def ejercicio9():
    m = memoria()
    for i in range(1, 11):
        m.agregar_final(nodo(i))

    actual = m._memoria__raiz
    while actual:
        if actual.dato % 2 == 0:
            print(actual.dato)
        actual = m.buscar(actual.siguiente)


# -----------------------------------------------------
# Ejercicio 10
# Lista con nombres
# -----------------------------------------------------
def ejercicio10():
    m = memoria()
    for nombre in ["Ana", "Luis", "Pedro", "Sofía", "Marta"]:
        m.agregar_final(nodo(nombre))
    m.mostrar()


# -----------------------------------------------------
# Ejercicio 11
# Agregar uno más al final
# -----------------------------------------------------
def ejercicio11():
    m = memoria()
    for x in [1, 2, 3, 4]:
        m.agregar_final(nodo(x))

    print("ANTES")
    m.mostrar()

    print("DESPUÉS")
    m.agregar_final(nodo(99))
    m.mostrar()


# -----------------------------------------------------
# Ejercicio 12
# Eliminar primera aparición de 4
# -----------------------------------------------------
def ejercicio12():
    m = memoria()
    for x in [2, 4, 4, 6]:
        m.agregar_final(nodo(x))

    for n in m._memoria__nodos:
        if n.dato == 4:
            m.eliminar(n.posicion)
            break

    m.mostrar()


# -----------------------------------------------------
# Ejercicio 13
# Contar nodos recorriendo
# -----------------------------------------------------
def ejercicio13():
    m = memoria()
    for x in [10, 20, 30]:
        m.agregar_final(nodo(x))

    contador = 0
    actual = m._memoria__raiz
    while actual:
        contador += 1
        actual = m.buscar(actual.siguiente)

    print("Total nodos:", contador)


# -----------------------------------------------------
# Ejercicio 14
# Eliminar todos uno por uno
# -----------------------------------------------------
def ejercicio14():
    m = memoria()
    for x in [1, 2, 3, 4, 5]:
        m.agregar_final(nodo(x))

    while m._memoria__cantidad > 0:
        pos = m._memoria__raiz.posicion
        m.eliminar(pos)
        print("Estado actual:")
        m.mostrar()


# -----------------------------------------------------
# Ejercicio 15
# Menú interactivo
# -----------------------------------------------------
def ejercicio15():
    m = memoria()

    while True:
        op = input("1 insertar | 2 eliminar | 3 mostrar | 0 salir: ")

        if op == "1":
            x = int(input("valor: "))
            m.agregar_final(nodo(x))

        elif op == "2":
            x = int(input("posicion: "))
            print(m.eliminar(x))

        elif op == "3":
            m.mostrar()

        elif op == "0":
            break


# =====================================================
# EJECUCIÓN
# Activa SOLO UNO a la vez
# =====================================================

if __name__ == "__main__":

    ejercicio1()
    #ejercicio2()
    #ejercicio3()
    #ejercicio4()
    #ejercicio5()
    #ejercicio6()
    #ejercicio7()
    #ejercicio8()
    #ejercicio9()
    #ejercicio10()
    #ejercicio11()
    #ejercicio12()
    #ejercicio13()
    #ejercicio14()
    #ejercicio15()