import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



## um dataframe pode ser um dict de series
d = {'coluna1': pd.Series([1., 2., 3.], index=['a', 'b', 'c']),
     'coluna2': pd.Series([1., 2., 3., 4.], index=['a', 'b', 'c', 'd']),
     'coluna3': pd.Series([10., 2., 8.], index=['b', 'c', 'd'])}

## criando dataframe
df = pd.DataFrame(d)
print(df)

print("Imprimindo coluna 2:")
print(df['coluna2'])

## lendo arquivo excel

## lendo arquivo csv

## escrevendo arquivo excel

## escrevendo arrquivo csv

## atributos do dataframe


## adicionando colunas no dataframe

## renomeando colunas do dataframe

## estatisticas basicas

## ordenanacao

## usando operacoes logicas e relacionais para extrair linhas de um dataframe

## outras operacoes com dataframes

## plotando dados