cont = 0

s = int(input("Número inicio: "))
n = int(input("Número fin   : "))

for i in range(s, n + 1):
    if i % 3 == 0:
        cont += 1
        print(i)

print(cont)
