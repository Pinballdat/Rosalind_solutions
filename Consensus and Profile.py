from Bio.Seq import Seq
from Bio import SeqIO


seq_db = []
with open("C:/Users/Admin/Downloads/rosalind_cons (2).txt","r") as hd:
    seq_list = SeqIO.parse(hd, "fasta")
    for seq in seq_list:
        seq_db.append(seq.seq)
        
# Create a profile
profile = {"A":[0]*len(seq_db[0]), "C":[0]*len(seq_db[0]), "G":[0]*len(seq_db[0]), "T":[0]*len(seq_db[0])}
# print(profile)

for i in range(len(seq_db[0])):
    for j in seq_db:
        profile[j[i]][i] += 1



# Create consensus string
max_keys = []
for i in range(len(seq_db[0])):
    consensus_str= {"A":0, "C":0, "G":0, "T":0}
    for j in seq_db:
        consensus_str[j[i]] += 1
    max_keys.append(max(consensus_str, key=consensus_str.get))
# print("".join(max_keys))

with open("C:/Users/Admin/Downloads/rosalind_cons_result.txt","w") as whd:
    whd.write("".join(max_keys))
    for x in profile:
        whd.write("\n")
        whd.write("{0}: {1}".format(x, " ".join(map(str, profile[x]))))
        
    