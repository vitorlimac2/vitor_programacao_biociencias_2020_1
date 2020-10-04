# leia números inteiros do teclado
# condição de parada: O programa deve ler os números até que o usuário digite 0 (zero)
# No final da execução, exiba:
## a quantidade de números digitados
## soma
## média aritmética

## recebo numero
## somo numero
## gravo quantos numeros eu já li

soma = 0
n_lidos = 0

num = int(input("Digite o número:"))

while num!=0:
    soma = soma + num
    n_lidos = n_lidos + 1
    num = int(input("Digite o número:"))

print("Soma total = %d" % soma)

print("Números lidos = %d" % n_lidos)

media_aritmetica = soma/n_lidos

print("Média aritmética = %d" % media_aritmetica)






