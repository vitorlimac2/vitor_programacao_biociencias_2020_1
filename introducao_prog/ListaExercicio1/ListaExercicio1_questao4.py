#### ler valor em nanogramas

valor_nanograma = float(input("Digite o valor em nanograma:"))

## converte para microgramas -- dividir valor por 1000

valor_micrograma = valor_nanograma/1000

## imprime valor convertido

print("Valor em nanograma = %.5f" % valor_nanograma)
print("Valor em micrograma = %.5f" % valor_micrograma)
