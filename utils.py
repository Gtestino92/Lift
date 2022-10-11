def splitArrayByValue(array, value):
    arrayLowerEq = []
    arrayGreater = []
    for x in array:
        if(x > value): arrayGreater.append(x)
        else: arrayLowerEq.append(x)
    
    return arrayLowerEq, arrayGreater
