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
        
    
       
def insert_at_back(st,value): 
    if st.size() == 0:
        st.push(value)
        return
    top = st.pop()
    insert_at_back(st,value)
    st.push(top)
    
    
 
def reverse(st):
    if st.size() == 0:
        return
    
    top = st.pop()
    reverse(st)
    insert_at_back(st,top)
    

s = Stack()

s.push(10)
s.push(20)
s.push(30)

print("Before Reverse: ",s.peek())
reverse(s)
print("After Reverse: ",s.peek())