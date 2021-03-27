def jumpingOnClouds(c):
    jumps = 0
    j = 0
    n = len(c)
    while j < len(c)-1:
        if j+2 < n and c[j+2] != 1:
            jumps += 1
            j +=2
        else:
            jumps += 1
            j+=1
    return jumps