def repeatedString(s, n):
    length_str = len(s)
    a_count = 0
    remainder_count = 0
    remainder = n % length_str
    value = n // length_str
    for val in s:
        if val == 'a':
            a_count +=1
    
    if remainder !=0:
        for i in range(remainder):
            if s[i] == 'a':
                remainder_count +=1
    return a_count*value+remainder_count