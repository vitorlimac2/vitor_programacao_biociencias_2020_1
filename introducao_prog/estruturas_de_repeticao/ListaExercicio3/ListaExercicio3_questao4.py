## Lista 3 - questao 4

## Leia números inteiros do teclado.
## O programa deve ler os números até que o usuário digite 0 (zero).
## No final da execução, exiba a quantidade de números digitados,
## assim como a soma e a média aritmética

soma = 0

numero = int(input("Digite um número:"))

numeros_lidos = 0

while numero != 0:
    soma = soma + numero
    numeros_lidos = numeros_lidos + 1
    numero = int(input("Digite um número:"))

print(soma)

media_aritmetica = soma/numeros_lidos
print(media_aritmetica)

