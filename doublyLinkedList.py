"""
If the linked list is given an out of range index, it just returns without throwing an error.
Error value can be attached to it, I just didn't want to confuse myself with error and value

All methods work perfectly with the most complex in half the size of the LinkedList.
"""
class Node:
    def __init__(self,val):
        self.val = val
        self.previous = None
        self.next = None
        
class DoublyLinkedList:
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
        ##Dynamic
        neg_index = self.size * (-1)
        if index >= self.size or index < neg_index:
            return
        if index < 0:
            #Make index positive for simplicity only if negative index is passed
            index = index + self.size
        
        if index <= self.size//2:
            #Iterare from head
            i = index
            current = self.head
            while i != 0:
                current = current.next
                i-=1
            return current.val
        else:
            #Iterate from tail
            i = self.size - index - 1
            current = self.tail
            while i != 0:
                current = current.previous
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
            self.head.previous = newNode
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
            newNode.previous = self.tail
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
            if index <= self.size//2:
                #Iterare from head
                newNode = Node(value)
                i = index - 1
                current = self.head
                while i != 0:
                    current = current.next
                    i-=1
                newNode.next = current.next
                newNode.previous = current
                current.next.previous = newNode
                current.next = newNode
                self.size +=1

            else:
                #Iterate from tail
                newNode = Node(value)
                i = self.size - index
                current = self.tail
                while i != 0:
                    current = current.previous
                    i-=1
                newNode.next = current.next
                newNode.previous = current
                current.next.previous = newNode
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
        current = self.head.next
        current.previous = None
        self.head = current
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
        current = self.tail.previous
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
            if index <= self.size//2:
                #Iterare from head
                i = index - 1
                current = self.head
                while i != 0:
                    current = current.next
                    i-=1
                current.next = current.next.next
                current.next.previous = current
                self.size -=1

            else:
                #Iterate from tail
                i = self.size - index
                current = self.tail
                while i != 0:
                    current = current.previous
                    i-=1
                current.next = current.next.next
                current.next.previous = current
                self.size -=1
    
    def getSize(self):
        """
        Returns the size of the linked list
        """
        return self.size
    
