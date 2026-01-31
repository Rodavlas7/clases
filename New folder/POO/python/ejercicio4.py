def factorial(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

n = int(input("dime el valor n: "))
r = int(input("dime el valor r: "))

if r > n:
    print("error (r > n)")
elif r == 0 and n == 0:
    print("El numero de combinaciones es 1")
else:
    print(f"El numero de combinaciones es {int(factorial(n)/(factorial(r)*factorial(n-r)))}")