## Lista 2 - questao 5

## ler três números positivos
## Escrever em ordem crescente

num1 = float(input("Digite primeiro número:"))
num2 = float(input("Digite segundo número:"))
num3 = float(input("Digite terceiro número:"))

#### existe as seguintes possibilidades:

## num1 > num2 > num3
if num1 > num2 and num2 > num3:
    print(num1, num2, num3)

## num1 > num3 > num2
if num1 > num3 and num3 > num2:
    print(num1, num3, num2)

## num2 > num1 > num3
if num2 > num1 and num1 > num3:
    print(num2, num1, num3)

## num2 > num3 > num1
if num2 > num3 and num3 > num1:
    print(num2, num3, num1)

## num3 > num1 > num2
if num3 > num1 and num1 > num2:
    print(num3, num1, num2)

## num3 > num2 > num1
if num3 > num2 and num2 > num1:
    print(num3, num2, num1)
