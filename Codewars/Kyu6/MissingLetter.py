import string
def find_missing_letter(chars):
    if chars[0].isupper(): 
        alphabet = string.ascii_uppercase
    else:
        alphabet = string.ascii_lowercase
    positie = alphabet.find(chars[0])

    for i in chars:
        if i == alphabet[positie]:
            positie += 1
        else:
            return alphabet[positie]