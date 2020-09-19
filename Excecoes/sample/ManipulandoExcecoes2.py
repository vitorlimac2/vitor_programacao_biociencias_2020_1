def minhaFuncao():
    x = int("cinco")

try:
    minhaFuncao()
except ValueError as e:
    print("Ta comigo o erro:", e)


print("Segue o jogo...")