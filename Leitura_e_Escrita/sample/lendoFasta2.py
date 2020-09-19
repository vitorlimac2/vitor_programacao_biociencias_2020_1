refArquivo = open("/home/vitor/Downloads/TcCLB.506717.80_AA.fasta")

primeiraLinha = refArquivo.readline()
cabecalho = primeiraLinha[1:-1]
sequencia = ""
while True:
    linha = refArquivo.readline()
    if linha == "":
        break
    sequencia += linha.replace('\n','')
print ("Cabecalho: %s"%cabecalho)
print ("Sequencia: %s"%sequencia)
refArquivo.close()