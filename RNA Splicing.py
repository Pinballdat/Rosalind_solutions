from Bio import SeqIO
from Bio.Seq import Seq

with open("C:/Users/Admin/Downloads/rosalind_splc (5).txt","r") as hd:
    content = SeqIO.parse(hd, "fasta")
    dna = []
    for seq in content:
        dna.append(str(seq.seq))
    
    dna_string = dna[0]
    introns = dna[1:]
    pos = [0]
   
    for intron in introns:
        for i in range(len(dna_string)):
            substr = dna_string[i:i+len(intron)]
            if intron == substr:
                pos.append(i)
                pos.append(i+len(intron))
    pos.append(len(dna_string))
    sorted_pos = sorted(pos)
    # print(sorted_pos)

    exons = ""
    for j in range(len(sorted_pos)):
        if j % 2 == 0:
            exons += dna_string[sorted_pos[j]:sorted_pos[j+1]]
    # print(len(exons))
    
    protein = Seq(exons).translate(to_stop= True)
    # print(protein)
    
    # protein_pos = [0]
    # for i in range(len(protein)):
    #     if protein[i] == "*":
    #         protein_pos.append(i)
    # protein_pos.append(len(protein))

    # result = []
    # for k in range(len(protein_pos)-1) :
    #     cds = protein[protein_pos[k]:protein_pos[k+1]].strip("*")
    #     for aa in range(len(cds)):
    #         if cds[aa] == "M":
    #             result.append(cds[aa:])
    
    with open("C:/Users/Admin/Downloads/rosalind_splc_result.txt","w") as whd:
        whd.write(str(protein))

    