def countingValleys(steps, path):
    # Write your code here
    if steps < 2 or steps > pow(10,6):
        return 
    val = 0
    valley = 0
    for i in range(steps):
        if path[i] == 'U':
            val +=1
            if val == 0:
                valley +=1
        else:
            val -=1
    return valley