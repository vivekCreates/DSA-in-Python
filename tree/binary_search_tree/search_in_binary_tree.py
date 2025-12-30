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


def search(root,target):
    if root==None:
        return False
    if target == root.data:
        return True
    elif target < root.data:
        return search(root.left,target)
    elif target > root.data:
        return search(root.right,target)
    else:
        return False
    
    
ans = search(a,15)
print("ans: ",ans)


