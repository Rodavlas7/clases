import os
from colorama import init, Fore, Style

# Inicializamos colorama
init(autoreset=True)

inventario = {
    1: {"nombre": "Normales", "limite": 10, "lista": []},
    2: {"nombre": "Portabebé", "limite": 5, "lista": []},
    3: {"nombre": "Pequeños", "limite": 5, "lista": []}
}

def limpiar_pantalla():
    # Comando 'clear' específico para Ubuntu/Linux/macOS. 
    # (Si quisieras que también funcionara en Windows, usarías 'cls').
    os.system('clear')

# Limpiamos la pantalla por primera vez al iniciar el programa
limpiar_pantalla()

while True:
    print(f"\n{Fore.CYAN}{Style.BRIGHT}--- SISTEMA DE CARRITOS ---")
    print("1. Ingresar carrito")
    print("2. Retirar carrito")
    print("3. Carritos totales")
    print(f"{Fore.RED}4. Salir")

    try:
        opcion = int(input(f"\n{Fore.MAGENTA}Seleccione una opcion: {Style.RESET_ALL}"))
    except ValueError:
        print(f"{Fore.RED}{Style.BRIGHT}Error: Por favor, ingrese un número válido.")
        input(f"\n{Fore.WHITE}Presione Enter para continuar...")
        limpiar_pantalla()
        continue

    # 1. INGRESAR CARRITO
    if opcion == 1:
        limpiar_pantalla()
        print(f"\n{Fore.CYAN}Tipo de carrito a ingresar:")
        for key, value in inventario.items():
            print(f"{key}. {value['nombre'][:-1] if value['nombre'].endswith('s') else value['nombre']}")
        
        try:
            tipo = int(input(f"\n{Fore.MAGENTA}Seleccione tipo: {Style.RESET_ALL}"))
            if tipo not in inventario:
                print(f"{Fore.RED}Opción de tipo no válida.")
            else:    
                codigo = input(f"{Fore.MAGENTA}Ingrese código del carrito: {Style.RESET_ALL}")
                categoria = inventario[tipo]
                
                if len(categoria["lista"]) < categoria["limite"]:
                    categoria["lista"].append(codigo)
                    print(f"\n{Fore.GREEN}✓ Carrito '{codigo}' agregado. Posición en fila: {len(categoria['lista'])}")
                else:
                    print(f"\n{Fore.YELLOW}⚠ La fila de carritos {categoria['nombre'].lower()} está llena.")
                    
        except ValueError:
            print(f"\n{Fore.RED}{Style.BRIGHT}Error: Ingrese un número válido para el tipo.")

    # 2. RETIRAR CARRITO
    elif opcion == 2:
        limpiar_pantalla()
        print(f"\n{Fore.CYAN}Tipo de carrito a retirar:")
        for key, value in inventario.items():
            print(f"{key}. {value['nombre'][:-1] if value['nombre'].endswith('s') else value['nombre']}")
            
        try:
            tipo = int(input(f"\n{Fore.MAGENTA}Seleccione tipo: {Style.RESET_ALL}"))
            if tipo not in inventario:
                print(f"\n{Fore.RED}Opción de tipo no válida.")
            else:    
                categoria = inventario[tipo]
                
                if categoria["lista"]:
                    carrito = categoria["lista"].pop()
                    print(f"\n{Fore.GREEN}✓ Se retiró el carrito: {carrito}")
                else:
                    print(f"\n{Fore.YELLOW}⚠ No hay carritos {categoria['nombre'].lower()} disponibles.")
                    
        except ValueError:
            print(f"\n{Fore.RED}{Style.BRIGHT}Error: Ingrese un número válido.")

    # 3. MOSTRAR INVENTARIO
    elif opcion == 3:
        limpiar_pantalla()
        print(f"\n{Fore.CYAN}{Style.BRIGHT}--- CARRITOS DISPONIBLES ---")
        for key, value in inventario.items():
            print(f"{Style.BRIGHT}{value['nombre']}: {Fore.YELLOW}{len(value['lista'])} {Fore.WHITE}{value['lista']}")

    # 4. SALIR
    elif opcion == 4:
        limpiar_pantalla()
        print(f"{Fore.CYAN}Saliendo del sistema... ¡Hasta luego!\n")
        break

    else:
        print(f"\n{Fore.RED}Opción no válida. Elija un número del 1 al 4.")

    # Pausa antes de limpiar y volver al menú principal
    input(f"\n{Fore.WHITE}Presione Enter para continuar...")
    limpiar_pantalla()