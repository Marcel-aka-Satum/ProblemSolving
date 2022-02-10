def order(sentence):
    l = []
    index = 1
    for i in sentence.split():
        l.append(index)
        index += 1

    for i in sentence.split():
        for j in i:
            if j.isnumeric():
                l[int(j) -1] = i
    return " ".join(l)