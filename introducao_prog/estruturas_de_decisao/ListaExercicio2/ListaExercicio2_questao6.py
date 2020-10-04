## ler um numero

## testar se está entre
## 15 e 187

num = int(input("Digite o número:"))

if num > 15 and num < 187:
    print("Sim! Está entre 15 e 187!")


### testar se está entre dois números quaisquer
limiteInferior = int(input("Digite o limite inferior:"))
limiteSuperior = int(input("Digite o limite superior:"))

if num > limiteInferior and num < limiteSuperior:
    print("Sim! Está entre %d e %d!" % (limiteInferior,limiteSuperior))