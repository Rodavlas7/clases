class Lavadora:
    def __init__(self, nombre, color, marca, precio, ciclos):
        self.nombre = nombre
        self.color = color
        self.marca = marca
        self.precio = precio
        self.ciclos = ciclos
        self.encendida = False

    def info(self):
        estado = "encendida" if self.encendida else "apagada"
        print(f"Lavadora: {self.nombre} | Marca: {self.marca} | Color: {self.color} | Precio: {self.precio} | Ciclos: {self.ciclos} | Estado: {estado}")

    def encender(self):
        if not self.encendida:
            self.encendida = True
            print(f"{self.nombre} ahora está encendida")
        else:
            print(f"{self.nombre} ya estaba encendida")

    def apagar(self):
        if self.encendida:
            self.encendida = False
            print(f"{self.nombre} ahora está apagada")
        else:
            print(f"{self.nombre} ya estaba apagada")

def main():
    lav1 = Lavadora("Lavadora Ultra", "Blanco", "Samsung", 8500, 12)

    lav1.info()
    lav1.apagar()
    lav1.info()
    lav1.encender()
    lav1.info()


if __name__ == "__main__":
    main()
