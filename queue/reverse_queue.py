class Stack:
    
    def __init__(self):
        self.stack = []
    
    def push(self, value):
        self.stack.append(value)
        
    def pop(self):
        if self.size() == 0:
            return None
        return self.stack.pop()
    
    def peek(self):
        if self.size() == 0:
            return None
        return self.stack[-1]
    
    def size(self):
        return len(self.stack)



class Queue:
    
    def __init__(self):
        self.queue = []
        
    def enqueue(self, value):
        self.queue.append(value)
        
    def dequeue(self):
        if self.size() == 0:
            return None
        return self.queue.pop(0)
    
    def peek(self):
        if self.size() == 0:
            return None
        return self.queue[0]
    
    def size(self):
        return len(self.queue)



def reverse_queue(q):
    s = Stack()
    
   
    while q.size() != 0:
        s.push(q.dequeue())
    
   
    while s.size() != 0:
        q.enqueue(s.pop())
    
    return q


q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

print("Before Reverse:", q.queue)

reverse_queue(q)

print("After Reverse:", q.queue)
