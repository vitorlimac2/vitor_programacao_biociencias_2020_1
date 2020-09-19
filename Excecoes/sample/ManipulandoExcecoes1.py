import sys

try:
    f = open('numeros.txt')
    s = f.readline()
    i = int(s.strip())
except IOError as e:
    errno, strerror = e.args
    print("I/O error({0}): {1}".format(errno,strerror))
    # e can be printed directly without using .args:
    # print(e)
except ValueError:
    print("Numero invalido.")
except:
    print("Erro inesperado:", sys.exc_info()[0])
    raise