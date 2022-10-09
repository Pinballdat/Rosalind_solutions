import itertools
filepath = "C:/Users/ADMIN/Downloads/rosalind_lexv.txt"

with open(filepath, "r") as hd:
    alphabet = hd.readline().strip().split(" ")
    
    n = int(hd.readline().strip())
    #print(n)
    res_list = []
    for i in range(1, n+1):
        result = itertools.product(alphabet, repeat=i)
        for res in result:
            res_list.append("".join(res))
    # print(res_list)
    str_perm = sorted(res_list, key= lambda word: [alphabet.index(w) for w in word])

with open("C:/Users/ADMIN/Desktop/result.txt", "w") as rec:
    for pe in str_perm:
        rec.write("%s\n"%pe)
