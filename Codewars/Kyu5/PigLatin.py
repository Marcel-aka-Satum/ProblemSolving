def pig_it(text):
    splitted = []
    for i in text.split():
        if i.isalpha():
            splitted.append(i[1:] + i[0] + "ay")
        else:
            splitted.append(i)
    return " ".join(splitted)