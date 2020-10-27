# 1 - Escreva um código que procure numa lista L= [10, 15, 88, 79, 44, 55, 36, 47, 889, 147] dois valores digitados pelo usuário.
# Quando achar o valor informe ao usuário a posição na lista. Caso um número não seja encontrado, informe ao usuário.
# Considere o fato que um dos números pode estar contido na lista e o outro não.
# a ) Escreva um código que use while para iterar os elementos da lista e realizar a busca;
# b) Escreva um código que use a função range para para iterar os elementos da lista e realizar a busca;
# c) Escreva um código que use a função enumerate para iterar os elementos da lista e realizar a busca;

# lendo os numeros
num1 = int(input("Digite o primeiro número:"))
num2 = int(input("Digite o segundo número:"))

# a lista
L= [10, 15, 88, 79, 44, 55, 36, 47, 889, 147]

## "flags" para indicar se achamos ou não cada número
achou1 = False
achou2 = False

## a)

## contador
n = 0

while n < len(L):
    if L[n] == num1:
        print("O primeiro número %d está na posição %d" % (num1, n))
        achou1 = True

    if L[n] == num2:
        print("O segundo número %d está na posição %d" % (num2, n))
        achou2 = True

    n += 1

if not achou1:
    print("O primeiro número %d não foi encontado." % num1)

if not achou2:
    print("O segundo número %d não foi encontado." % num2)
