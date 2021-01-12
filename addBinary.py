def addBinaryNum(a,b):
    """
    Takes two binary numbers, sums them and retuens their sum

    """
    
    return bin((int(a,2)+int(b,2))).replace("0b","")
    
print(addBinaryNum("101","101"))
