from Bio import SeqIO
transitions = 0
transversions = 0
seq = []

with open("C:/Users/Admin/Downloads/rosalind_tran (4).txt","r") as hd:
    content = SeqIO.parse(hd, "fasta")
    
    for s in content:
        seq.append(s.seq)
    
for i in range(len(seq[0])):
    if seq[0][i] != seq[1][i]:
        tem = seq[0][i] + seq[1][i]
        # print(tem)
        if tem in ["AG","GA","CT","TC"]:
            transitions += 1
        else:
            transversions += 1

with open("C:/Users/Admin/Downloads/rosalind_tran_results.txt","w") as whd:
    whd.write(str(transitions/transversions))