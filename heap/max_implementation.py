class Max_heap:
    def __init__(self):
        self.heap = []
        
    def insert(self,element):
       self.heap.append(element)
       self.heapify_up(len(self.heap)-1)
       
        
    def pop(self):
        if len(self.heap) == 0:
            print("Heap is empty: ")
            return 
        
        if len(self.heap)==1:
            self.heap.pop()
            
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.heapify_down(0)
        
        return root
        
    def peek(self):
        return self.heap[0] if self.heap else None
    
    def heapify_up(self,index):
        parent_index = (index-1)//2
        
        while index > 0 and self.heap[index] > self.heap[parent_index]:
            self.heap[index],self.heap[parent_index] = self.heap[parent_index],self.heap[index]
            index = parent_index
            parent_index = (index-1)//2

    
    def heapify_down(self, index):
        size = len(self.heap)
        while True:
            left = 2 * index + 1
            right = 2 * index + 2
            largest = index
            if left < size and self.heap[left] > self.heap[largest]:
                largest = left
            if right < size and self.heap[right] > self.heap[largest]:
                largest = right
            if largest == index:
                break
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            index = largest



heap = Max_heap()
heap.insert(2)
heap.insert(7)
heap.insert(9)
heap.insert(4)
heap.insert(8)

print("peek: ",heap.peek())
heap.pop()
print("peek: ",heap.peek())


