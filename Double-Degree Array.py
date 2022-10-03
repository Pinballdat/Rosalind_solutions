filepath = "C:/Users/ADMIN/Downloads/rosalind_ddeg (2).txt"
from collections import defaultdict


with open(filepath, "r") as hd:
    m, n = map(int, hd.readline().strip().split(" "))
    # print(m)
    # print(n)
    array = hd.read().strip().split("\n")
    nodes = []
    for i in array:
        edge = i.split(" ")
        for j in edge:
            nodes.append(int(j))
    res = defaultdict(int)
    for number in range(1,m+1):
        count = 0
        if number not in nodes:
            res[number] = 0
        else:
            for node in nodes:
                if number == node:
                    count += 1
                    res[number] = count
    # print(res)
    edges = []
    for i in array:
        edges.append(i.split(" "))
    # print(edges)
    
    for number in range(1,m+1):
        sum_nb = 0
        sum = []
        new = []
        for ed in edges:
            if str(number) in ed:
                new.append(ed)
        # print(new)
        for n in new:
            for nb in n:
                if nb != str(number):
                    sum_nb += res[int(nb)]
        print(sum_nb, end= " ")
        

        
        
