
import time  # solo para pequeñas animaciones de pausas


## Pequeña cartelera ##

cartelera = [
    {
        "id": 1,
        "titulo": "Dune: Parte Tres",
        "horario": "4:00 PM",
        "sala": "Sala A",
        "precio": 85.00,
        "asientos_totales": 10
    },
    {
        "id": 2,
        "titulo": "Mision Imposible 8",
        "horario": "6:30 PM",
        "sala": "Sala B",
        "precio": 90.00,
        "asientos_totales": 10
    },
    {
        "id": 3,
        "titulo": "El Senor de los Anillos: La Guerra",
        "horario": "9:00 PM",
        "sala": "Sala C",
        "precio": 95.00,
        "asientos_totales": 10
    }
]

## Pelicula para preventa ##

preventa_info = {
    "titulo": "Avatar 3: El Ultimo Cielo",
    "fecha_estreno": "15 de Agosto, 2025",
    "precio_estimado": 110.00
}

## Estructuras de datos para el sistema de boletos ##

# COLA: clientes esperando en la fila para ser atendidos
fila_clientes = []

# COLA DE PREVENTA: clientes anotados para la proxima preventa
fila_preventa = []

# PILA: historial de transacciones completadas
historial_transacciones = []

# Lista de todos los boletos vendidos (para ordenar y buscar)
boletos_vendidos = []

# Contador global para IDs de boletos
id_boleto_actual = 1

# Contador para IDs de registro en preventa
id_preventa_actual = 1

# Asientos ocupados por pelicula
asientos_ocupados = {1: [], 2: [], 3: []}


## Funciones para cola ##

def encolar_cliente(nombre, id_cliente):
    # meto al cliente al final de la fila
    cliente = {"id_cliente": id_cliente, "nombre": nombre}
    fila_clientes.append(cliente)

def desencolar_cliente():
    # saco al primero de la fila
    if len(fila_clientes) == 0:
        return None
    return fila_clientes.pop(0)


## Cola en preventa ##

def encolar_preventa(nombre, contacto):
    global id_preventa_actual
    # registro al cliente en la fila de preventa con su contacto (correo o tel)
    registro = {
        "id_preventa": id_preventa_actual,
        "nombre": nombre,
        "contacto": contacto
    }
    fila_preventa.append(registro)
    id_preventa_actual += 1
    return registro

def cancelar_preventa(id_p):
    # busco y saco al cliente de la fila de preventa si decide cancelar
    for i in range(len(fila_preventa)):
        if fila_preventa[i]["id_preventa"] == id_p:
            cancelado = fila_preventa.pop(i)
            return cancelado
    return None  # no lo encontre



## VER AMBAS FILAS (cola normal + cola preventa) ""


def ver_fila():
    # se muestran las dos colas juntas para tener una vista completa del estado
    print("\n  " + "="*48)
    print("   ESTADO DE FILAS")
    print("  " + "="*48)

    # --- fila de atencion normal ---
    print(f"\n  [FILA DE ATENCION ACTUAL]  ({len(fila_clientes)} personas)")
    print("  " + "-"*48)
    if len(fila_clientes) == 0:
        print("  (nadie esperando en este momento)")
    else:
        for i in range(len(fila_clientes)):
            c = fila_clientes[i]
            # indico quien es el siguiente a ser atendido
            etiqueta = "  <-- siguiente" if i == 0 else ""
            print(f"  {i+1}. [{c['id_cliente']}] {c['nombre']}{etiqueta}")

    # --- fila de preventa ---
    print(f"\n  [FILA DE PREVENTA]  ({len(fila_preventa)} registrados)")
    print(f"  Pelicula : {preventa_info['titulo']}")
    print(f"  Estreno  : {preventa_info['fecha_estreno']}  |  Precio aprox: ${preventa_info['precio_estimado']:.2f}")
    print("  " + "-"*48)
    if len(fila_preventa) == 0:
        print("  (nadie registrado en preventa todavia)")
    else:
        for i in range(len(fila_preventa)):
            p = fila_preventa[i]
            print(f"  {i+1}. [Preventa #{p['id_preventa']}] {p['nombre']}  —  {p['contacto']}")
    print("  " + "="*48)


## Flujo de registro en preventa (solo registro, no compra todavia) ##

