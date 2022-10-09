from Bio import Seq
filepath = "C:/Users/ADMIN/Downloads/rosalind_dbru (1).txt"
with open(filepath, "r") as hd:
    seq_list = hd.read().split("\n")
    # print(seq_list)
    rc_seq_list = [Seq.reverse_complement(seq) for seq in seq_list]
    # print(rc_seq_list)

    k_mers = seq_list + rc_seq_list
    # print(k_mers)
    n = len(seq_list[0])
    k = n-1
    
    nodes = []
    
    for element in k_mers:
        # print(element)
        nodes.append([element[:k], element[1:k+1]])
        sorted_nodes = sorted(nodes)
    # print(sorted_nodes)
    tem = []
    for i in range(len(sorted_nodes)-1):
        # print(sorted_nodes[i])
        if sorted_nodes[i] == sorted_nodes[i+1]:
            tem.append(sorted_nodes[i])
    for t in tem:
        result = sorted_nodes.remove(t)
    # print(sorted_nodes)
with open("C:/Users/ADMIN/Desktop/result.txt","w") as whd:
    for ele in sorted_nodes:
        whd.write("(%s, %s)\n"%(ele[0], ele[1]))
