def deleteDuplicates(arr = [2,3,5,5,7,11,11,11,12,13]):
  if len(arr) == 0:
    return 0
  index = 1
  print(len(arr))
  for i in range(1,len(arr)):
    if arr[index -1] != arr[i]:
      arr[index] = arr[i]
      index+=1
  return arr[:index]

print(deleteDuplicates())