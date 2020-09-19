## descricao:
## entrada: arquivo FASTA contendo apenas uma sequência
## saída: identificador do gene e a sequência separados por tabulação

## abre arquivo
refArquivo = open("../data/TcCLB.506717.80_AA.fasta")

## inicializa variaveis gene_id e sequence
gene_id = ""
sequence = ""

## itera cada linha de arquivo.
for line in refArquivo:

    ## se encontra cabecalho
    if ">" in line:

        ## quebra a linha onde encontra o caractere ":" = line.split(':')
        ## seleciona o primeiro elemento do vetor retornado por line.split(':') = line.split(':')[0]
        ## para não selecionar o sinal de maior, pegamos o segundo elemento da cadeia de caracteres [1]
        gene_id = line.split(':')[0][1:]

    ## senao, esta lendo sequencia
    else:

        ##concatena os blocos de sequencia
        sequence += line.replace('\n', "")

## imprime gene_id e sequence
print("%s\t%s" % (gene_id, sequence))

## fecha arquivo
refArquivo.close()
