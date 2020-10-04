## Lista de exercícios 2 - questão 2

# ler dois números inteiros

num1 = int(input("Digite o primeiro número:"))
num2 = int(input("Digite o segundo número:"))

#informar se estes números são iguais ou diferentes, maior ou menor que o outro.

if num1 == num2:
    print("Os números são iguais!")
else:
    print("Os números são diferentes!")
    if num1 > num2:
        print("Primeiro número é maior que o segundo número!")
    elif num1 < num2:
        print("Primeiro número é menor que o segundo número!")

