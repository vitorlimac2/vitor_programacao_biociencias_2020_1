def concatenaStringMaiuscula(*args):
    s = ""
    for a in args:
        s = s.join(a) ## join pega um elemento da iteracao do for, converte e concatena numa string.
    print s.upper()


L= ["Tudo ", "vai passar."]

concatenaStringMaiuscula("Tudo") 
concatenaStringMaiuscula(["Tudo"," "])
concatenaStringMaiuscula(["Tudo"," ", "vai"])
concatenaStringMaiuscula(["Tudo"," ", "vai", " "])
concatenaStringMaiuscula(["Tudo"," ", "vai", " ", "passar"])
concatenaStringMaiuscula(["Tudo"," ", "vai", " ", "passar","!"])

