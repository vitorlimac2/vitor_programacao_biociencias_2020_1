## lista 4 questão 3

## Escreva um programa que leia uma relação de materiais de laboratório de biologia molecular digitada pelo usuário.
## O programa vai ler produto, preço e quantidade até que o usuário digite “-1” para parar.
## O programa armazenará em um dicionário onde o produto será a chave referente à uma lista contendo o preço e
## quantidade deste produto, ou seja, a chave será “produto” e o valor será uma lista [preço, quantidade].


estoque = {}

while True:


    ## ler nome do produto
    produto = input("Digite o nome do produto (-1 para cancelar): ")

    if produto == "-1":
        break
    ## ler preço

    preco = int(input("Digite o preco do produto %s (-1 para cancelar): " % produto))

    if preco == -1:
        break
    
    ## ler quantidade

    quantidade = int(input("Digite a quantidade (-1 para cancelar): "))

    if quantidade == -1:
        break

    estoque[produto] = [preco, quantidade]

total = 0

for i in estoque:
    print ("Produto %s\t Preço %d\t Quantidade %d" % (i, estoque[i][0], estoque[i][1]))
    total = total + estoque[i][0]*estoque[i][1]

print("Total de compra %.2f" % total)
    
