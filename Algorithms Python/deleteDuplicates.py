def deleteDuplicates(arr = [11,2,11, 12,3,13,5,5,7,11,11,11,12,13]):
  if len(arr) == 0:
    return 0
  index = 1
  for i in range(1,len(arr)):
    if arr[index -1] != arr[i]:
      if arr[i] not in arr[:index]:
        arr[index] = arr[i]
        index+=1
  return arr[:index]

print(deleteDuplicates())