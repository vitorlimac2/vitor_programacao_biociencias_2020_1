### ler numero de identificao

identificador = int(input("Digite o numero de identificação: "))

## ler as 3 notas

nota1 = float(input("Digite a primeira nota: "))

nota2 = float(input("Digite a segunda nota: "))

nota3 = float(input("Digite a terceira nota: "))

## ler a media dos exercicios

me = float(input("Digite a média dos exercicios: "))

## calcular a media de aproveitamento

media_ap = (nota1 + nota2 * 2 + nota3 * 3 + me)/7

## verificar qual o conceito

print("Identificador = $d" % identificador)

if media_ap >= 90:
    print("A - aprovado")
elif media_ap >= 75:
    print("B - aprovado")
elif media_ap >= 60:
    print("C - aprovado")
elif media_ap >= 40:
    print("D - reprovado")
else:
    print("E - reprovado")
