class Nodo():
    def __init__(self, dato, posicion = None, siguiente = None):
        self.__dato = dato
        self.__posicion = posicion
        self.__siguiente = siguiente

    @property
    def dato(self):
        return self.__dato
    
    @dato.setter
    def dato(self, dato):
        self.__dato =  dato

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
        self.__siguiente =  siguiente

    def __str__(self):
        return f"Dato: {self.__dato}\n Posicion: {self.__posicion}\n Siguiente: {self.__siguiente}"
    
class lista():
    def __init__(self):
        self.__cantidad = 0
        self.__raiz = None

    def insertar(self, nodo, posicion = None):
        if type(nodo) != Nodo:
            print('Debe ingresar un nodo')
            return

        if self.__raiz == None:
            self.__raiz = nodo
            self.__raiz.posicion = 1
            self.__cantidad += 1
            return
        
        elif posicion == None:
            n = self.__raiz

            while n.siguiente != None: #Para tomar el ultimo
                n = n.siguiente

            self.__cantidad += 1
            nodo.posicion = self.__cantidad
            n.siguiente = nodo
            return
        
        elif type(posicion) == int & posicion >= 0:
            n = self.__raiz
            existe = None

            for i in range(self.__cantidad): #Para buscar el de la posicion
                if posicion == n.posicion:
                    existe = n
                    break
                else:
                    if n.siguiente != None:
                        n = n.siguiente
            if existe != True: #Si existe lo pondra despues de el de la posicion dicha
                existe
                
        return


l =  lista()
n1 = Nodo(1)
n2 = Nodo(2)

l.insertar(n1)
l.insertar(n2)