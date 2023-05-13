with open("C:/Users/Admin/Downloads/rosalind_hamm.txt","r") as hd:
    content=hd.read().splitlines()
    count = 0
    for i in range(len(content[0])):
        if content[0][i] != content[1][i]:
            count += 1
with open("C:/Users/Admin/Downloads/rosalind_hamm_result.txt","w") as whd:
    whd.write(str(count))