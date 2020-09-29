## questao 1
import pandas as pd
data = pd.read_excel("../data/WHO POP TB some.xls")
print(data)

## questao 2
tbMortesColuna = data['TB deaths']
print(tbMortesColuna.sum())

## questao 3
print(tbMortesColuna.max())
print(tbMortesColuna.min())

## questao 4
print(tbMortesColuna.mean())
print(tbMortesColuna.median())

## questao 5

print(data.sort_values('TB deaths'))

## questao 6
populacaoColuna = data['Population (1000s)']
data['TB deaths (per 100,000)'] = tbMortesColuna * 100 / populacaoColuna
print(data)

## questao 7
## BRICS = Brazil, Russia, India, China, South Africa

brazil_populacao = data[(data['Country'] == "Brazil")]["Population (1000s)"]


### ou

brics_data = data[(data['Country'] == "Brazil") |
                  (data['Country'] == "Russia") |
                  (data['Country'] == "India")  |
                  (data['Country'] == "China")  |
                  (data['Country'] == "South Africa")]
print(brics_data)

total = brics_data['TB deaths'].sum()
print(total)

media = brics_data['TB deaths'].mean()
print(media)


