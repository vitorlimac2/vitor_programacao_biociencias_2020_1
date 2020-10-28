# Lista 2 - questao 4
#  Escreva um programa em Python que recebe do usuário uma sequência de DNA que
# contém dois exons e um íntron; leia do usuário as coordenadas do primeiro exon (no formato start1;end1)
# e as coordenadas do segundo exon (start2;end2). Em seguida, imprima apenas a região exônica, isto é,
# as sub-sequências concatenadas do primeiro exon com o segundo exon.

seq = input("Digite sua sequência: ")

exon1 = input("Digite as coordenadas do primeiro exon: ")

start_exon1 = int(exon1.split(";")[0]) - 1
end_exon1 = int(exon1.split(";")[1])

exon2 = input("Digite as coordenadas do segundo exon: ")

start_exon2 = int(exon2.split(";")[0]) - 1
end_exon2 = int(exon2.split(";")[1])

seq_exonica = seq[start_exon1:end_exon1] + seq[start_exon2:end_exon2]

print("sequência de entrada: ", seq)
print("sequência do primeiro exon: ", seq[start_exon1:end_exon1])
print("sequência do segundo exon: ", seq[start_exon2:end_exon2])
print("Sequência exônica: ", seq_exonica)

