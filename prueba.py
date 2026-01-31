import tkinter as tk
import os

def crear_boleto(nombre, origen, destino, fecha, asiento):
    # Crear ventana y canvas
    root = tk.Tk()
    root.title("Boleto de Autobús")
    canvas = tk.Canvas(root, width=800, height=400, bg="white")
    canvas.pack()

    # Borde del boleto
    canvas.create_rectangle(20, 20, 780, 380, outline="black", width=3)

    # Título
    canvas.create_text(400, 50, text="BOLETO DE AUTOBÚS", font=("Arial", 36), fill="black")

    # Línea divisoria
    canvas.create_line(20, 100, 780, 100, fill="black", width=2)

    # Datos del pasajero
    canvas.create_text(100, 150, text=f"Nombre: {nombre}", font=("Arial", 20), anchor="w")
    canvas.create_text(100, 190, text=f"Origen: {origen}", font=("Arial", 20), anchor="w")
    canvas.create_text(100, 230, text=f"Destino: {destino}", font=("Arial", 20), anchor="w")
    canvas.create_text(100, 270, text=f"Fecha: {fecha}", font=("Arial", 20), anchor="w")
    canvas.create_text(100, 310, text=f"Asiento: {asiento}", font=("Arial", 20), anchor="w")

    # Función para guardar como PDF usando Ghostscript
    def guardar_pdf():
        # Guardar primero como PostScript
        ps_file = "boleto.ps"
        pdf_file = "boleto.pdf"
        canvas.postscript(file=ps_file)
        # Convertir PS a PDF con Ghostscript
        comando = f'gswin64c -dBATCH -dNOPAUSE -sDEVICE=pdfwrite -sOutputFile={pdf_file} {ps_file}'
        os.system(comando)
        print(f"Boleto guardado como {pdf_file}")

    boton_guardar = tk.Button(root, text="Guardar Boleto como PDF", command=guardar_pdf)
    boton_guardar.pack(pady=10)

    root.mainloop()


def pedir_datos():
    nombre = input("Ingrese su nombre: ")
    origen = input("Ciudad de origen: ")
    destino = input("Ciudad de destino: ")
    fecha = input("Fecha (YYYY-MM-DD): ")
    asiento = input("Número de asiento: ")
    return nombre, origen, destino, fecha, asiento


def main():
    nombre, origen, destino, fecha, asiento = pedir_datos()
    crear_boleto(nombre, origen, destino, fecha, asiento)


if __name__ == "__main__":
    main()
