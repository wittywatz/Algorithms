def isDuplicate(nums):
        """
        Returns true if duplicate in array
        """
        duplicate = {}
        for i in nums:
            if i in duplicate.keys():
                return True
            else:
                duplicate[i] = i
        return False
        
        
def isDuplicate2(nums):
        """
        Returns true if duplicate in array
        """
       return len(nums) != len(set(nums))
