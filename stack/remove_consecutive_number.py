class Stack:
    def __init__(self):
        self.stack = []
        
    def push(self,value):
        self.stack.append(value)
        
    def pop(self):
        return self.stack.pop()
    
    def peek(self):
        return self.stack[len(self.stack)-1] 
    
    def size(self):
        return len(self.stack)
    
    
def remove_consecutive_number(string):
    st = Stack()
    
    for b in string:
        if st.size() == 0:
            st.push(b)
        else:
            if st.peek() == b:
                continue
            else:
                st.push(b)

    result = ""
    while st.size() > 0:
        result = st.pop() + result
        
    return result



print(remove_consecutive_number("aaabbaacddee"))