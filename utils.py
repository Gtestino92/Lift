def splitArrayByValue(array, value):
    arrayLower = []
    arrayGreaterEq = []
    for x in array:
        if(x < value): arrayLower.append(x)
        else: arrayGreaterEq.append(x)
    
    return arrayLower, arrayGreaterEq
