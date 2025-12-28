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


def pre_order(root):
    if root == None:
        return
    print(root.data,end=" ")
    pre_order(root.left)
    pre_order(root.right)
    
    
def in_order(root):
    if root == None:
        return
    in_order(root.left)
    print(root.data,end=" ")
    in_order(root.right)
    
    
def post_order(root):
    if root == None:
        return
    post_order(root.left)
    post_order(root.right)
    
    print(root.data,end=" ")
    

print("pre: ",end=" ")
pre_order(a)
print("\nin: ",end=" ")
in_order(a)
print("\npost: ",end=" ")
post_order(a)
print(end="\n")

