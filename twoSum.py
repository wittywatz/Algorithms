# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 20:22:40 2021
@author: watson
"""

def twoSum(arr,target):
    """
    Takes an array of integers and a target variable
    
    Returns a list of indexes which sum up to the target or [] if otherwise
    """
    store = {}
    for index,value in enumerate(arr):
        difference = target-value
        if difference in store.keys():
            return [store[difference], index]
        else:
            store[value] = index
    return []

nums = [2,7,11,15]
target = 9
result = twoSum(nums,target)
print(result)
