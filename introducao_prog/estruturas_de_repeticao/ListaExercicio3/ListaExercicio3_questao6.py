## Lista 3 - questão 5

## leia a altura de 15 pessoas
## imprima maior altura
## imprima menor altura

alturas_lidas = 1
altura = float(input("Digite altura:"))

maiorAltura = altura
menorAltura = altura


## usando while

while alturas_lidas <= 14:
    altura = float(input("Digite altura:"))
    if altura > maiorAltura:
        maiorAltura = altura
    if altura < menorAltura:
        menorAltura = altura
    alturas_lidas = alturas_lidas + 1

## usando estrutura de repetição for e função range
## range(4) = [0,1, 2, 3]

for i in range(14): ## 14 porque eu já li o primeiro número
    altura = float(input("Digite altura:"))
    if altura > maiorAltura:
        maiorAltura = altura
    if altura < menorAltura:
        menorAltura = altura
    
