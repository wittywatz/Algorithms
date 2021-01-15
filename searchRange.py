"""
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

Follow up: Could you write an algorithm with O(log n) runtime complexity?
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

"""
class SolutionSearchRange():
        
    def binarySearch(self,arr, value):
        """
        Returns the index position of the target element if found
        Returns -1 if target is not in array
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

    def leftIndex(self,arr, value):
        """
        Returns the index(left) of the first occurence of the element
        """
        left = self.binarySearch(arr,value)
        if left == -1:
            return -1
        else:
            i = left
            while i>0 and arr[left] == arr[i-1]:
                i-=1
            return i    
    
    def rightIndex(self,arr, value):
        """
        Returns the index(right) of the last occurence of the element
        """
        right = self.binarySearch(arr,value)
        if right == -1:
            return -1
        else:
            i = right
            while i<len(arr)-1 and arr[right] == arr[i+1]:
                i+=1
            return i
    
    def searchRange(self, nums, target):
        """
        Returns the range of the start and end position when given a target
        """
        left = self.leftIndex(nums, target)
        right = self.rightIndex(nums,target)
        
        return [left, right]
        
nums = [5,7,7,8,8,10] 
target = 8
findRange = SolutionSearchRange()
result = findRange.searchRange(nums,target)
print(result)
print(f"The index of the given target starts at {result[0]} and ends at {result[1]}")
