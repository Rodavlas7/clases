num = int(input("Deme el número de números que quiere ingresar: "))
par, impar, totpar, totimpar = 0, 0, 0, 0

for _ in range(num): 
    n = int(input("Ingrese un número: "))
    if n != 0:
        if n % 2 == 0:
            par += 1
            totpar += n
        else:
            impar += 1
            totimpar += n

print(f"Cantidad de números pares (sin contar 0): {par}")
print(f"Cantidad de números impares: {impar}")
print(f"Suma de los números pares: {totpar}")
print(f"Suma de los números impares: {totimpar}")
print(f"Media de los números pares: {totpar/par}")
print(f"Media de los números impares: {totimpar/impar}")
