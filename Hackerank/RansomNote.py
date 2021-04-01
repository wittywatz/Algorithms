def checkMagazine(magazine, note):
    mag = {}
    notE = {}
    for j in magazine:
        mag[j] = mag.get(j,0)+1
    for k in note:
        notE[k] = notE.get(k,0)+1
    for i in note:
        if i not in magazine:
            print('No')
            return
        if mag[i] < notE[i]:
            print('No')
            return   
    print('Yes')