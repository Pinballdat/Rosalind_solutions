from Bio import SeqIO
from Bio.Seq import Seq

seq = {}
stop_pos = []
with open("C:/Users/Admin/Downloads/rosalind_orf (1).txt","r") as hd:
    content=SeqIO.read(hd,"fasta")
    protein_1= [Seq(content.seq[i:]).translate() for i in range(0,3)]
    protein_2= [Seq(content.seq).reverse_complement()[i:].translate() for i in range(0,3)]
    
    for p1 in protein_1:
        seq[p1] = []
        if "*" in p1:
            seq[p1].insert(0,0)
            for i in range(len(p1)):
                
                if p1[i] == "*":
                    seq[p1].append(i)
        
    for p2 in protein_2:
        seq[p2] = []
        if "*" in p2:
            seq[p2].insert(0,0)
            for i in range(len(p1)):
                
                if p2[i] == "*":
                    seq[p2].append(i)
    # print(seq)     
    new = set()
    for s in seq:
        for i in range(len(seq[s])-1):
            res_1 = s[(seq[s][i]):(seq[s][i+1])+1]
            # print(res_1)
            for pos in range(len(res_1)):
                    if res_1[pos] == "M":
                        new.add(res_1[pos:len(res_1)-1])
    
    with open("C:/Users/Admin/Downloads/rosalind_orf_result.txt","w") as whd:
        
        for n in new:
            whd.write(str(n))
            whd.write("\n")          
    # print(seq)
    # print(protein_1)
    # print(protein_2)
