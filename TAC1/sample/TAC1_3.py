## descricao: usando a biblioteca csv
## entrada: arquivo .csv
## saída: busca em arquivo .csv por valor

## importa a biblioteca csv
import csv

## usando with para abrir o arquivo de entrada species.csv e criar o arquivo de saida birds.csv
with open("../data/species.csv") as refArquivoCsvEntrada, open("../data/birds.csv", 'w') as refArquivoCsvSaida:

    ## inicializa o manipulador do arquivo de entrada
    leitorArquivoCsvEntrada = csv.reader(refArquivoCsvEntrada)

    ## inicializa o manipulador do arquivo de saida
    escritorArquivoCsvSaida = csv.writer(refArquivoCsvSaida)

    ## itera as linhas do arquivo de entrada
    for linha in leitorArquivoCsvEntrada:

        ## faz o teste para linhas referentes a birds
        if linha[3].upper().rstrip()=="BIRD":
            ## escreve linha no formato CSV no arquivo birds.csv
            escritorArquivoCsvSaida.writerow(linha)

            ## como eu realmente queria
            print(' '.join(linha))