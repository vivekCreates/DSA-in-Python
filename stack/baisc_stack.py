class Stack:
    
    def __init__(self):
        self.stack = []
    
    
    def push(self,value):
        self.stack.append(value)
        
        
    def pop(self):
        self.stack.pop()
        
    def peek(self):
        if len(self.stack) == 0:
            print("Stack is empty! ")
        else:
            return self.stack[len(self.stack)-1]
        
        

s = Stack()
s.push(10)
print(s.peek())
s.push(20)
print(s.peek())
s.push(30)
s.pop()
print(s.peek())