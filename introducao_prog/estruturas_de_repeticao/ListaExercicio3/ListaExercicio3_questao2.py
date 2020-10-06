## Lista 3 - questao 2

## 2 - efetue a soma de todos os números ímpares
## que são múltiplos de três
## e que se encontram no conjunto dos números de 1 até 500.

soma = 0

numero = 3

while numero <= 500:
    if numero % 2 != 0 and numero % 3 == 0:
        soma = soma + numero
    numero = numero + 1

print(soma)

    
