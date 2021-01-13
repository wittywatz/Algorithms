class Stack():
    def __init__(self):
        self.stack = []
    
    def push(self,element):
        """
        Adds element into stack
        """
        self.stack.append(element)
            
    def pop(self):
        """
        Returns the value of the popped element
        """
        if self.stack == []:
            return None
        return self.stack.pop(-1)
    
    def top(self):
        """
        Returns the value at the top
        """
        if self.stack == []:
            return None
        return self.stack[-1]


    
mystack = Stack()
mystack.push(3)
mystack.push(2)
mystack.push(1)
mystack.push(4)
mystack.push(1)
mystack.push(4)
print(f"The top element in the stack is {mystack.top()}")
print(f"{mystack.pop()} has been removed from the stack")
print(f"{mystack.pop()} has been removed from the stack")
print(f"{mystack.pop()} has been removed from the stack")
print(f"{mystack.pop()} has been removed from the stack")
print(f"{mystack.pop()} has been removed from the stack")
print(f"The top element in the stack is {mystack.top()}")
print(f"{mystack.pop()} has been removed from the stack")
