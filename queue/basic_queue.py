class Queue:
    
    def __init__(self):
        self.queue = [None] *10
        self.length = 0
        self.front = -1
        self.rear = -1
        
    def enqueue(self,value):
        if self.front < 0:
            self.front+=1
        self.rear+=1
        self.length+=1
        # print(self.rear)
        self.queue[self.rear] = value
        
    def dequeue(self):
        if self.front < 0:
             print("Queue is empty ! ")
        else:
            self.front+=1
            self.length-=1
            
    def peek(self):
        print(self.queue[self.front])
        
    def size(self):
        return self.length
    
    
    
q = Queue()

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
print(q.size())

q.peek()
q.dequeue()
print(q.size())
q.peek()        