### Escreva um programa que leia dois números e que
## pergunte qual operação deseja realizar.
## Você deve poder calcular a soma (+),
## subtração (-),
## multiplicação (*) e divisão (/).
## Exiba o resultado da operação solicitada

### ler o primeiro numero
numero1 = int(input("Digite o primeiro numero:"))
## ler o segundo numero
numero2 = int(input("Digite o segundo numero:"))

## qual operacao deseja realizar
print("Digite o número da operação que deseja realizar")
print("1 - soma")
print("2 - subtração")
print("3 - multiplicação")
print("4 - divisão")

operacao = int(input("Operação ="))

### resultado
# resultado = 0

## realizar operacao

if operacao == 1:
    ## soma
    resultado = numero1 + numero2
elif operacao == 2:
    ## subtracao
    resultado = numero1 - numero2
elif operacao == 3:
    ## multiplicacao
    resultado = numero1 * numero2
elif operacao == 4:
    ## divisao
    resultado = numero1/numero2
else:
    print("Operação inválida")

print(resultado)

