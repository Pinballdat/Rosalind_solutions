filepath = "C:/Users/ADMIN/Downloads/rosalind_ba1i.txt"
import itertools
from collections import defaultdict
with open(filepath, "r") as rec:
    text = rec.readline().strip()
    # print(text)
    k,d = map(int,rec.readline().strip().split(" "))
    # print(k)
    # print(d)

    perm = ["".join(element) for element in itertools.product("ACGT", repeat=k)]
    # print(perm) 

    def distance(seq1, seq2): # Haming distance for 2 seq
        count = 0
        for i in range(len(seq1)):
            if seq1[i] != seq2[i]:
                count += 1
        return count
    

    temp_1 = []
    for p in perm: # each k_mer in permutation
        for i in range(len(text)-k):
            if distance(p, text[i:i+k]) <= d:
                temp_1.append(p)
    # print(temp_1)

    def pattern_to_num(text,pattern): # return the postition of sseq if sseq == pattern 
        for i in range(len(text)):
            sub_seq = text[i:i+len(pattern)]
            if sub_seq == pattern and len(sub_seq) == len(pattern):
                return i
    
    index = [] # list of position
    count = [] # list of count 
    for i in range(len(temp_1)):
        pattern = temp_1[i] # each k_mers in temp_1 if distance(k_mers in text, k_mers in perm) <= d
        index.append(pattern_to_num(text, pattern)) # position of subseq in text if k_mers in text == pattern
        count.append(1)

    # print(index)
    # print(count)

    temp_2 = []
    for i in index:
        if i != None:
            temp_2.append(i)
    # print(temp_2)
    sorted_temp = sorted(temp_2)
    # print(sorted_temp)
    for i in range(len(sorted_temp)-1):
        if sorted_temp[i] == sorted_temp[i+1]:
            count[i+1] = count[i] + 1
    # print(count)
    max_count = max(count)
    # print(max_count)

    def num_to_patt(text,index,k):
        for i in range(len(text)-k):
            sseq = text[i:i+k]
            if(i==index):
                return sseq

    result = set()
    for i in range(len(temp_1)-1):
        if count[i] == max_count:
            pattern = num_to_patt(text, sorted_temp[i], k)
            result.add(pattern)
    print(*result)
