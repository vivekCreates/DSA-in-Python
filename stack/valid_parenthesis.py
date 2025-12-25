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
        
    


def valid_parenthesis(string):
    st = Stack()
    
    for b in string:
     
        if b == '{' or b == '(' or b == '[':
            st.push(b)
        
     
        elif b == '}' or b == ')' or b == ']':
            if st.size() == 0:
                return False
            
            top = st.peek()
            
            if (top == '{' and b == '}') or \
               (top == '(' and b == ')') or \
               (top == '[' and b == ']'):
                st.pop()
            else:
                return False
    
    return st.size() == 0



print(valid_parenthesis("{()}[]"))     
print(valid_parenthesis("{(]"))        
print(valid_parenthesis("((()))"))     
print(valid_parenthesis("{()}["))      
