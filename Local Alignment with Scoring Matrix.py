from Bio import SeqIO
from Bio import pairwise2
from Bio.SubsMat import MatrixInfo as matlist
from Bio.pairwise2 import format_alignment
matrix = matlist.pam250

filepath = "C:/Users/ADMIN/Downloads/rosalind_loca (1).txt"
with open(filepath, "r") as hd:
    content = SeqIO.parse(hd, "fasta")
    seqs = []
    for rec in content:
        seqs.append(str(rec.seq))
    
    s = seqs[0]
    t = seqs[1]

    alignments = pairwise2.align.localds(seqs[0], seqs[1], matrix, -5, -5)
    print(int(alignments[1].score))
    # with open("C:/Users/ADMIN/Desktop/result.txt", "w") as whd:

    #     whd.write(str(int(alignments[1][2])))
    #     whd.write("\n")
    #     seq1 = ""
    #     seq2 = ""
    #     for i,j in zip(alignments[1][0], alignments[1][1]):
    #         print(i, j)
    #         if i != "-" and j != "-":
    #             seq1 += i
    #             seq2 += j
    #     whd.write(seq1)
    #     whd.write("\n")
    #     whd.write(seq2)
    # print(format_alignment(*alignments[1]))
    list_alignment = format_alignment(*alignments[1]).split("\n")
    seq1 = list_alignment[0].strip().split(" ")[1].replace("-","")
    seq2 = list_alignment[2].strip().split(" ")[1].replace("-","")

    

    print(seq1)
    print(seq2)
