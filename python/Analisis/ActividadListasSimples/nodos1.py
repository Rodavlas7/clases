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
    

    def elminar(self, posicion):
        if self.__cantidad == 0:
            return
        
        for anterior in self.__nodos:
            if anterior.siguiente == posicion:

                for siguiente in self.__nodos:
                    if siguiente.anterior == posicion:

                        for elim in self.__nodos:
                            if elim.posicion == posicion:
                                anterior.siguiente = elim.siguiente
                                siguiente.anterior = elim.anterior

                                elim.siguiente = None
                                elim.anterior = None

                                self.__cantidad =- 1
                                
                                return 'nodo eliminado'

        return 'No se encontro el nodo'

                



def main():
    memoria1 = memoria()
    for i in range(5):
        nodo1 = nodo(i)
        memoria1.agregar_final(nodo1)
    memoria1.mostrar()
    memoria1.elminar(3)
    print("\n\n\n\n")
    memoria1.mostrar()

if __name__ == "__main__":    
    main()