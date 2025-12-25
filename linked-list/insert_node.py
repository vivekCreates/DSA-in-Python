class Node:
    def __init__(self,value):
        self.data = value
        self.next = None
        
        
class SinglyList:
    def __init__(self):
        self.head = self.tail = None
    
    def insert(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
            
    
    def insert_at_position(self,value,postion):
        new_node = Node(value)
        if postion <= 0:
            print("Can't insert on negative or zero postion")
            return
        
        size = 0
        temp = self.head
        while temp:
            size+=1
            temp = temp.next
        
        if postion > size:
            print("List size is small than the postion!")
            return
        else:
            if self.head is None:
                print("List is empty!")
                return
            else:
                temp = self.head
                for i in range(postion-1):
                    temp = temp.next
                new_node.next = temp.next
                temp.next = new_node
                
        
                    

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next
            
            


sl = SinglyList()
sl.insert(20)
sl.insert(10)
sl.insert(30)
sl.insert_at_position(100,2)
sl.print_list()