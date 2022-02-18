def redo_helper(number, awesome_phrases):
    INTERESTING = True
    arrofnumbers = [int(i) for i in str(number)]
    #digit followed by all zeros
    for i in arrofnumbers[1:]:
        if i == 0:
            INTERESTING = True
        else:
            INTERESTING = False
            break
    if(INTERESTING):
        return INTERESTING
    #every digit is the same number
    for i in arrofnumbers[1:]:
        if i == arrofnumbers[0]:
            INTERESTING = True
        else:
            INTERESTING = False
            break
    if(INTERESTING):
        return INTERESTING

    #digits sequential incrementing
    for i, value in enumerate(arrofnumbers[1:]):
        if(value == 0 and arrofnumbers[i] == 9):
            INTERESTING = True
        else:
            if value == arrofnumbers[i] + 1:
                INTERESTING = True
            else:
                INTERESTING = False
                break
    if(INTERESTING):
        return INTERESTING

    #digits sequential decrementing
    for i, value in enumerate(arrofnumbers[1:]):
        if(value == 0 and arrofnumbers[i] == 1):
            INTERESTING = True
        else:
            if value == arrofnumbers[i]-1:
                INTERESTING = True
            else:
                INTERESTING = False
                break
    if(INTERESTING):
        return INTERESTING

    #palindrome
    if arrofnumbers == arrofnumbers[::-1]:
        INTERESTING = True
        return INTERESTING

    #awesome_phrases
    if number in awesome_phrases:
        INTERESTING = True
    return INTERESTING


def is_interesting(number, awesome_phrases):
    #error checking
    if number < 98:
        return 0
    elif number >= 98 and number < 100:
        return 1
    INTERESTING = redo_helper(number, awesome_phrases)
    if(INTERESTING):
        return 2
    else:
        INTERESTING = redo_helper(number-1, awesome_phrases)
        if(INTERESTING):
            return 1
        else:
            INTERESTING = redo_helper(number-2, awesome_phrases)
        if(INTERESTING):
            return 1
        else:
            INTERESTING = redo_helper(number+1, awesome_phrases)
            if(INTERESTING):
                return 1
            else:
                INTERESTING = redo_helper(number+2, awesome_phrases)
            if(INTERESTING):
                return 1
    return 0
