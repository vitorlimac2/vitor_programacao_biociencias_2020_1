## 2 - Escreva um código que contenha uma função denominada calculaAreaRetangulo.
## Caso seja passado somente um valor como argumento, significa que o retângulo
## possui todos lados iguais e a área é dada pelo quadrado do valor passado como argumento.
## Caso seja passado dois valores como argumentos, a área é dada pela multiplicação dos dois argumentos.
## Ou seja, a função terá um argumento opcional.

def calculaAreaRetangulo(lado1, lado2=0):
    if lado2 == 0:
        return lado1*lado1
    return lado1*lado2


print(calculaAreaRetangulo(10))
print(calculaAreaRetangulo(2,4))
