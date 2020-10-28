# 3 - Escreva um programa Python que peça ao usuário duas sequências de DNA e
# imprima o complemento reverso de sua concatenação

def complemento(seq):
    complemento = "";
    for base in seq:
        if base == "A":
            complemento = complemento + "T"
        if base == "C":
            complemento = complemento + "G"
        if base == "G":
            complemento = complemento + "C"
        if base == "T":
            complemento = complemento + "A"

    return complemento

def reverso(seq):
    reverso = ""

    n = len(seq) - 1

    while n >=   0:
        reverso = reverso + seq[n]
        n -= 1
    
    return reverso

seq1 = input("Digite a primeira sequência: ")

seq2 = input("Digite segunda sequência: ")

concat_seq = seq1 + seq2

print("Sequência concatenada: ", concat_seq)

comp_seq = complemento(concat_seq)

print("Complemento: ", comp_seq)

print("Complemento reverso: ", reverso(comp_seq))


