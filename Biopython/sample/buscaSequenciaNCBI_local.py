from Bio.Blast.Applications import *

### endereço completo para os arquivos

sequencia = "/home/vitor/PycharmProjects/VitorCoelho/Biopython/data/TcCLB.506717.80_AA.fasta"
sequenciasAlvo = "/home/vitor/PycharmProjects/VitorCoelho/Biopython/data/TriTrypDB-47_TcruziCLBrenerEsmeraldo-like_AnnotatedProteins.fasta"
meuOutput = "/home/vitor/PycharmProjects/VitorCoelho/Biopython/data/out.blastp.outfmt6.txt"

## criando a linha de comando para o blastp (proteína vs proteína)

## NcbiblastpCommandline - proteina vs proteina
## NcbiblastnCommandline - nucleotideo vs nucleotideo
## NcbiblastxCommandline - nucleotideo -> traduz para proteina vs proteina

linha_de_comando_blastp = NcbiblastpCommandline(query=sequencia, subject=sequenciasAlvo, outfmt=6, out=meuOutput, evalue=0.05)

print("A linha de comando para o blastp é:\n%s" % linha_de_comando_blastp)

#
print("Executando busca local:")

stdout, stderr = linha_de_comando_blastp()

print("Fim da busca local...")

# Abrindo resultado
blast_result = open(meuOutput, "r")

linhas = blast_result.read()
print(linhas)