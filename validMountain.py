def validMountainArray(arr):
        
        if (len(arr)<3):
            return False
        
        index = 0
        arrlen = len(arr)
        
        while ((index+1)<=(arrlen-1) and arr[index]<arr[index+1]):
            index +=1
        
        if(index == arrlen-1 or index==0):
            return False
        
        while((index+1)<=(arrlen-1) and arr[index]>arr[index+1]):
            index +=1
            
        if(index < arrlen-1):
            return False
        else:
            return True
