with open("C:/Users/Admin/Desktop/Python_code/Monoisotopic_mass_table.txt","r") as tb:
    content = tb.read().strip().split("\n")
    # print(content)
    mass_table = {}
    for c in content:
        mass_table[c.split("   ")[0]] = float(c.split("   ")[1])
    # print(mass_table)
    
with open("C:/Users/Admin/Downloads/rosalind_prtm (4).txt","r") as hd:
    protein=hd.read().strip()
    # print(protein)
    mass = 0
    for aa in protein:
        if aa in mass_table:
            mass += mass_table[aa]
    
with open("C:/Users/Admin/Downloads/rosalind_prtm_result.txt","w") as whd:
    whd.write(str(mass))