def transformSentence(sentence):
    wrds = sentence.split()
    res = []
    for i in wrds:
        new = i[0]
        for j in range(1, len(i)):
            bef = i[j-1].lower()
            aft = i[j]
            if bef < aft.lower():
                new += aft.upper()
            elif bef > aft.lower():
                new += aft.lower()
            else:
                new += aft
        res.append(new)
    return " ".join(res)
