class MaxStack():
    def __init__(self):
        self.stack = []
        self.maxx = []
    
    def push(self,element):
        """
        Adds element into stack and tracks the maximum element in the stack
        """
        self.stack.append(element)
        
        if self.maxx == []:
            self.maxx.append(element)
        else:
            #LessThan or equalTo caters for a repetition of maximum element.
            #This would ensure that the maximum element is always retrieved
            if self.maxx[-1] <= element:
                self.maxx.append(element)  
                
    def pop(self):
        """
        Returns the value of the popped element
        """
        if self.stack == [] and self.maxx == []:
            return None
        
        if self.stack[-1] == self.maxx[-1]:
            self.maxx.pop(-1)
        return self.stack.pop(-1)
    
    def top(self):
        """
        Returns the value at the top
        """
        if self.stack == []:
            return None
        return self.stack[-1]
    
    def max_stack(self):
        """
        Returns the maximum element in the stack
        """
        if self.maxx == []:
            return None
        return self.maxx[-1]

    
mystack = MaxStack()
mystack.push(3)
mystack.push(2)
mystack.push(1)
mystack.push(4)
mystack.push(1)
mystack.push(4)
print(f"The top element in the stack is {mystack.top()}")
print(f"The maximum element in the stack is {mystack.max_stack()}")
print(f"{mystack.pop()} has been removed from the stack")
print(f"The current maximum element in the stack is {mystack.max_stack()}")
print(f"{mystack.pop()} has been removed from the stack")
print(f"{mystack.pop()} has been removed from the stack")
print(f"The current maximum element in the stack is {mystack.max_stack()}")
print(f"{mystack.pop()} has been removed from the stack")
print(f"{mystack.pop()} has been removed from the stack")
print(f"{mystack.pop()} has been removed from the stack")
print(f"{mystack.pop()} has been removed from the stack")
