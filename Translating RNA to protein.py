from Bio.Seq import Seq

with open("C:/Users/Admin/Downloads/rosalind_prot (2).txt","r") as hd:
    content=Seq(hd.read()).translate(to_stop=True)
    
with open("C:/Users/Admin/Downloads/rosalind_prot_result.txt","w") as whd:
    whd.write(str(content))
    