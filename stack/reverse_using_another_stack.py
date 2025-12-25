class Stack:
    
    def __init__(self):
        self.stack = []
    
    
    def push(self,value):
        self.stack.append(value)
        
        
    def pop(self):
        return self.stack.pop()
        
    def size(self):
        return len(self.stack)
    
    def peek(self):
        if len(self.stack) == 0:
            print("Stack is empty! ")
        else:
            return self.stack[len(self.stack)-1]
        
    

    
def reverse(st1,st2):
    if st1.size() == 0:
        print("stack 1 is empty ")
        return
    while(st1.size() > 0 ):
        top  = st1.pop()
        st2.push(top)
        

s1 = Stack()
s2 = Stack()

s1.push(10)
s1.push(20)
s1.push(30)



print("Before Reverse: ",s1.peek())
reverse(s1,s2)
print("After Reverse: ",s2.peek())