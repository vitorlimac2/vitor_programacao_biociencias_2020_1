## Escreva um programa Python que peça ao usuário uma sequência de aminoácido e imprima o percentual de cada aminoácido.

aminoacidos = {}

seq = input("Digite sua sequência de aminoácidos")

seq_comprimento = len(seq)

for aa in seq:
    if aa in aminoacidos:
        aminoacidos[aa] = aminoacidos[aa] + 1
    else:
        aminoacidos[aa] = 1

for aa in aminoacidos:
    print(aa,aminoacidos[aa]*100/seq_comprimento)
