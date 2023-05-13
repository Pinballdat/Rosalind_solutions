from Bio import SeqIO
from Bio import Seq
from collections import defaultdict
with open("C:/Users/Admin/Downloads/rosalind_corr.txt","r") as hd:
    content = SeqIO.parse(hd,"fasta")
    
    seq = []
    rc_seq = []
    
    for info in content:
        seq.append(str(info.seq))
        rc_seq.append(str(Seq.reverse_complement(info.seq)))
data = seq + rc_seq
dataset = defaultdict(int)
for s in data:
    dataset[s] += 1
# print(dataset)
    
correction = []
incorrection = []

for d in dataset:
    if dataset[d] == 1 and d in seq:
        incorrection.append(d)
    if dataset[d] > 1:
        correction.append(d)
# print(incorrection)
# print(correction)

def Haming_distance(seq1, seq2):
    count = 0
    for i in range(len(seq1)):
        if seq1[i] != seq2[i]:
            count += 1
    return count


with open("C:/Users/Admin/Downloads/rosalind_corr_result.txt","w") as whd:
    for incorrect in incorrection:
        for correct in correction:
            if Haming_distance(incorrect, correct) == 1:
                whd.write("%s->%s" % (incorrect, correct))
                whd.write("\n")