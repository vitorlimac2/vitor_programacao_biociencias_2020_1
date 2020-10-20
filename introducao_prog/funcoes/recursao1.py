# -*- coding: utf-8 -*-

## O módulo sys contém várias funcionalidades que permitem
## a interação do interpretador de Python com o sistema operacional.

## O atributo argv é uma lista de argumentos passados para o interpretador
## na linha de comando.
from sys import argv

def soma_recursiva(n):
  if(n > 0):
    resultado = n + soma_recursiva(n - 1)
  else:
    resultado = 0
  print("Resultado = %d\tValor de n = %d" % (resultado, n))
  return resultado

## argv[0] é o nome do script "recursao1.py"
## argv[1] será o número passado pelo usuário.
numero = int(argv[1])

soma_recursiva(numero)

