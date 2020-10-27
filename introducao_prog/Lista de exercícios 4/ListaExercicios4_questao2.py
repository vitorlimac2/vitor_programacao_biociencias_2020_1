## lista 4 questão 2

# leia uma frase digitada pelo usuário e conte a quantidade de cada caractere.
# Cada chave será letra e o valor será a quantidade de vezes que a letra se repete na frase.
# Dica: primeiramente converta a string lida para letras maiúsculas antes de contar usando a função upper.

frase = input("Digite sua frase: ")

dicio = {}

for letra in frase:
    if letra in dicio:
        dicio[letra] = dicio[letra] + 1
    else:
        dicio[letra] = 1

print(dicio)

    
