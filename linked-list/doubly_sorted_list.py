class Node:
    def __init__(self,value):
        self.data = value
        self.next = None
        self.prev = None
        
        
class DoublyList:
    def __init__(self):
        self.head = self.tail = None
    
    def insert_in_Sorted_list(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = self.tail = new_node
            return
        
        if value < self.head.data:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            return
       
           
        temp = self.head
        while temp.next and temp.next.data < value:
          temp = temp.next
        # Case 4: Insert at end
        if temp.next is None:
            temp.next = new_node
            new_node.prev = temp
            self.tail = new_node
        else:
            # Case 3: Insert in middle
            new_node.next = temp.next
            new_node.prev = temp
            temp.next = new_node
                    

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next
            
            


dll = DoublyList()
dll.insert_in_Sorted_list(5)
dll.insert_in_Sorted_list(2)
dll.insert_in_Sorted_list(4)
dll.insert_in_Sorted_list(3)
dll.insert_in_Sorted_list(1)
dll.insert_in_Sorted_list(8)
dll.insert_in_Sorted_list(12)
dll.insert_in_Sorted_list(0)
dll.print_list()