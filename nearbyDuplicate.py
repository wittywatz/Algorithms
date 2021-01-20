def nearDuplicate(nums,k):
    for i in range(len(nums)):
        for j in range(1,k+1):
            if i+j < len(nums)  and nums[i] == nums[i+j]:
                return True
    return False
    
def NearbyDuplicate(nums=nums,k=3):
        if len(nums) <= k:
            return len(nums) != len(set(nums))
        for i in range(len(nums)-k):
            if len(nums[i:i+k+1]) != len(set(nums[i:i+k+1])):
                return True
        return False
        
        
def nearbyDuplicateElement(nums,k):
    container = {}
    for i, num in enumerate(nums):
        if (num in container.keys()) and ((i-container[num])<=k):
            return True
        else:
            container[num]=i
    return False
    
    
    
