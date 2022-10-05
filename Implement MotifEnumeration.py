filepath = "C:/Users/ADMIN/Downloads/rosalind_ba2a (1).txt"
from collections import defaultdict
from itertools import product
with open(filepath, "r") as hd:
    k,d = map(int, hd.readline().strip().split(" "))
    seq = hd.read().strip().split("\n")
    
    pattern = ["".join(p) for p in product("ACGT", repeat=k)]
    def distance(seq1, seq2):
        count = 0
        for i in range(len(seq1)):
            if seq1[i] != seq2[i]:
                count += 1
        return count
    sub_seq = []
    for s in seq:
        sub_seq.append([])
        for i in range(len(s)-k+1):
            sseq = s[i:i+k]
            if sseq not in sub_seq[seq.index(s)]:
                sub_seq[seq.index(s)].append(sseq)
    # print(sub_seq)
    res = []
    for p in pattern:
        for array in sub_seq:
            res.append([])
            for sseq in array:
                if distance(p, sseq) <= d:
                    res[sub_seq.index(array)].append(p)
    new_res = []
    for r in res:
        if r != []:
          set_seq = set(r)
          for ss in set_seq:
            new_res.append(ss)
    count = defaultdict(int)
    result = []
    for n in new_res:
        count[n] += 1
        if count[n] == len(seq):
            result.append(n)
    print(*sorted(result))
