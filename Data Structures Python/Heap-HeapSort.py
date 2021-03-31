class Heap:
    def __init__(self,heapSize):
        assert type(heapSize) == int
        self.HEAP_SIZE = heapSize
        self.heap = [0]*heapSize
        self.currentPosition = -1
        
    def _isFull(self):
        return self.currentPosition+1==self.HEAP_SIZE
    
    def _swap(self,first,second):
        self.heap[first], self.heap[second] = self.heap[second],self.heap[first]
    
    def _reOrderUpwards(self, index):
        parentIndex = (index-1)//2
        if parentIndex >=0 and self.heap[parentIndex] < self.heap[index]:
            self._swap(parentIndex,index)
            self._reOrderUpwards(parentIndex)
            
    def insert(self, value):
        if self._isFull():
            print('Heap is full could not insert')
            return
        self.currentPosition +=1
        self.heap[self.currentPosition] = value
        self._reOrderUpwards(self.currentPosition)
    
    def _reOrderDownwards(self, start, end):
        left = (2*start) +1
        right = (2*start) +2
        if end>left:
            if end>right:
                if self.heap[left]> self.heap[right]:
                    self._swap(start,left)
                    self._reOrderDownwards(left, end)
                else:
                    self._swap(start,right)
                    self._reOrderDownwards(right, end)
            else:
                self._swap(start,left)
                self._reOrderDownwards(left, end)
    
                    
    def heapsort(self):
        for i in range(self.currentPosition+1):
            print(self.heap[0], end=' ')
            self.heap[0],self.heap[self.currentPosition-i] = self.heap[self.currentPosition-i],self.heap[0]
            self._reOrderDownwards(0,self.currentPosition-i-1)
        