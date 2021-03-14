"""
Given a non-empty array of integers nums, 
every element appears twice except for one. Find that single one.

Follow up: Could you implement a solution with
a linear runtime complexity and without using extra memory?
"""

def singleNumber(arr):
    for value in arr:
        if arr.count(value) == 1:
            return value
        else: #The else block can be ignored
            while value in arr:
                arr.remove(value)
print(singleNumber([4,1,2,1,2]))
