from figuras import Rectangulo
r = Rectangulo(2, 3.2)
print(f"Altura: {r.getAlto()}")
print(f"Anchura: {r.getAncho()}")
print(f"Área: {r.area()}")
print(f"Perímetro: {r.perimetro()}")

print("\n\n")

r2 = Rectangulo(2, 25)
print(f"Altura: {r2.getAlto()}")
print(f"Anchura: {r2.getAncho()}")
print(f"Área: {r2.area()}")
print(f"Perímetro: {r2.perimetro()}")