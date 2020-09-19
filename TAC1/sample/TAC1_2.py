## descricao:
## entrada: arquivo multi-FASTA
## saída: imprime cabeçalho e a sequência

## abre arquivo
refArquivo = open("../data/TriTrypDB-47_TcruziCLBrenerEsmeraldo-like_AnnotatedProteins.fasta")

## inicializa variaveis gene_id e sequence
gene_id = ""
sequence = ""

## itera cada linha de arquivo.
for line in refArquivo:

    ## se encontra cabecalho
    if ">" in line:

        ## se sequence nao esta vazia e o programa achou um cabecalho, significa
        ## que nas iteracoes anteriores ele ja leu um cabecalho+sequencia,
        ## logo precisa imprimir ambos e reinicializar as variaveis
        if sequence != "":
            print("%s\n%s" % (gene_id, sequence))

            ## reinicializa sequencia
            sequence = ""

        ## para não selecionar o sinal de maior, pegamos o segundo elemento da cadeia de caracteres [1]
        gene_id = line.rstrip()[1:]

    ## senao, esta lendo sequencia
    else:

        ##concatena os blocos de sequencia
        sequence += line.replace('\n', "")

## imprime gene_id e sequence
print("%s\n%s" % (gene_id, sequence))

## fecha arquivo
refArquivo.close()