def flujo_preventa():
    print("\n" + "="*52)
    print("   REGISTRO DE PREVENTA")
    print("="*52)
    print(f"\n  Proxima pelicula: {preventa_info['titulo']}")
    print(f"  Fecha de estreno: {preventa_info['fecha_estreno']}")
    print(f"  Precio estimado : ${preventa_info['precio_estimado']:.2f}")
    print("\n  Al registrarte, tendras prioridad cuando")
    print("  abra la venta oficial. Te avisaremos por")
    print("  correo o telefono.")

    print("\n  " + "-"*40)
    nombre = input("  Tu nombre: ").strip()
    if nombre == "":
        print("  Necesitas escribir un nombre.")
        return
    contacto = input("  Correo o telefono de contacto: ").strip()
    if contacto == "":
        print("  Necesitas dejar un contacto.")
        return

    registro = encolar_preventa(nombre, contacto)
    print(f"\n  Listo! Quedaste registrado.")
    print(f"  Tu numero en la fila de preventa es: #{registro['id_preventa']}")
    print(f"  Posicion en fila: {len(fila_preventa)} de {len(fila_preventa)}")
    print(f"  Te contactaremos a: {contacto}")


## Funciones para pila (historial de transacciones) ##

def apilar_transaccion(transaccion):
    # el mas reciente queda hasta arriba
    historial_transacciones.append(transaccion)

def ver_historial():
    print("\n  === HISTORIAL DE TRANSACCIONES ===")
    if len(historial_transacciones) == 0:
        print("  (sin transacciones todavia)")
        return
    # muestro del mas reciente al mas antiguo
    for i in range(len(historial_transacciones) - 1, -1, -1):
        t = historial_transacciones[i]
        print(f"  Boleto #{t['id_boleto']} | {t['cliente']} | {t['pelicula']} | Asiento {t['asiento']} | ${t['total']:.2f}")


## Funciones para ordenamiento y busqueda de boletos ##

def ordenar_burbuja(lista):
    # hago copia para no tocar la original
    copia = []
    for x in lista:
        copia.append(x)

    n = len(copia)
    for i in range(n):
        for j in range(0, n - i - 1):
            if copia[j]["id_boleto"] > copia[j+1]["id_boleto"]:
                temp = copia[j]
                copia[j] = copia[j+1]
                copia[j+1] = temp
    return copia


## busqueda secuencial por ID de boleto ##

def buscar_boleto(id_buscado):
    # recorro uno por uno hasta encontrarlo o acabar
    for boleto in boletos_vendidos:
        if boleto["id_boleto"] == id_buscado:
            return boleto
    return None


## Funciones para mostrar cartelera y mapa de asientos ##

def mostrar_cartelera():
    print("\n  +--------------------------------------------------+")
    print("  |           CARTELERA DE HOY                      |")
    print("  +--------------------------------------------------+")
    for peli in cartelera:
        disponibles = peli["asientos_totales"] - len(asientos_ocupados[peli["id"]])
        print(f"  | [{peli['id']}] {peli['titulo']:<43}|")
        print(f"  |     Horario: {peli['horario']}  |  {peli['sala']}  |  ${peli['precio']:.2f}  |  Lugares: {disponibles}/10  |")
        print("  +--------------------------------------------------+")

def obtener_pelicula_por_id(id_peli):
    for peli in cartelera:
        if peli["id"] == id_peli:
            return peli
    return None

def asientos_libres(id_peli):
    ocupados = asientos_ocupados[id_peli]
    libres = []
    for num in range(1, 11):
        if num not in ocupados:
            libres.append(num)
    return libres

def mostrar_mapa_asientos(id_peli):
    ocupados = asientos_ocupados[id_peli]
    print("\n  Mapa de asientos  [N] = libre   X = ocupado")
    print("  +-----------+   +-----------+")
    fila1 = ""
    fila2 = ""
    for num in range(1, 6):
        if num in ocupados:
            fila1 += " X "
        else:
            fila1 += f"[{num}]"
    for num in range(6, 11):
        if num in ocupados:
            fila2 += " X "
        else:
            fila2 += f"[{num}]"
    print(f"  |{fila1}|   |{fila2}|")
    print("  +-----------+   +-----------+")
    print("         -- PANTALLA --\n")


## Flujo completo de compra de boleto (desde que el cliente llega hasta que se emite el boleto) ##

