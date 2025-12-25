class Node:
    def __init__(self,value):
        self.data = value 
        self.next  = None
        
class Circular_list:
    def __init__(self):
        self.head = self.tail = None
        
    def insert_at_back(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.tail.next = self.head
            
    def print_list(self):
        
        temp = self.head.next
        print(self.head.data)
        while temp != self.head:
            print(temp.data)
            temp = temp.next
                
        
    
cl = Circular_list()
cl.insert_at_back(10)
cl.insert_at_back(22)
cl.insert_at_back(19)
cl.insert_at_back(15)

cl.print_list()