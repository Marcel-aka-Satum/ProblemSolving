def create_phone_number(n):
    returnString = "("
    for index, value in enumerate(n):
        if(index == 3):
            returnString += ")"
            returnString += " "
        if(index == 6):
            returnString += "-"
        returnString += str(value)
    return returnString