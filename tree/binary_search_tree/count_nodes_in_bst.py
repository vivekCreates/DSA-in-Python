class Node:
    def __init__(self,value):
        self.data = value
        self.left = self.right = None
        
        

a = Node(10)
b = Node(5)
c = Node(50)
d = Node(1)
e = Node(40)
f = Node(100)


a.left = b
a.right = c
b.left = d
c.left= e
c.right = f

def count_nodes(root, l, h):
    if root is None:
        return 0
    
    if root.data < l:
        return count_nodes(root.right, l, h)
    
    if root.data > h:
        return count_nodes(root.left, l, h)
    
    return 1 + count_nodes(root.left, l, h) + count_nodes(root.right, l, h)


print("count: ",count_nodes(a,4,100))