def Ham_dis(seq1, seq2):
    count = 0
    for i in range(len(seq1)):
        if seq1[i] != seq2[i]:
            count += 1
    return count
def distance_between_patttern(pattern, dna):
    length_pattern = len(pattern)
    Haming_distance = []
    min_nb = []
    for seq in dna:
        Haming_distance.append([])
        for i in range(len(seq)):
            sseq = seq[i: i+length_pattern]
            if len(sseq) == len(pattern):
                # print(sseq)
                distance = Ham_dis(pattern, sseq)
                # print(distance)
            Haming_distance[dna.index(seq)].append(distance)
    for hm in Haming_distance:
        min_nb.append(min(hm))
    return sum(min_nb)

filepath = "C:/Users/ADMIN/Downloads/rosalind_ba2h.txt"

with open(filepath, "r") as hd:
    pattern = hd.readline().strip()
    dna = hd.readline().strip().split(" ")
    # print(pattern)
    print(distance_between_patttern(pattern, dna))
    