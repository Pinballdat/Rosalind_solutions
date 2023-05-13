with open("C:/Users/Admin/Downloads/rosalind_subs (1).txt","r") as hd:
    content= hd.read().splitlines()
    postition = []
    # Count from 0 to length of seq
    # Position from 1 (count + 1)
    for i in range(len(content[0])+1):
        # print(content[0][i:i+len(content[1])])
        if content[1] == content[0][i:i+len(content[1])]:
            postition.append(str(i+1)) # Convert int to str and write into result_file
            
with open("C:/Users/Admin/Downloads/rosalind_subs_result.txt","w") as whd:
    whd.write(" ".join(postition))