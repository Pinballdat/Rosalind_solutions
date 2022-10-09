filepath = "C:/Users/ADMIN/Downloads/rosalind_ba9d.txt"
from collections import defaultdict
with open(filepath, "r") as rec:
    text = rec.read().strip()
    # print(text)
    seq = []
    for i in range(len(text)-1):
        for j in range(i+2,len(text)):
            seq.append(text[i:j])
    res = defaultdict(int)

    for k in seq:
        res[k] += 1
    tem = {}
    for key in res:
        if res[key] > 1:
            tem[key] = len(key)
    
    max_length = max(tem.values())
    for t in tem:
        if tem[t] == max_length:
            print(t)
