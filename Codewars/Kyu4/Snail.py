def snail(snail_map):
    outputList = []

    while len(snail_map) > 0:
        #top row
        outputList += snail_map[0]
        del snail_map[0]

        #most right column from top to down
        if len(snail_map) > 0:
            for rij in snail_map:
                outputList += [rij[-1]]
                del rij[-1]
        
        #down row from right to left
        if len(snail_map) > 0:
            outputList += snail_map[-1][::-1]
            del snail_map[-1]

        #most left from down to up
        if len(snail_map) > 0:
            for i in reversed(snail_map):
                outputList += [i[0]]
                del i[0]    

    return outputList

array = [[1,2,3],
         [4,5,6],
         [7,8,9]]
print(snail(array))