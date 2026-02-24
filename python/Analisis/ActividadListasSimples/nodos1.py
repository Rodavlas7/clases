import random

class nodo:
    def __init__(self, dato, siguiente = None, posicion = None):
        self.__dato = dato
        self.__siguiente = siguiente

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
    def dato(self):
        return self.__dato
    
    @dato.setter
    def dato(self, dato):
        self.__dato = dato

    def __str__(self):
        return f"Tiene valor de: {self.__dato} \n Tiene posicion de: {self.__posicion} \n Tiene siguiente: {self.__siguiente}\n"

class memoria: 
    def __init__(self): 
        self.__raiz = None
        self.__nodos = []
        self.__cantidad = 0
        self.__posicionmax = 0

    def agregar(self, nodo):
        nodo.posicion = random.randint(self.__posicionmax, self.__posicionmax + 10)
        self.__posicionmax = nodo.posicion + 1

        if self.__cantidad == 0:
            self.__raiz = nodo
            self.__nodos.append(nodo)
            self.__cantidad += 1
            return
        else:
            self.__nodos.append(nodo)
            self.__nodos[self.__cantidad - 1].siguiente = nodo.posicion
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

def main():
    memoria1 = memoria()
    for i in range(5):
        nodo1 = nodo(i)
        memoria1.agregar(nodo1)
    memoria1.mostrar()

if __name__ == "__main__":    
    main()