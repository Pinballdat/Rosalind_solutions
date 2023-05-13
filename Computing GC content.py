from Bio.SeqUtils import gc_fraction
from Bio import SeqIO
GC_content = {}
gc_content = 0
with open("C:/Users/Admin/Downloads/rosalind_gc.txt", "r") as hd:
    content = SeqIO.parse(hd, "fasta")
    for record in content:
        GC_content[gc_fraction(record.seq)] = record.name
# print(GC_content)  
with open("C:/Users/Admin/Downloads/rosalind_gc_results.txt", "w") as whd:
    whd.write(GC_content[sorted(GC_content)[-1]])
    whd.write("\n")
    whd.write(str(round(sorted(GC_content)[-1] * 100,6)))
# print(GC_content[sorted(GC_content)[-1]])
# print(round(sorted(GC_content)[-1] * 100,6))
 