class MinStack():
    def __init__(self):
        self.stack = []
        self.min = []
    
    def push(self,element):
        """
        Adds element into stack and tracks the mimimum element in the stack
        """
        self.stack.append(element)
        
        if self.min == []:
            self.min.append(element)
        else:
            #GreaterThan or equalTo caters for a repetition of minimum element.
            #This would ensure that the minimum element is always retrieved
            # Eg [3,2,1,4,1]
            if self.min[-1] >= element:
                self.min.append(element)  
                
    def pop(self):
        """
        Returns the value of the popped element
        """
        if self.stack == [] and self.min == []:
            return None

        if self.stack[-1] == self.min[-1]:
            self.min.pop(-1)
        return self.stack.pop(-1)
    
    def top(self):
        """
        Returns the value at the top
        """
        if self.stack == []:
            return None
        return self.stack[-1]
    
    def min_stack(self):
        """
        Returns the minimum element in the stack
        """
        if self.min == []:
            return None
        return self.min[-1]

mystack = MinStack()
mystack.push(3)
mystack.push(2)
mystack.push(1)
mystack.push(4)
mystack.push(1)
mystack.push(4)
print(f"The top element in the stack is {mystack.top()}")
print(f"The minimum element in the stack is {mystack.min_stack()}")
print(f"{mystack.pop()} has been removed from the stack")
print(f"The current minimum element in the stack is {mystack.min_stack()}")
print(f"{mystack.pop()} has been removed from the stack")
print(f"{mystack.pop()} has been removed from the stack")
print(f"{mystack.pop()} has been removed from the stack")
print(f"The current minimum element in the stack is {mystack.min_stack()}")
print(f"{mystack.pop()} has been removed from the stack")
print(f"{mystack.pop()} has been removed from the stack")
print(f"{mystack.pop()} has been removed from the stack")
