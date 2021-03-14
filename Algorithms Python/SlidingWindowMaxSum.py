# -*- coding: utf-8 -*-


def maxSum(array,k):
    """
    Given an array of integers, and K elements to sum
    
    Returns the maximum possible sum of a sub-array of K elements in the array
    """
    array_length = len(array)
    
    if k == 0:
        return -1
    
    if array_length < k:
        return -1
    
    window = sum(array[:k])
    maximum = window
    
    for i in range(array_length-k):
        window = window - array[i] + array[i+k]
        maximum = max(window, maximum)
    return maximum

arr = [0,1,3,5,2,7,8,2,9,0,4,1]
# Maximum should be 8+7 with K as 2
result = maxSum(arr,2)

print("Try valid inputs") if (result==-1) else print(f"The maximum possiblesum is {result} for the given sub-array")