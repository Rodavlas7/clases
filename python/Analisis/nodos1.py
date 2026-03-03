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


    
    def mostrarReves(self):
        if self.__cantidad == 0:
            return
        nodo_actual = self.__raiz
        while nodo_actual.siguiente is not None:
            nodo_actual = self.buscar(nodo_actual.siguiente)

        while nodo_actual is not None:
            print(nodo_actual)
            nodo_actual = self.buscar(nodo_actual.anterior)



    def buscar(self, posicion):
        if self.__cantidad == 0:
            return None
        for i in self.__nodos:
            if i.posicion == posicion:
                return i
        return None
    

    
    def buscar_por_dato(self, dato):
        if self.__cantidad == 0:
            return None
        for i in self.__nodos:
            if i.dato == dato:
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


m = memoria()

# Agregamos 5 nodos
for x in [10, 20, 30, 40, 50]:
    m.agregar_final(nodo(x))
    
print("--- Mostrar normal (Adelante hacia atrás) ---")
m.mostrar()

print("\n--- Mostrar al revés (Atrás hacia adelante) ---")
m.mostrarReves()