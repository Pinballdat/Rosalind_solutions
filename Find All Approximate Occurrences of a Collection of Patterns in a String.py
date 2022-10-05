filepath = "C:/Users/ADMIN/Downloads/rosalind_ba9o.txt"

with open(filepath, "r") as rec:
    text = rec.readline().strip()
    # print(text)
    patterns = rec.readline().strip().split(" ")
    d = int(rec.readline().strip())
    # print(patterns)
    # print(d)

    res = []
    def distance(seq1, seq2):
        count = 0
        for i in range(len(seq1)):
            if seq1[i] != seq2[i]:
                count += 1
        return count

    def mismatch_count(patterns, text, d):
        res = []
        for pattern in patterns:
            for i in range(len(text)):
                sub_seq = text[i:i+len(pattern)]
                if len(sub_seq) == len(pattern) and distance(pattern, sub_seq) <= d:
                    res.append(i)
        return sorted(res)

    print(*mismatch_count(patterns, text, d))
