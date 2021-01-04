#Binary Search algorithm only works on sorted arrays.

def binarySearch(arr, value):
    """
    Returns the index position of the target element if found
    Returns -1 if target not in array
    """
    start = 0
    end = len(arr)-1

    while (end>=start):
        mid = (start + end) // 2
        if arr[mid] < value:
            start = mid +1
        elif arr[mid] > value:
            end = mid -1
        else:
            return mid
    return -1

arr = [1,2,3,4,5,6,7,8,9]
val = 10
index = binarySearch(arr,val)

print("Target element not found") if (index == -1) else print(f"The index of the target element is at position {index}")
