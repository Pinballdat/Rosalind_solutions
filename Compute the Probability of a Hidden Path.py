filepath = "C:/Users/ADMIN/Downloads/rosalind_ba10a.txt"
import pandas as pd
with open(filepath, "r") as hd:

	content = hd.read().strip().split("\n")
	seq = content[0]
	alp = content[2].split("\t")
	# print(alp)

	values = content[5].strip().split("\t")[1:] + content[6].strip().split("\t")[1:]
	# print(values)
	values_dict = {"AA":float(values[0]), "AB":float(values[1]), "BA":float(values[2]), "BB":float(values[3])}

	prob = 1 / len(alp)

	for i in range(len(seq)):
		sseq = seq[i:i+len(alp)]
		if len(sseq) == len(alp):
			prob *= values_dict[sseq]
		
	print(prob)
