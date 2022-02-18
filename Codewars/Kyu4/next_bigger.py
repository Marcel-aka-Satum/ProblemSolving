def next_bigger(n):
    strlistofpar = list(str(n))

    for i in range(len(strlistofpar) - 2, -1, -1):
        if strlistofpar[i] < strlistofpar[i + 1]:
            iAfter = strlistofpar[i:]
            nextMin = min(filter(lambda x : x > iAfter[0], iAfter)) #extract all elements higher than strlistofpar[i] and choose the min of them because it's gonna be the next biggest number
            iAfter.remove(nextMin) # remove the nextMin from this array because it's gonna go before it  
            iAfter.sort() 
            strlistofpar[i:] = [nextMin] + iAfter 
            return int("".join(strlistofpar))
    return -1




print(next_bigger(48721))