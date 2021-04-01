def arrayManipulation(n, queries):
    #Solution achieved using Prefix sum
    updates = [0]*(n+1)
    maximum = temp = 0
    for i in range(len(queries)):
        a,b,k = queries[i][0],queries[i][1],queries[i][2]
        updates[a-1] += k
        updates[b] -= k
    for j in range(len(updates)):
        temp += updates[j]
        maximum = max(temp,maximum)
    return maximum
