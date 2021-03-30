def rotLeft(a, d):
    """
    With the given constraints, d shouldn't be greater than n or less than 1
    """
    # Without this condition, the function should work just fine
    if  len(a) == d:
        return a
    arr1 = a[:d]
    arr2 = a[d:]
    newArray = arr2 + arr1
    return newArray