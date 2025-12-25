class Node:
    def __init__(self,value):
        self.data = value
        self.next = None
        
        
class Stack:
    def __init__(self):
        self.top = None
        
    def push(self,value):
        newNode = Node(value)
        if self.top is None:
            self.top = newNode
            return
        else:
            newNode.next = self.top
            self.top = newNode
            
    def pop(self):
        if self.top is None:
            print("Stack is empty! ")
            return
        else:
            self.top = self.top.next
            
    def peek(self):
        return self.top.data
    
    def size(self):
        count = 1
        temp = self.head
        while temp:
            count += 1
            temp = temp.next
        return count
    
    
    
    
st = Stack()

st.push(10)
st.push(20)
st.push(30)

print(st.peek())
st.pop()
print(st.peek())

