# -*- coding: utf-8 -*-
"""
Created on Fri Jan  8 00:23:08 2021

@author: witty

Would be updated to cater for leetcodes test cases
"""



def longestSubStringLength(st):
    str_longest = ""
    max_so_far = 0
    if st == "":
        return 0
    
    for i in st:
        if i in str_longest:
            max_so_far = max(max_so_far, len(str_longest))
            str_longest = i
        else:
             str_longest += i
    # Caters for final case after loop exits, 
    #can also place this in the else block, though it'll require more run time
    max_so_far = max(max_so_far, len(str_longest))
    return max_so_far

print(longestSubStringLength("backlashed"))
