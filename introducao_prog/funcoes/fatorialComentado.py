import sys

def fatorial(n):
    if n > 1:
        return n*fatorial(n-1)
    else:
        return 1

numero = int(sys.argv[1])

print(fatorial(numero))
