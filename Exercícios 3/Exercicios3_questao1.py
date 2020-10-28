## Lista 3 - questao 1
# 1 - Escreva um código em Python que leia um número não determinado de valores (podendo ser positivos e negativos) e
# calcule e escreva a média aritmética dos valores lidos,
# a quantidade de valores positivos,
# a quantidade de valores negativos
# e o percentual de valores negativos e positivos.

total_positivos = 0
total_negativos = 0
total_num_lidos = 0

total_soma = 0

while True:
    num = int(input("Digite um número: "))

    total_num_lidos += 1

    if num > -1:
        total_positivos += 1
    else:
        total_negativos += 1

    total_soma += num

    opcao = input("Deseja continuar? [S/n] ")

    if opcao.upper() == "N":
        break

media = total_soma/total_num_lidos

print("Média aritmética = ", media)
print("Números positivos = ", total_positivos)
print("Números negativos = ", total_negativos)
print("Percentual dos valores positivos = %.02f" % (total_positivos*100/total_num_lidos))
print("Percentual dos valores negativos = %.02f" % (total_negativos*100/total_num_lidos))
