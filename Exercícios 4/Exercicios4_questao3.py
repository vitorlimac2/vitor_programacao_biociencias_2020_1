## Exercícios 4 - questao 3
## Escreva um código que leia uma frase digitada pelo usuário.
## uma função lambda que identifique quando um caractere é uma vogal
## uma função lambda que identifique quando um caractere é uma consoante
## uma função lambda identifique quando um caractere é um número

## Ao final, imprima a quantidade de consoantes, vogais, números e outros caracteres



vogal = lambda caractere: caractere.upper() in "AEIOU"
consoante = lambda caractere: caractere.upper() in "BCDFGHJKLMNPQRSTUXWZ"
numero = lambda caractere: caractere in "1234567890"

frase = input("Digite uma frase: ")

total_vogal = 0
total_consoante = 0
total_numero = 0
total_outros = 0

for caractere in frase:
    if vogal(caractere):
        total_vogal += 1
    elif consoante(caractere):
        total_consoante += 1
    elif numero(caractere):
        total_numero += 1
    else:
        total_outros += 1

print("Total de consoantes = %d" % total_consoante)
print("Total de vogais = %d" % total_vogal)
print("Total de números = %d" % total_numero)
print("Total de outros = %d" % total_outros)
