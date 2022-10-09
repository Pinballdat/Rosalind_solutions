from Bio import SeqIO
from Bio import Seq
filepath = "C:/Users/ADMIN/Downloads/rosalind_corr (6).txt"
with open(filepath, "r") as hd:
    content = SeqIO.parse(hd, "fasta")
    seq_list = []
    for rec in content:
        seq_list.append(str(rec.seq))
    # print(seq_list)

    right = []

    for i,s in enumerate(seq_list):
        seq = s
        rev_seq = Seq.reverse_complement(s)
        for k in range(i+1, len(seq_list)):
            if s == seq_list[k] or rev_seq == seq_list[k]:
                if s not in right and rev_seq not in right:
                    right.append(s)
                    right.append(rev_seq)
    # print(right)
    
    wrong = []
    for i in seq_list:
        if i not in right:
            wrong.append(i)

    def Haming_distance(seq1, seq2):
        count = 0
        for s1, s2 in zip(seq1, seq2):
            if s1 != s2:
                count += 1
        return count

    with open("C:/Users/ADMIN/Desktop/result.txt" , "w") as whd: 
        for w in wrong:
            for r in right:
                if Haming_distance(w, r) == 1:
                    whd.write("%s->%s\n"%(w,r))
              
