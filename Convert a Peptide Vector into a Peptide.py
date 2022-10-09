filepath = "C:/Users/ADMIN/Downloads/rosalind_ba11d.txt"
from collections import defaultdict
with open(filepath, "r") as hd:
    vector = [int(nb) for nb in hd.read().strip().split(" ")]
    # print(vector)
    mass_table = {
        "A":   71.03711,
        "C":   103.00919,
        "D":   115.02694,
        "E":   129.04259,
        "F":   147.06841,
        "G":   57.02146,
        "H":   137.05891,
        ("I","L"):   113,
        ("K","Q"):   128,
        "M":   131.04049,
        "N":   114.04293,
        "P":   97.05276,
        "R":   156.10111,
        "S":   87.03203,
        "T":   101.04768,
        "V":   99.06841,
        "W":   186.07931,
        "Y":   163.06333,
    }
    mass = [0]
    for i in range(len(vector)):
        if vector[i] == 1:
            mass.append(i+1)
    seq = ""
    for j in range(len(mass)-1):
        res = mass[j+1] - mass[j]
        for k in mass_table:
            if res == int(mass_table[k]):
                seq += k[0]
    print(seq)
