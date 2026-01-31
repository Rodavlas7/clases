def calcular_danio_por_turno(): #       Zero Division Error    Value Error
    try:
        danio_total = int(input("Daño total del Space Marine: "))
        turnos = int(input("Número de turnos: "))
        resultado = danio_total / turnos
        print(f"Daño promedio por turno: {resultado:.2f}")
    except ZeroDivisionError:
        print("Error: no puede haber 0 turnos, el combate debe tener al menos uno.")
    except ValueError:
        print("Error: ingresa solo números enteros.")

def calcular_poder_psiquico():#         Type Error      Value Error
    try:
        poder = int(input("Nivel psíquico del bibliotecario: "))
        multiplicador = input("Multiplicador del Warp: ")
        multiplicador = float(multiplicador)
        resultado = poder * multiplicador
        print(f"Poder total: {resultado}")
    except ValueError:
        print("Error: debes ingresar valores numéricos válidos.")
    except TypeError:
        print("Error: tipo de dato incorrecto.")
    except Exception as e:
        print(f"Error inesperado: {e}")

def mostrar_primarca(): #               Index Error     Value Error
    try:
        primarcas = ["Horus", "Sanguinius", "Magnus", "Roboute Guilliman"]
        indice = int(input("Elige un número de Primarca (0-3): "))
        print(f"Has elegido a {primarcas[indice]}")
    except IndexError:
        print("Error: ese número no corresponde a ningún Primarca.")
    except ValueError:
        print("Error: ingresa solo números enteros.")

def cargar_registro(): #                File Not Found Error
    try:
        nombre = input("Nombre del archivo: ")
        archivo = open(nombre, "r")
        contenido = archivo.read()
        print(contenido)
        archivo.close()
    except FileNotFoundError:
        print("Error: el archivo no existe o no se encontró en el sistema.")

def import_modulo_adeptus():#           Import Error
    try:
        import modulo # type: ignore
    except ImportError:
        print("Error: el módulo 'modulo_adeptus' no existe o no se pudo cargar.")



calcular_danio_por_turno()
calcular_poder_psiquico()
mostrar_primarca()
cargar_registro()
import_modulo_adeptus()
