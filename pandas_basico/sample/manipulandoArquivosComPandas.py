import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#### ATENÇÃO: Instale o pacote xlrd >= 1.0.0 para ler arquivos Excel
# ## Use pip
# ou
## conda install -c anaconda xlrd
#
## ou diretamente pelo PyCharm

## lendo arquivo excel
with pd.ExcelFile('../data/quantificacao_exemplo.xlsx') as xlsx:
    df = pd.read_excel(xlsx, 'Counts')

print(df)

######################################
### normalizando os niveis de expressão por
### CPM = numero de counts * 10**6/total numero de counts




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