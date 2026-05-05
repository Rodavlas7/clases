def fib(n, memo={}):
    if n in memo:
        return memo[n]
    if n == 0:
        memo[0] = 0
        print("fib(0) = 0")
        return 0
    elif n == 1:
        memo[1] = 1
        print("fib(1) = 1")
        return 1
    else:
        memo[n] = fib(n - 1, memo) + fib(n - 2, memo)
        print(f"fib({n}) = {memo[n]}")
        return memo[n]

def multiplicar(a, b):
    # CASO BASE:
    # Si el multiplicador es 0, el resultado de la multiplicación es 0
    if b == 0:
        return 0
    # CASO RECURSIVO:
    # Se suma 'a' una vez y se vuelve a llamar a la función
    # disminuyendo el multiplicador en 1
    return a + multiplicar(a, b - 1)

def potencia(base, exp):
    if exp < 0:
        return potencia(base, exp + 1) / base
    elif exp == 0:
        return 1
    else:
        return base * potencia(base, exp - 1)


# Función de Ackermann
def ackerman(m, n):
    # CASO BASE:
    # Cuando m es 0, la función deja de llamar recursivamente
    # y devuelve n + 1
    if m == 0:
        return n + 1
    # SEGUNDO CASO:
    # Si m es mayor que 0 y n es 0, se reduce m en 1
    # y se reinicia n con el valor 1
    if m > 0 and n == 0:
        return ackerman(m - 1, 1)
    # TERCER CASO (recursión anidada):
    # Primero se calcula ackerman(m, n - 1)
    # El resultado de esa llamada se usa como nuevo valor de n
    # en la llamada ackerman(m - 1, ...)
    return ackerman(m - 1, ackerman(m, n - 1))