def countTriplets(arr, r):
    # Array has to be sorted
    array = sorted(arr)
    result = 0
    firstMultiple = {}
    secondMultiple = {}
    for i in array:
        if i in secondMultiple:
            result += secondMultiple[i]
        if i in firstMultiple:
            val2 = i*r
            secondMultiple[val2]= secondMultiple.get(val2,0)+firstMultiple[i]
        val = i*r
        firstMultiple[val] = firstMultiple.get(val,0)+1
    return result