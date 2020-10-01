### exemplo para ler dois números inteiros da linha de comando
## e imprimir a soma

import sys

print("Argumentos passados para o interpretador pela linha de comando:")

num_args = len(sys.argv)
print("Total de argumentos: %d" % num_args)

for i in range(num_args):
    print("Argumento %d com índice %d = %s" % (i+1,i,sys.argv[i]))

if num_args < 3:
    print("Você precisa digitar dois números como argumentos. Finalizando script.")
    sys.exit()

## ler o primeiro numero da linha de comando
num1 = int(sys.argv[1])
## ler o segundo numero da linha de comando
num2 = int(sys.argv[2])

print("Soma = %d" % (num1+num2))