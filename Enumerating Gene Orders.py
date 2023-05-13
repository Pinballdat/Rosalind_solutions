from itertools import permutations

with open("C:/Users/Admin/Downloads/rosalind_perm.txt","r") as hd:
    number = int(hd.read().strip())
    
    array = []
    for i in range(1,number+1):
        array.append(i)
    res = permutations(array)
    new = []
    for r in res:
        new.append(r)
    # print(new)
with open("C:/Users/Admin/Downloads/rosalind_perm_result.txt","w") as whd:
    whd.write(str(len(new)))
    for r in new:
        my_list=" ".join(map(str, r))
        whd.write("\n")
        whd.write(my_list)