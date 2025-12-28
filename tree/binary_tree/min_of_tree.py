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


def minimum(root):
    if root == None:
        return float('inf')
    return min(root.data,minimum(root.left),minimum(root.right))
    
    
    
print("maximum: ",minimum(a))
