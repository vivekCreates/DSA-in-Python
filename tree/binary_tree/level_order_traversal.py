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
            f= self.front
            self.front+=1
            self.length-=1
            return self.queue[f]
        
            
    def peek(self):
        print(self.queue[self.front])
        
    def size(self):
        return self.length
    


class Node:
    def __init__(self,value):
        self.data = value
        self.left = self.right = None
        
        
a = Node(3)
b = Node(2)
c = Node(4)
d = Node(1)
e = Node(5)
f = Node(6)
g = Node(9)

a.left = b
a.right = c
c.left = f
c.right = g
b.left = d
b.right = e


def level_order(root):
     q = Queue()
     q.enqueue(root)
     arr=[]
     while q.size()>0:
         
         front = q.dequeue()
         arr.append([front.data])
         print(front.data)
         if(front.left != None): q.enqueue(front.left)
         if(front.right != None): q.enqueue(front.right)
     
    
    
    
level_order(a)
