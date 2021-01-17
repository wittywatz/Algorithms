"""
If the linked list is given an out of range index, it just returns without throwing an error.
Error value can be attached to it, I just didn't want to confuse myself with error and value
"""
class Node:
    def __init__(self,val):
        self.val = val
        self.next = None
        
class LinkedList:
    """
    Works perfectly with negative indexing
    """
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def getElement(self, index):
        """
        Returns the value of element at a particular index
        """
        neg_index = self.size * (-1)
        if index >= self.size or index < neg_index:
            return
        if index < 0:
            #Make index positive for simplicity only if negative index is passed
            index = index + self.size
    
        i = index
        current = self.head
        while i != 0:
            current = current.next
            i-=1
        return current.val
       
    
    def insertAtHead(self, value):
        """
        Inserts new element at head with the value provided
        """
        newNode = Node(value)
        if self.head == None:
            self.head = newNode
            self.tail = newNode
        else:
            newNode.next = self.head
            self.head = newNode
        self.size +=1
        
    def insertAtTail(self, value):
        """
        Inserts new element at tail with the value provided
        """
        newNode = Node(value)
        if self.head == None:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode
        self.size +=1
    
    def insertAtIndex(self, value, index):
        """
        Inserts new element at any index with the value provided
        """
        neg_index = self.size * (-1)
        if index >= self.size or index < neg_index:
            return
        if index < 0:
            #Make index positive for simplicity only if negative index is passed
            index = index + self.size
        if index == 0:
            self.insertAtHead(value)
        elif index == self.size-1:
            self.insertAtTail(value)
        else:
            newNode = Node(value)
            i = index - 1
            current = self.head
            while i != 0:
                current = current.next
                i-=1
            newNode.next = current.next
            current.next = newNode
            self.size +=1
            
    def deleteAtHead(self):
        """
        Deletes element at head
        """
        if self.head == None:
            return
        if self.size == 1:
            self.head = None
            self.tail = None
            self.size -= 1
            return
        self.head = self.head.next
        self.size -= 1
      
    def deleteAtTail(self):
        """
        Deletes element at tail
        """
        if self.head == None:
            return
        if self.size == 1:
            self.head = None
            self.tail = None
            self.size -= 1
            return
        current = self.head
        
        while current.next.next:
            current = current.next
        current.next = None
        self.tail = current
        self.size -= 1
    
    def deleteAtIndex(self, index):
        """
        Deletes element at any given index
        """
        neg_index = self.size * (-1)
        if index >= self.size or index < neg_index:
            return
        if index < 0:
            #Make index positive for simplicity only if negative index is passed
            index = index + self.size
        if index == 0:
            self.deleteAtHead()
        elif index == self.size-1:
            self.deleteAtTail()
        else:
            i = index - 1
            current = self.head
            while i != 0:
                current = current.next
                i-=1
            current.next = current.next.next
            self.size -=1

    
    def getSize(self):
        """
        Returns the size of the linked list
        """
        return self.size
    
    def reverseList(self):
        """
        Reverses the linked list in place
        """
        
        next_node = None
        previous = None
        current = self.head
        i = 0
        while current:
            if i == 0:
                next_node = current.next
                current.next = previous
                previous = current
                current = next_node
                self.tail = previous
                i +=1
            else:
                next_node = current.next
                current.next = previous
                previous = current
                current = next_node 
        self.head = previous
            
