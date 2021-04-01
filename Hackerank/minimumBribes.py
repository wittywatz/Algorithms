def minimumBribes(q):
    count = 0
    for i in reversed(range(len(q))):
        if q[i] != (i+1):
            if i-1>=0 and q[i-1] == i+1:
                q[i],q[i-1] =  q[i-1], q[i]
                count +=1
            elif i-2>=0 and q[i-2] == i+1:
                q[i-2],q[i-1],q[i] =  q[i-1], q[i], q[i-2]
                count +=2
            else:
                print('Too chaotic')
                return
    print(count)

    