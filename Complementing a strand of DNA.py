from Bio.Seq import Seq

with open("C:/Users/Admin/Downloads/rosalind_revc.txt","r") as hd:
    content=Seq(hd.read().strip()).reverse_complement()

with open("C:/Users/ADmin/Downloads/rosalind_revc_result.txt", "w") as whd:
    whd.write(str(content))
    