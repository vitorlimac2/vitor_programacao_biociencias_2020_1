def imprimeString(string1, string2, operacao):
    print operacao(string1, string2)

def concatenaString(string1, string2):
    return (string1 + string2)

def tudoMaiuscula(string1, string2):
    return (string1.upper() + string2.upper())

def converteEmLista(string1, string2):
    L = string1 + string2
    return(list(L))

L= ["Tudo ", "vai passar."]

print("Apenas concatena:")
imprimeString(*L, operacao=concatenaString)

print("Concatena tudo em caixa alta:")
imprimeString(*L, operacao=tudoMaiuscula)

print("Converte string em lista")
imprimeString(*L, operacao=converteEmLista)
