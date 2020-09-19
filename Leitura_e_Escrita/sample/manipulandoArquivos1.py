import os
mypath = '/home/vitor/Downloads/seqs'

print(os.listdir(mypath))

pathout = 'saida.fasta'

print(os.getcwd())

fout = open(pathout,"w")

for x in os.listdir(mypath):
    fh = open(os.path.join(mypath,x))
    data = fh.read()
    fh.close()
    fout.write(data)
fout.close()
