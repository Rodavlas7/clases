class Carrito:

    def __init__(self, codigo, tipo):
        self.codigo = codigo
        self.tipo = tipo    # normales, portabebes, pequeños

    def __str__(self):
        return f"Código: {self.codigo} | Tipo: {self.tipo}"