from collections import defaultdict
filepath = "C:/Users/ADMIN/Downloads/rosalind_ba3d (7).txt"
with open(filepath, "r") as rec:
    content = rec.read().strip().split("\n")
    k = int(content[0])
    seq = content[1]

    # print(k)
    # print(seq)
    nodes_1 = []
    nodes_2 = []
    for i in range(len(seq)):
        sseq = seq[i:i+(k-1)]
        if len(sseq) == k-1:
            if sseq not in nodes_1:
                nodes_1.append(sseq)
            sorted_nodes_1 = sorted(nodes_1)
            nodes_2.append(sseq)

    tem = []
    for n in sorted_nodes_1:
        tem.append(set())
        for m in nodes_2:
            if n[1:] == m[:len(m)-1]:
                tem[sorted_nodes_1.index(n)].add(m)
    # print(tem)
    with open("C:/Users/ADMIN/Desktop/result.txt", "w") as whd:
        for i in range(len(sorted_nodes_1)):
            if tem[i] != set():
                list_tem = list(sorted(tem[i]))
                
                whd.write("{} -> ".format(sorted_nodes_1[i]))
                # print(sorted_nodes_1[i], "-> ", end='')
                for j in range(len(tem[i])):
                    whd.write(list_tem[j])
                    # print(list_tem[j], end="")
                    if(j != len(tem[i]) - 1):
                        whd.write(",")
                whd.write("\n")
                        # print(",", end='')
                
                # print()
