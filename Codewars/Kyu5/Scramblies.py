
def check_freqs(s):
    chars = {}
    for i in s:
        if i not in chars:
            chars[i] = 1
        else:
            chars[i] += 1
    return chars 

def scramble(s1, s2):
    dict_s1 = check_freqs(s1)
    dict_s2 = check_freqs(s2)

    for i in s2:
        if i in s1 and dict_s2[i] <= dict_s1[i]:
            continue
        else:
            return False
    return True