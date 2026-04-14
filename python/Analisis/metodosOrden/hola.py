"""Proceso OrdenamientoBurbuja
	Definir i, j, n, temp Como Entero
	Dimension lista[5]
	
	lista[1] <- 5
	lista[2] <- 4
	lista[3] <- 3
	lista[4] <- 2
	lista[5] <- 1
	
	n <- 5
	
	Para i <- 1 Hasta n-1 Hacer
		Para j <- 1 Hasta n-i Hacer
			Si lista[j] > lista[j+1] Entonces
				temp <- lista[j]
				lista[j] <- lista[j+1]
				lista[j+1] <- temp
			FinSi
		FinPara
	FinPara
	
	Escribir "Lista ordenada:"
	
	Para i <- 1 Hasta n Hacer
		Escribir lista[i]
	FinPara
FinProcesoÓN"""

def ordenamiento_burbuja(lista):
    l = len(lista)
    for i in range(l):
        for j in range(l - 1 - i):
            if lista[j] > lista[j+1]: 
                # Intercambio de variables en una sola

                lista[j], lista[j+1] = lista[j+1], lista[j]
                
                # Muestra la lista paso a paso
                print(f"Intercambio: {lista}")                
                
    return lista



if __name__ == "__main__":
    numeros_desordenados = [5, 2, 9, 1, 5, 6]
    
    print(f"Lista original: {numeros_desordenados}")
    print("-" * 30)
    
    lista_final = ordenamiento_burbuja(numeros_desordenados)
    
    print("-" * 30)
    print(f"Lista final ordenada: {lista_final}")