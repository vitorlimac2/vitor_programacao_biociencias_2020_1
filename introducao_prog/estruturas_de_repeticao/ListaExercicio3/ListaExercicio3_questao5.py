## Lista 3 - questão 5

## usuário digita vários números inteiros e positivos
## imprima o produto dos números ímpares e a soma dos números pares.

soma = 0
produto = 1

num = int(input("Digite número:"))

### loop infinito
while True:
    if num % 2 == 0:
        soma = soma + num
    else:
        produto = produto * num

    print(soma)
    print(produto)
    num = int(input("Digite número"))