def flujo_compra():
    global id_boleto_actual

    print("\n" + "="*52)
    print("   BIENVENIDO A CINETOBI")
    print("="*52)

    # paso 1: pedir nombre y agregar a la fila
    nombre = input("\n  Como te llamas? ").strip()
    if nombre == "":
        nombre = "Cliente"
    id_c = f"C{len(fila_clientes) + len(historial_transacciones) + 1:03d}"
    encolar_cliente(nombre, id_c)
    print(f"\n  Hola {nombre}! Te agregamos a la fila. Tu ID es: {id_c}")
    print(f"  Posicion en fila: #{len(fila_clientes)}")
    time.sleep(1)

    # paso 2: llamar al cliente (desencolar)
    print("\n  Llamando al siguiente cliente...")
    time.sleep(1)
    cliente_actual = desencolar_cliente()
    print(f"  Es tu turno, {cliente_actual['nombre']}!")

    # paso 3: mostrar cartelera y elegir pelicula
    mostrar_cartelera()

    pelicula_elegida = None
    while pelicula_elegida is None:
        try:
            opcion = int(input("\n  Que pelicula quieres ver? (1, 2 o 3): "))
            pelicula_elegida = obtener_pelicula_por_id(opcion)
            if pelicula_elegida is None:
                print("  Esa opcion no existe.")
            else:
                libres = asientos_libres(opcion)
                if len(libres) == 0:
                    print(f"  Lo sentimos, '{pelicula_elegida['titulo']}' ya no tiene lugares. Elige otra.")
                    pelicula_elegida = None
        except:
            print("  Escribe un numero valido.")

    print(f"\n  Elegiste: {pelicula_elegida['titulo']} a las {pelicula_elegida['horario']}")

    # paso 4: elegir asiento
    mostrar_mapa_asientos(pelicula_elegida["id"])
    libres = asientos_libres(pelicula_elegida["id"])

    asiento_elegido = None
    while asiento_elegido is None:
        try:
            num = int(input(f"  Elige tu asiento {libres}: "))
            if num in libres:
                asiento_elegido = num
            else:
                print("  Ese asiento no esta disponible.")
        except:
            print("  Escribe un numero de asiento.")

    # paso 5: resumen y pago
    precio = pelicula_elegida["precio"]
    print(f"\n  ------------------------------------")
    print(f"  RESUMEN DE COMPRA")
    print(f"  ------------------------------------")
    print(f"  Pelicula : {pelicula_elegida['titulo']}")
    print(f"  Horario  : {pelicula_elegida['horario']}")
    print(f"  Sala     : {pelicula_elegida['sala']}")
    print(f"  Asiento  : {asiento_elegido}")
    print(f"  Total    : ${precio:.2f}")
    print(f"  ------------------------------------")

    confirmar = input("\n  Confirmas la compra? (s/n): ").strip().lower()
    if confirmar != "s":
        print("  Compra cancelada.")
        return

    # simulacion de pago
    print("\n  Procesando pago", end="")
    for _ in range(4):
        time.sleep(0.4)
        print(".", end="", flush=True)
    print()

    pago_valido = False
    while not pago_valido:
        try:
            pago = float(input(f"\n  Con cuanto pagas? $"))
            if pago < precio:
                print(f"  Pago insuficiente. El total es ${precio:.2f}.")
            else:
                pago_valido = True
        except:
            print("  Escribe un monto valido.")

    cambio = pago - precio
    print(f"  Pago recibido: ${pago:.2f}")
    print(f"  Cambio: ${cambio:.2f}")

    # paso 6: registrar el boleto
    asientos_ocupados[pelicula_elegida["id"]].append(asiento_elegido)

    boleto = {
        "id_boleto": id_boleto_actual,
        "id_cliente": cliente_actual["id_cliente"],
        "cliente": cliente_actual["nombre"],
        "pelicula": pelicula_elegida["titulo"],
        "horario": pelicula_elegida["horario"],
        "sala": pelicula_elegida["sala"],
        "asiento": asiento_elegido,
        "total": precio
    }
    boletos_vendidos.append(boleto)
    apilar_transaccion(boleto)

    print(f"\n  ====================================")
    print(f"  BOLETO #{id_boleto_actual} EMITIDO")
    print(f"  ====================================")
    print(f"  {cliente_actual['nombre']} — {pelicula_elegida['titulo']}")
    print(f"  Asiento {asiento_elegido} | {pelicula_elegida['horario']} | {pelicula_elegida['sala']}")
    print(f"  ====================================")

    id_boleto_actual += 1


## Menu de administracion para ver boletos vendidos, buscar por ID, ordenar, ver historial y estado de filas ##

