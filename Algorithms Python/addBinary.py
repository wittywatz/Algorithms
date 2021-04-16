# def addBinaryNum(a,b):
#     """
#     Takes two binary numbers, sums them and returns their sum

#     """
#     return bin((int(a,2)+int(b,2))).replace("0b","")
    
# # print(addBinaryNum("101","101"))
# res = 30/4
# print(30//4)

def triplets(t,d):
    d.sort()
    count = 0
    for i in reversed(range(len(d))):
        if i == 1:
            break
        # print('check', d[i])
        sum_to_search = t - d[i]
        # print('sum',sum_to_search)
        p1 = 0
        p2 = 1
        p2_max = i-1
        p1_max = i-2
        while(p1 <= p1_max):
            if(p2 == p2_max+1):
                p1+=1
                p2 = p1 + 1
                continue
            if(d[p1]+d[p2] <=sum_to_search):
                count +=1
            p2+=1
    # print('Print', count)
    return count

print(triplets(8,[1,2,3,4,6]))