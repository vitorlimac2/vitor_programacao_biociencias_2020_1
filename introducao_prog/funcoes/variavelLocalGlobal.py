a = 1
def alteraVariavel():
    a = 2
    print("Valor de a dentro da função é: %d" % a)
print("Variavel a antes de chamar função: %d" % a)
alteraVariavel()
print("Variavel a depois de chamar função: %d" % a)
