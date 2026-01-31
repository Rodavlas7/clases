def potencia(base, exponente):
    resultado = 1

    if exponente > 0:
        for _ in range(exponente):
            resultado *= base
    elif exponente == 0:
        resultado = 1
    else:
        for _ in range(-exponente):  
            resultado *= base
        resultado = 1 / resultado

    return resultado


print(potencia(2, 5))
print(potencia(2, 0))
print(potencia(2, -3))
