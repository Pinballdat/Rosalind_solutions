from Bio.Seq import Seq

with open("C:/Users/Admin/Downloads/rosalind_rna.txt","r") as hd:
    content=Seq(hd.read().strip()).transcribe()

with open("C:/Users/ADmin/Downloads/rosalind_rna_result.txt", "w") as whd:
    whd.write(str(content))
    