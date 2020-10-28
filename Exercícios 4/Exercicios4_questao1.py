# Exercícios 4 - questão 1

#1 - Faça um programa que leia um número indeterminado de valores e armazene numa lista,
# correspondentes a notas, encerrando a entrada de dados quando for informado um valor igual a -1 (que não deve ser armazenado). Após esta entrada de dados, faça:
# Uma função que mostre a quantidade de valores que foram lidos;
# Uma função que mostre todos os valores na ordem em que foram informados, um ao lado do outro;
# Uma função que mostre todos os valores na ordem inversa à que foram informados, um abaixo do outro;
# Uma função que calcule e mostre a soma dos valores;
# Uma função que calcule e mostre a média dos valores;
# Uma função que calcule e mostre a quantidade de valores acima da média calculada;


def quantNumLidos(lista):
    return len(lista)

def mostrarListaOrdem(lista):
    for i in lista:
        print(i, sep=" ")

def mostrarListaOrdemReversa(lista):
    for i in lista[::-1]:
        print(i)

def soma(lista):
    soma = 0
    for i in lista:
        soma += i
    return soma

def media(lista):
    total_soma = soma(lista)
    total_numeros = len(lista)
    return total_soma/total_numeros
    

def valoresAcimaMedia(lista):
    media_valores = media(lista)
    quant_acima_media = 0
    for i in lista:
        if i > media_valores:
            quant_acima_media += 1
    return quant_acima_media

lista = []


while True:

    num = int(input("Digite um número: "))

    if num == -1:
        break
    lista.append(num)



print("Quantidade de valores que foram lidos", quantNumLidos(lista))
print("Valores na ordem em que foram informados, um ao lado do outro:")
mostrarListaOrdem(lista)
print("Valores na ordem inversa à que foram informados, um abaixo do outro:")
mostrarListaOrdemReversa(lista)
print("Soma dos valores: ", soma(lista))
print("Média dos valores: ", media(lista))
print("Quantidade de valores acima da média:", valoresAcimaMedia(lista))
