filepath = "C:/Users/ADMIN/Downloads/rosalind_ba9e.txt"
from collections import defaultdict
with open(filepath, "r") as rec:
    text = rec.read().strip().split("\n")
    text_1 = text[0]
    text_2 = text[1]
    # print(text)
    seq = []
    for i in range(len(text_1)-1):
        for j in range(i+2,len(text_1)):
            seq.append(text_1[i:j])
            seq.append(text_2[i:j])
    # print(seq)
    res = defaultdict(int)

    for s in seq:
        res[s] += 1
    
    tem = {}
    for r in res:
        if res[r] > 1:
            tem[r] = len(r)
    
    for k in tem:
        if tem[k] == max(tem.values()):
            print(k)
