def twoStrings(s1, s2):
    s1_length = len(s1)
    s2_length = len(s2)
    if s2_length > s1_length:
        for i in s1:
            if i in s2:
                return 'YES'
                
    else:
        for j in s1:
            if j in s2:
                return 'YES'
    return 'NO'           