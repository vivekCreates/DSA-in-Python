# Implement a delete_from_front method that removes and returns the head of
# the list. Hint: This is an edge case in the general-purpose delete method.
# 
# 

from string import printable


class Node:
    def __init__(self,value) -> None:
        self.data = value
        self.next = None
        


class Singly_linked_list:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        
    def insert_front(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
            
            
    def insert_back(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            temp = self.head
            while temp:
                temp = temp.next
            
            self.tail.next = temp
            self.tail = temp
            
    def pop_front(self):
        temp = self.head
        self.head = temp.next
        return temp
    
    def printList(self,cb):
        if self.head is None:
            print("List is empty! ")
            return
        else:
            temp = self.head
            while temp:
                cb(temp.data)
                print(temp.data)
                temp = temp.next
            
      
        
l = []

def convert_linked_list_to_list(data):
    l.append(data)

sll = Singly_linked_list()
sll.insert_front(10)
sll.insert_front(20)
sll.insert_front(30)
sll.insert_front(30)
sll.insert_back(40)
head = sll.pop_front()
sll.printList(convert_linked_list_to_list)

print(l)