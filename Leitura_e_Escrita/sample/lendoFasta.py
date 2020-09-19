refArquivo = open("/home/vitor/Downloads/TcCLB.506717.80_AA.fasta")
arquivoFasta = refArquivo.read() #myfile is a string
cabecalho = arquivoFasta.split('\n')[0][1:]
sequencia = ''.join(arquivoFasta.split('\n')[1:])
print("Identificador: %s"%cabecalho)
print("Sequencia: %s"%sequencia)
refArquivo.close()
