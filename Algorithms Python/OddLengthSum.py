def OddLengthSum(arr):
	all_sum = 0
	n = len(arr)
	for i in range(n):
		start = n-i
		end = i+1
		total = start * end
		odd = total//2
		if total % 2 != 0:
			odd +=1
		all_sum += odd * arr[i]
	return all_sum

arr = [ 1, 4, 2, 5, 3 ]
print(OddLengthSum(arr))

