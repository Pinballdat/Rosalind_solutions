# Use requests modules to access UniProt database
from Bio import SeqIO
import requests as r

seq = {}
# motif = N{P}[ST]{P} 
with open("C:/Users/Admin/Downloads/rosalind_mprt (2).txt","r") as hd:
    content = hd.read().strip().splitlines()
    
    baseurl = "http://www.uniprot.org/uniprot/"
    
    for id in content:
        crurl = baseurl+id.split("_")[0]+".fasta"
        response = r.post(crurl)
        seq[id] = "".join(response.text.strip().split("\n")[1:])
# print(seq)
result = {}
for s in seq:
    result[s] = []
    for i in range(len(seq[s])-4):
        if seq[s][i] == "N" and seq[s][i+1] and seq[s][i+3] != "P" and seq[s][i+2] in ["T","S"]:
            result[s].append(str(i+1))

with open("C:/Users/Admin/Downloads/rosalind_mprt_result.txt","w") as whd:
   
    for r in result:
        if result[r] != []:
            whd.write(r)
            whd.write("\n")
            whd.write(" ".join(result[r]))
            whd.write("\n")
    
    