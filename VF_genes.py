from Bio import SeqIO
import pandas as pd

vf_files = SeqIO.parse("C:/Users/Admin/Desktop/VF_AD_genes.txt", "fasta")
name = []
description = {}
gene = {}
protein = {}
protein_id = {}
locus_tag = {}
location = {}
gbkey = {}
for seq_record in vf_files:
    name.append(seq_record.name)
    rep_1 = seq_record.description.replace("["," ")
    rep_2 = rep_1.replace("]","").split("  ")
    description[rep_2[0]] = rep_2[1:]

for des in description:
    for info in description[des]:
        if info.find("gene=") != -1:
            gene[des] = info.split("=")[1]
        if info.find("protein=") != -1:
            protein[des] = info.split("=")[1]
        if info.find("protein_id=") != -1:
            protein_id[des] = info.split("=")[1]
        if info.find("locus_tag=") != -1:
            locus_tag[des] = info.split("=")[1]
        if info.find("location") != -1:
            location[des] = info.split("=")[1]
        if info.find("gbkey") != -1:
            gbkey[des] = info.split("=")[1]
            
            

d = {"gene":pd.Series(data=gene, index=list(gene.keys())),"protein":pd.Series(data=protein, index=list(protein.keys())), "protein_id":pd.Series(data=protein_id, index=list(protein_id.keys())), "locus_tag":pd.Series(data=locus_tag, index=list(locus_tag.keys())), "location":pd.Series(data=location, index=list(location.keys())), "gbkey":pd.Series(data=gbkey, index=list(gbkey.keys()))}

df = pd.DataFrame(data=d, index=name)
df.to_excel("C:/Users/Admin/Desktop/VF_AD_genes.xlsx", sheet_name="VF_AD")