# 2 - Faça um algoritmo para ler o nome, as três notas e o número de faltas de um aluno e
# escrever qual a sua situação final: Aprovado, Reprovado por Falta ou Reprovado por Média.
# A média para aprovação é 7,0 e o limite de faltas é 25% do total de aulas.
# O número de aulas ministradas no semestre foi de 80. Caso seja reprovado por falta e por média, prevalece a reprovação por falta.



AULAS_MINISTRADAS = 80
NUM_MAX_FALTAS = 80*0.25
MEDIA_APROVACAO = 7


nome = input("Digite o nome: ")
nota1 = float("Digite a nota 1: ")
nota2 = float("Digite a nota 2: ")
nota3 = float("Digite a nota 3: ")
num_faltas = int(input("Digite o número de faltas: "))

media = (nota1 + nota2 + nota3)/3

if num_faltas > NUM_MAX_FALTAS:
    print("Reprovado por falta.")
elif media < MEDIA_APROVACAO:
    print("Reprovado por média.")
else:
    print("Aprovado.")
