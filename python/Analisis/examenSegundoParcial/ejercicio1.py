class Nodo:
    def __init__(self, valor):
        self.__valor = valor
        self.__posicion = None
        self.__siguiente = None
    
    @property
    def valor(self):
        return self.__valor
    
    @valor.setter
    def valor(self, valor):
        self.__valor =  valor

    @property
    def posicion(self):
        return self.__posicion
    
    @posicion.setter
    def posicion(self, posicion):
        self.__posicion =  posicion

    @property
    def siguiente(self):
        return self.__siguiente
    
    @siguiente.setter
    def siguiente(self, siguiente):
        self.__siguiente = siguiente

    def __str__(self):
        if self.__siguiente != None:
            postexto = self.siguiente.posicion
        else:
            postexto = None
        return f"Valor: {self.__valor}\n Posicion: {self.__posicion}\n Siguiente: {postexto}"
    
class lista:
    def __init__(self):
        self.__raiz = None
        self.__cantidad = 0

    def agregar(self, nodo, posicion = None):

        if type(nodo) != Nodo:
            nodo = Nodo(nodo)

        if self.__raiz == None:
            self.__cantidad += 1

            self.__raiz = nodo
            self.__raiz.posicion = self.__cantidad
            return True
        
        n = self.__raiz

        if posicion == None:

            while n.siguiente != None:
                n = n.siguiente
            
            self.__cantidad += 1
            
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
                


    def buscar(self, valor):
        if self.__raiz == None or self.__cantidad == 0:
            return
        
        n = self.__raiz

        while n != None:
            if n.valor == valor:
                return n
            n = n.siguiente
        return None



    def eliminar(self, posicion):
        if self.__raiz == None or self.__cantidad == 0:
            return
        
        n = self.__raiz

        if posicion == self.__raiz.posicion:
            self.__raiz = self.__raiz.siguiente

        while n.siguiente != None:
            if n.siguiente.posicion == posicion:
                n.siguiente = n.siguiente.siguiente
                return True
            n = n.siguiente
        return False




    def mostrar(self):
        if self.__raiz == None or self.__cantidad == 0:
            print("\nNo hay lista\n")
            return
        
        n = self.__raiz

        while n != None:
            print(n)
            n = n.siguiente



def viejomain():
    valores = [10,20,30,40,50,60,70]
    l = lista()

    for i in valores:
        l.agregar(Nodo(i))
    
    l.mostrar()

    nodo40 = l.buscar(40)

    print("\n\neliminando 40\n")
    l.eliminar(nodo40.posicion)

    l.mostrar()

    print("\n\neliminando insertando entre 60 y 70\n")
    l.agregar(Nodo(65),6)
    l.mostrar()



if __name__ == "__main__":
    valores = [10,20,30,40,50,60,70]
    l = lista()

    for i in valores:
        l.agregar(Nodo(i))
    
    print("Bienvenido al menu de nodo simple:")
    while True:
        print("Presione 1 para mostrar\nPresione 2 para agregar un nuevo nodo al final de la lista\nPresione 3 para agregar un nuevo nodo en alguna posicion especifica de la lista\nPresione 4 para eliminar un nodo\nPresione 5 para buscar un nodo en base a su valor\nPresione 0 para salir\n")
        respuesta =  int(input("Numero: "))

        if respuesta == 1:
            print()
            print()
            l.mostrar()
            print()
            print()
        elif respuesta == 2:
            l.agregar(input("Deme el valor para insertar"))
        elif respuesta == 3:
            l.agregar(input("Deme el valor para insertar: "),int(input("Deme la posicion para colocarlo despues de ese nodo: ")))
        elif respuesta == 4:
            opcion = int(input("1 para eliminar buscando con su valor\n2 para eliminar buscando con su posicion\n"))
            if opcion == 1:
                l.eliminar(l.buscar(int(input("valor: "))).posicion)
            elif opcion == 2:
                l.eliminar(int(input("posicion: ")))
            else:
                print("valor invalido")
        elif respuesta == 5:
            encontro = l.buscar(int(input("Valor que quiere buscar :")))
            if encontro != None:
                print(encontro)
            else:
                print("No se encontro")
        elif respuesta == 0:
            break
        else:
            print("Respuesta invalida")