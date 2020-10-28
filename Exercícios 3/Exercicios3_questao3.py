## Exercícios 3 - questao 3

# Elabore um algoritmo que leia o peso e a altura de um adulto e mostre sua condição de acordo com a tabela abaixo.
##  IMC = peso/(altura*altura)

# IMC em adultos	Condição
# Abaixo de 18,5	Abaixo do peso
# Entre 18,5 e 25	Peso normal
# Entre 25 e 30		Acima do peso
# Acima de 30		obeso

massa = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura em metros: "))

imc = massa/(altura * altura)

if imc < 18.5:
    print("Condição Abaixo do Peso.")
elif imc < 25:
    print("Condição Peso Normal.")
elif imc < 30:
    print("Condição Acima do Peso.")
else:
    print("Condição Obeso.")
