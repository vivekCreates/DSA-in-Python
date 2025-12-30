class Node:
    def __init__(self,value):
        self.data = value
        self.left = self.right = None
        
        

a = Node(10)
b = Node(3)
c = Node(15)
d = Node(2)
e = Node(4)
f = Node(12)
g = Node(17)

a.left = b
a.right = c
b.left = d
b.right = e
c.left=f
c.right=g


def minimum(root):
    temp = root
    while temp.left!=None:
        temp = temp.left
        
    return temp.data


def maximum(root):
    temp = root
    while temp.right!=None:
        temp = temp.right
        
    return temp.data


print("minimum: ",minimum(a))
print("maximum: ",maximum(a))