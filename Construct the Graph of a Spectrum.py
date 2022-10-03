filepath = "C:/Users/ADMIN/Downloads/rosalind_ba11a (1).txt"
from collections import defaultdict
with open(filepath, "r") as hd:
    content = [int(number) for number in hd.read().strip().split(" ")]
    mass_list = [0]
    for number in content:
        mass_list.append(number)
    # print(mass_list)
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
    # pos = tuple()
    for i in range(len(mass_list)-1):
        for j in range(i+1, len(mass_list)):
            mass = mass_list[j] - mass_list[i]
            for k in mass_table:
                if mass == int(mass_table[k]):
                    # pos.add((mass_list[i],mass_list[j]))
                    print("%d->%d:%s"%(mass_list[i], mass_list[j], k[0]))
