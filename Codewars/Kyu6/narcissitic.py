def narcissistic(value):
    power = str(value)
    power = len(power)
    sum = 0
    for i in str(value):
        sum += int(i) ** power
    if sum == value:
        return True
    return False