# 1 - Escreva um código que contenha uma função que recebe como parâmetro uma string, o número mínimo e número máximo de caracteres.
# A função retorna verdadeiro se o comprimento da string está entre o intervalo mínimo e máximo de caracteres. Caso contrário, imprime falso.

def verificaString(string1, limiteInf, limiteSup):
    if limiteInf <= len(string1) <= limiteSup:
        return True
    return False

print(verificaString("Essa string retorna falso.", 5, 10))

print(verificaString("Essa string retorna verdadeiro.", 5, 100))
