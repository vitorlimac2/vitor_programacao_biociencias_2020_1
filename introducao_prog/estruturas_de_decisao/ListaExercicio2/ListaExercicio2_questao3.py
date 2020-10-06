###3 - Faça um algoritmo para ler duas variáveis inteiras A e B
### e garantir que A e B fiquem em ordem crescente, ou seja,
### a variável A deverá armazenar o menor valor fornecido e a variável B o maior

#### ler variavel A

a = int(input("Digite variavel A:"))

### ler variavel B

b = int(input("Digite variavel B:"))

#### variavel que recebe valor temporario
auxiliar = 0

if a > b:
    print("A antes = %d" % a)
    ## guardar primeiro valor de a
    auxiliar = a
    a = b
    print("A depois = %d" % a)
    ## atribuir valor antigo de a
    b = auxiliar
    print("B depois = %d" % b)

### imprime A e B
print("Variavel A %d" % a)
print("Variavel B %d" % b)
