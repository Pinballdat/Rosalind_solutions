from collections import defaultdict
filepath = "C:/Users/ADMIN/Downloads/rosalind_prsm (2).txt"
with open(filepath, "r") as hd:
    n = int(hd.readline().strip())
    content = hd.read().strip().split("\n")
    protein_strings = content[:n]
    multiset = content[n:]
    pre_suf = []

    mass_table = {
        "A":   71.03711,
        "C":   103.00919,
        "D":   115.02694,
        "E":   129.04259,
        "F":   147.06841,
        "G":   57.02146,
        "H":   137.05891,
        "I":   113.08406,
        "K":   128.09496,
        "L":   113.08406,
        "M":   131.04049,
        "N":   114.04293,
        "P":   97.05276,
        "Q":   128.05858,
        "R":   156.10111,
        "S":   87.03203,
        "T":   101.04768,
        "V":   99.06841,
        "W":   186.07931,
        "Y":   163.06333
    }
    tem = []
    for pro in protein_strings:
        pre_suf.append([])
        tem.append([])
        for i in range(0 , len(pro)):
            sum_pre = 0
            sum_suf = 0
            prefix = pro[:-i]
            suffix = pro[i:]
            tem[protein_strings.index(pro)].append((prefix, suffix))
            for p,k in zip(prefix, suffix):
                sum_pre += mass_table[p]
                sum_suf += mass_table[k]
            pre_suf[protein_strings.index(pro)].append(round(sum_pre,5))
            pre_suf[protein_strings.index(pro)].append(round(sum_suf,5))
    result = []
    for nb in multiset:
        number = float(nb)
        for spec in pre_suf:
            result.append([])
            for weight in spec:
                res = round(number - weight,5)
                result[pre_suf.index(spec)].append(res)
    
    max_value = []
    for r in result:
        if r != []:
            count = defaultdict(int)
            for number in r:
                count[number] += 1
            max_count= max(count.values())
            # print(count)
            max_value.append(max_count)
    print(max_value)
    for i, count in enumerate(max_value):
        if count == max(max_value):
            print(count)
            print(protein_strings[i])
    # print(tem)     
