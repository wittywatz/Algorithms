def minimumSwaps(arr):
    count = 0
    temp = [0]*len(arr)
    for i,v in enumerate(arr):
        # Get the sorted indices
        temp[v-1] = i
    for i,v in enumerate(arr):
        if v != i+1:
            t = temp[i]
            # Update the array in place
            arr[i], arr[t] = arr[t],arr[i]
            # Update the index of the temp array
            temp[i],temp[arr[t]-1] = i,t
            count+=1
    return count