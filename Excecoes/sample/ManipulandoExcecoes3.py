def minhaFuncao():
    try:
        x = int("cinco")
    except ValueError as e:
        print("Ta comigo o erro dentro da funcao:", e)

try:
    minhaFuncao()
except ValueError as e:
    print("Ta comigo o erro:", e)


print("Segue o jogo...")