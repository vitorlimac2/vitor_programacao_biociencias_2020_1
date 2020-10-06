### Lista 3 - questao 1
## Escreva um código em Python que leia um número N
# e imprima todos os números inteiros de N a 1 (em ordem decrescente).


numero = int(input("Digite um número:"))

while numero >= 1:
    print(numero)
    numero = numero - 1
