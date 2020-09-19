refArquivoEntrada = open("/home/vitor/Downloads/TcCLB.506717.80_AA.fasta")
refArquivoSaida = open("/home/vitor/Downloads/TcCLB.506717.80_AA.out",'w')

cabecalho = refArquivoEntrada.readline()[1:-1]
sequencia = ""

refArquivoSaida.write("header\tseq\n")

for linha in refArquivoEntrada:
    sequencia += linha.replace('\n','')

refArquivoSaida.write ("%s\t%s"% (cabecalho,sequencia))
refArquivoEntrada.close()
refArquivoSaida.close()