from Bio import SeqIO
from Bio.Seq import Seq

with open("C:/Users/Admin/Downloads/rosalind_grph (2).txt","r") as hd:
    content = SeqIO.parse(hd, "fasta")
    
    seq = []
    prefix_3 = []
    suffix_3 = []
    
    for i,info in enumerate(content):
        seq.append(info.name)
        prefix_3.append(info.seq[:3])
        
        suffix_3.append(info.seq[len(info.seq)-3:len(info.seq)])
    print(prefix_3)
    print(suffix_3)

    result = []
    for i in range(len(suffix_3)):
        for j in range(len(prefix_3)):
            if suffix_3[i] == prefix_3[j] and seq[i] != seq[j]:
                result.append("%s %s"%(seq[i], seq[j]))
    
with open("C:/Users/Admin/Downloads/rosalind_grph_result.txt","w") as whd:
    for r in result:
        whd.write(r)
        whd.write("\n")