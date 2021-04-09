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



#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'partitionArray' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY numbers
#

def helper(arr1, arr2):
    dd = {}
    for val in arr1:
        dd[val] = True
    for val2 in arr2:
        if val2 in dd:
            return False
    return True

def partitionArray(k, numbers):
    # Write your code here
    print(k)
    print(numbers)
    count = 0
    
    # number_set = list(set(numbers))
    # print(number_set)
    # len_numbers = len(number_set)
    # possible = len_numbers//k
    # print(possible)
    
    
    for i in range(0,len(numbers),k):
        temp = numbers[i:i+k]
        print('temp',temp)
        if len(temp) == len(set(temp)):
            count +=1
    print(count)
    return 'Yes' if count>=k else 'No'
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    k = int(input().strip())

    numbers_count = int(input().strip())

    numbers = []

    for _ in range(numbers_count):
        numbers_item = int(input().strip())
        numbers.append(numbers_item)

    result = partitionArray(k, numbers)

    fptr.write(result + '\n')

    fptr.close()
