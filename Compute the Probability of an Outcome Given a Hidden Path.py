filepath = "C:/Users/ADMIN/Downloads/rosalind_ba10b.txt"
import pandas as pd
with open(filepath, "r") as hd:

	content = hd.read().strip().split("\n")
	seq_1 = content[0]
	seq_2 = content[4]

	# print(seq_1)
	# print(seq_2)
	
	alp_1 = content[2].split("\t")
	alp_2 = content[6].split("\t")
	# print(alp_1)
	# print(alp_2)
	# print(content[9])
	values = content[9].strip().split("\t")[1:] + content[10].strip().split("\t")[1:]
	# print(values)
	values_dict = {"Ax":float(values[0]), "Ay":float(values[1]), "Az":float(values[2]),"Bx":float(values[3]), "By":float(values[4]), "Bz":float(values[5])}
	# print(values_dict)
	prob =  1

	for i in range(len(seq_1)):
		sseq = seq_2[i] + seq_1[i]
		print(sseq)
		if len(sseq) == 2:
			prob *= values_dict[sseq]
		
	print(prob)
