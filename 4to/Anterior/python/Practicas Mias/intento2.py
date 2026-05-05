class Nodo():
    def __init__(self, valor):
        self.__valor = valor
        self.__siguiente = None
        self.__posicion = None

    @property
    def valor(self):
        return self.__valor
    
    @valor.setter
    def valor(self, valor):
        self.__valor = valor

    @property
    def siguiente(self):
        return self.__siguiente
    
    @siguiente.setter
    def siguiente(self, siguiente):
        self.__siguiente =  siguiente

    @property
    def posicion(self):
        return self.__posicion
    
    @posicion.setter
    def posicion(self, posicion):
        self.__posicion =  posicion

    def __str__(self):
        if self.__siguiente != None:
            sig_info = self.__siguiente.posicion
        else:
            sig_info = "None"
            
        return f"Valor: {self.__valor} | Posicion: {self.__posicion} | Siguiente (Pos): {sig_info}"

class Memoria():
    def __init__(self):
        self.__raiz = None
        self.__cantidad = 0
        


    def agregar(self, nodo, posicion = None):

        if type(nodo) != Nodo:
            return False
        
        if self.__raiz == None:
                self.__raiz = nodo
                self.__cantidad += 1
                self.__raiz.posicion = self.__cantidad
                return True

        n = self.__raiz

        if posicion ==  None:
            self.__cantidad += 1

            while n.siguiente != None:
                n = n.siguiente

            nodo.posicion = self.__cantidad
            n.siguiente = nodo

        else:

            while n != None:
                if n.posicion == posicion:

                    self.__cantidad += 1
                    nodo.posicion = self.__cantidad
                    nodo.siguiente = n.siguiente
                    n.siguiente = nodo
                    return True

                n = n.siguiente
            return False



    def buscarPosicion(self, posicion):
        n = self.__raiz
        while n != None:
            if n.posicion == posicion:
                return n
            n = n.siguiente



    def buscarValor(self, valor):
        n = self.__raiz
        while n != None:
            if n.valor == valor:
                return n
            n = n.siguiente



    def eliminar(self, posicion):
        if self.__raiz == None:
            return
        
        n =  self.__raiz

        while n.siguiente != None:
            if n.siguiente.posicion == posicion:
                n.siguiente =  n.siguiente.siguiente
                return
            n = n.siguiente



    def mostrar(self):
        if self.__raiz == None:
            print('No hay nodos') 
            return
        
        n = self.__raiz

        while n != None:
            print(n)
            n = n.siguiente



if __name__ == "__main__":
    lista = Memoria()

    # 1. Crear la lista: 15, 25, 30, 45, 55, 61, 80
    valores = [15, 25, 30, 45, 55, 61, 80]
    for v in valores:
        lista.agregar(Nodo(v))

    print(">>> 1. MUESTRA LISTA CREADA:")
    lista.mostrar()

    # 2. Eliminar nodo que contiene el valor 45
    print("\n>>> 2. ELIMINANDO EL NODO CON VALOR 45...")
    nodo_a_borrar = lista.buscarValor(45) # Primero lo buscamos
    if nodo_a_borrar != None:
        lista.eliminar(nodo_a_borrar.posicion) # Luego usamos su posición para borrarlo
    lista.mostrar()

    # 3. Inserte un nodo con valor 65 entre 61 y 80
    print("\n>>> 3. INSERTANDO NODO 65 ENTRE 61 Y 80...")
    # Para insertarlo entre el 61 y el 80, lo agregamos DESPUÉS del 61.
    nodo_61 = lista.buscarValor(61)
    if nodo_61 != None:
        lista.agregar(Nodo(65), nodo_61.posicion)
    lista.mostrar()

    