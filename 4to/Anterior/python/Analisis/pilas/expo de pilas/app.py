import os
from colorama import init, Fore, Style 
from carrito import Carrito
from pilaCarritos import PilaCarritos

init(autoreset=True)

def limpiar():
    os.system('cls' if os.name == 'nt' else 'clear')

def repetir():
    return input(Fore.YELLOW + "\n¿Desea repetir el proceso? (s/n): " + Style.RESET_ALL).lower() == 's'

# --- Creación de las 3 pilas con su capacidad máxima ---
normales = PilaCarritos(10)
bebe = PilaCarritos(5)
pequenos = PilaCarritos(5)

contador = 1

def seleccionar_tipo():
    print(Fore.CYAN + "\nSeleccione el tipo de carrito:")
    print("1. Normal")
    print("2. Portabebés")
    print("3. Pequeño")

    opcion = input(Fore.YELLOW + "Opción: " + Style.RESET_ALL)

    if opcion == "1":
        return normales, "Normal"
    elif opcion == "2":
        return bebe, "Portabebés"
    elif opcion == "3":
        return pequenos, "Pequeño"
    else:
        return None, None

while True:
    limpiar()
    print(Fore.CYAN + Style.BRIGHT + "===== SISTEMA DE CARRITOS =====")
    print("1. Ingresar carrito")
    print("2. Retirar carrito")
    print("3. Carritos totales")
    print(Fore.RED + "4. Salir")

    opcion = input(Fore.YELLOW + "\nSeleccione una opción: " + Style.RESET_ALL)

    # --- OPCIÓN 1: PUSH ---
    if opcion == "1":
        while True:
            limpiar()
            pila, tipo = seleccionar_tipo()

            if pila is None:
                print(Fore.RED + "Tipo inválido")
                break

            if pila.esta_llena(): # Evita desbordamiento (Stack Overflow)
                print(Fore.RED + "\nNo hay espacio disponible en esta fila.")
            else:
                codigo = f"C{contador}"
                carrito = Carrito(codigo, tipo)

                pila.push(carrito) # Agrega el carrito a la fila

                print(Fore.GREEN + f"\nCarrito agregado en posición {pila.tope + 1}")
                print(Fore.GREEN + f"Código asignado: {codigo}")

                if pila.esta_llena():
                    print(Fore.YELLOW + "La fila se ha llenado.")

                contador += 1

            if not repetir():
                break

    # --- OPCIÓN 2: POP ---
    elif opcion == "2":
        while True:
            limpiar()
            pila, tipo = seleccionar_tipo()

            if pila is None:
                print(Fore.RED + "Tipo inválido")
                break

            carrito = pila.pop() # Lógica LIFO: Last In, First Out

            if carrito is None: # Evita Underflow
                print(Fore.RED + "\nNo hay carritos disponibles para retirar.")
            else:
                print(Fore.GREEN + f"\nSe retiró el carrito {carrito.codigo}")
                print(Fore.GREEN + f"Ocupaba la posición {pila.tope + 2}")

            if not repetir():
                break

    # --- OPCIÓN 3: MOSTRAR ---
    elif opcion == "3":
        limpiar()
        print(Fore.CYAN + Style.BRIGHT + "===== CARRITOS DISPONIBLES =====")

        print(Fore.MAGENTA + "\nCarritos Normales:", normales.total())
        normales.mostrar()

        print(Fore.MAGENTA + "\nCarritos Portabebés:", bebe.total())
        bebe.mostrar()

        print(Fore.MAGENTA + "\nCarritos Pequeños:", pequenos.total())
        pequenos.mostrar()

        input(Fore.YELLOW + "\nPresione ENTER para regresar al menú..." + Style.RESET_ALL)

    # --- OPCIÓN 4: SALIR ---
    elif opcion == "4":
        print(Fore.CYAN + "\nSaliendo del sistema... ¡Hasta luego!")
        break

    else:
        print(Fore.RED + "Opción inválida. Intente de nuevo.")