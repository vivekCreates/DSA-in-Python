#          1 
#     2         3
#  4    5    6    7


class Node:
    def __init__(self,value):
        self.data = value
        self.left = self.right = None
        
        
a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)
f = Node(5)
g = Node(7)

a.left = b
a.right = c
b.left = d
b.right = e
c.left = f
c.right = g


def invert_binary_tree(root):
    if root == None:
        return
    
    temp = root.left
    root.left=root.right
    root.right = temp
    invert_binary_tree(root.left)
    invert_binary_tree(root.right)
    
    
print(c.right.data)
invert_binary_tree(a)
print(c.right.data)