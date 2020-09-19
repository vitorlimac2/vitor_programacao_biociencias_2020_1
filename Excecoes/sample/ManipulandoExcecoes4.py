def minhaFuncao():
    try:
        x = int("cinco")
    except ValueError as e:
        print("Ta comigo o erro dentro da funcao:", e)
        raise

try:
    minhaFuncao()
except ValueError as e:
    print("Ta comigo o erro fora da funcao:", e)


print("Segue o jogo...")