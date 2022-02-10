def high(x):
    sum2 = 0
    for i in x.split():
        sum = 0
        for j in i:
            sum += (ord(j) - 96)
        if sum > sum2:
            sum2 = sum
            returnWoord = i         
    return returnWoord