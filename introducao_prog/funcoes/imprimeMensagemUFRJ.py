def imprimeSoma(arg1, arg2=0, adicionaMaisDois=False):
    if adicionaMaisDois:
        arg2 += 2
    print(arg1+arg2)

imprimeSoma(10)

imprimeSoma(10, 5)

imprimeSoma(10, 5, False)

imprimeSoma(10,5,True)


