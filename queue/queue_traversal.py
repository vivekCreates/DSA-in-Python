class Queue:
    
    def __init__(self):
        self.queue = []
        self.length = 0
        self.front = -1
        self.rear = -1
        
    def enqueue(self,value):
        if self.front < 0:
            self.front+=1
        self.rear+=1
        self.length+=1
        self.queue.append(value)
        
    def dequeue(self):
        if self.front < 0:
             print("Queue is empty ! ")
        else:
            self.front+=1
            self.length-=1
            
    def peek(self):
        if self.length == 0:
            print("Queue is empty !")
            return
        else:
            print(self.queue[self.front])
        
    def size(self):
        return self.length
    
    def printQueue(self):
        for i in range(self.length):
            print(self.queue[i])
            self.enqueue(self.dequeue())
            
        
    
    
    
q = Queue()

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
     
q.printQueue()
q.dequeue()
q.printQueue()