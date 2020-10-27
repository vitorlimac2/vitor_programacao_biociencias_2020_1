# Escreva um programa em Python que recebe uma sequência de DNA do usuário e calcula o conteúdo GC da sequência.


seq = input("Digite a sequência:")

total_c = 0
total_g = 0

for base in seq:
    if base.upper() == "C":
        total_c += 1
    elif base.upper() == "G":
        total_g += 1

print("Conteudo GC = %.2f" % ((total_c + total_g)*100/len(seq)))