def menu_admin():
    while True:
        print("\n" + "="*52)
        print("   PANEL DE ADMINISTRACION")
        print("="*52)
        print("  1. Ver todos los boletos vendidos")
        print("  2. Ver boletos por pelicula")
        print("  3. Buscar boleto por ID")
        print("  4. Ver boletos ordenados (algoritmo burbuja)")
        print("  5. Ver historial de transacciones (pila)")
        print("  6. Ver estado de filas (atencion + preventa)")
        print("  7. Cancelar registro de preventa")
        print("  0. Volver al menu principal")

        opcion = input("\n  Opcion: ").strip()

        if opcion == "1":
            print("\n  === TODOS LOS BOLETOS VENDIDOS ===")
            if len(boletos_vendidos) == 0:
                print("  No se ha vendido ningun boleto aun.")
            else:
                for b in boletos_vendidos:
                    print(f"  #{b['id_boleto']} | {b['cliente']} | {b['pelicula']} | Asiento {b['asiento']} | ${b['total']:.2f}")

        elif opcion == "2":
            mostrar_cartelera()
            try:
                id_p = int(input("  Boletos de cual pelicula? (1, 2 o 3): "))
                peli = obtener_pelicula_por_id(id_p)
                if peli is None:
                    print("  Pelicula no valida.")
                else:
                    print(f"\n  Boletos vendidos para '{peli['titulo']}':")
                    encontrado = False
                    for b in boletos_vendidos:
                        if b["pelicula"] == peli["titulo"]:
                            print(f"    #{b['id_boleto']} | {b['cliente']} | Asiento {b['asiento']}")
                            encontrado = True
                    if not encontrado:
                        print("  Ninguno todavia.")
            except:
                print("  Entrada no valida.")

        elif opcion == "3":
            try:
                id_buscar = int(input("  ID del boleto a buscar: "))
                resultado = buscar_boleto(id_buscar)
                if resultado is None:
                    print(f"  No se encontro el boleto #{id_buscar}.")
                else:
                    print(f"\n  Boleto encontrado:")
                    print(f"  Cliente  : {resultado['cliente']}")
                    print(f"  Pelicula : {resultado['pelicula']}")
                    print(f"  Horario  : {resultado['horario']}")
                    print(f"  Sala     : {resultado['sala']}")
                    print(f"  Asiento  : {resultado['asiento']}")
                    print(f"  Total    : ${resultado['total']:.2f}")
            except:
                print("  Ingresa un numero valido.")

        elif opcion == "4":
            if len(boletos_vendidos) == 0:
                print("  No hay boletos para ordenar.")
            else:
                ordenados = ordenar_burbuja(boletos_vendidos)
                print("\n  Boletos ordenados por ID (burbuja):")
                for b in ordenados:
                    print(f"  #{b['id_boleto']} | {b['cliente']} | {b['pelicula']} | Asiento {b['asiento']}")

        elif opcion == "5":
            ver_historial()

        elif opcion == "6":
            ver_fila()

        elif opcion == "7":
            # permite cancelar un registro de preventa buscando por id
            if len(fila_preventa) == 0:
                print("  No hay nadie en la fila de preventa.")
            else:
                ver_fila()
                try:
                    id_c = int(input("\n  Numero de preventa a cancelar: "))
                    cancelado = cancelar_preventa(id_c)
                    if cancelado is None:
                        print(f"  No se encontro el registro #{id_c}.")
                    else:
                        print(f"  Registro de {cancelado['nombre']} eliminado de la fila de preventa.")
                except:
                    print("  Ingresa un numero valido.")

        elif opcion == "0":
            break

        else:
            print("  Opcion no valida.")


## Menu principal del sistema ##

def menu_principal():
    while True:
        print("\n" + "="*52)
        print("   CINETOBI — SISTEMA DE BOLETOS")
        print("="*52)
        print("  1. Comprar boleto")
        print("  2. Registrarme en preventa  (Avatar 3)")
        print("  3. Panel de administracion")
        print("  0. Salir")

        opcion = input("\n  Que deseas hacer? ").strip()

        if opcion == "1":
            flujo_compra()
        elif opcion == "2":
            flujo_preventa()
        elif opcion == "3":
            menu_admin()
        elif opcion == "0":
            print("\n  Gracias por usar CINETOBI. Hasta pronto!\n")
            break
        else:
            print("  Opcion no valida.")


if __name__ == "__main__":
    menu_principal()