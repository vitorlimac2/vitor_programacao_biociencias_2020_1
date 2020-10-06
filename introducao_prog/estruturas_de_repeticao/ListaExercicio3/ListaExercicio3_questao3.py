## contar a quantidade de números pares entre dois números quaisquer.

numero1 = int(input("Digite o limite inferior:"))
numero2 = int(input("Digite o limite superior:"))

pares = 0

while numero1 <= numero2:
    if numero1 % 2 == 0: # é par
        pares = pares + 1
    numero1 = numero1 + 1
print(pares)
