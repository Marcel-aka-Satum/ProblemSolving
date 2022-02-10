def alphabet_position(text):
    n = []
    text = text.lower()
    for i in text:
        if i.isalpha():
            n.append(str(ord(i) - 96))
    return " ".join(n)