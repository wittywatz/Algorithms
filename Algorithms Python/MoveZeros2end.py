#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 20:22:40 2021

@author: watson
"""

def moveZeros(arr):
    """
    Maintains the order of non-zero elements and moves zeros to the end of array
    """
    array_length = len(arr)
    count = 0
    
    for value in arr:
        if (value != 0):
            arr[count]=value
            count+=1
    for i in range(count,array_length):
        arr[i] = 0
    
    return arr

print(moveZeros([0,5,0,8,0,3,1,0,4]))