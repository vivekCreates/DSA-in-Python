class Node:
    def __init__(self,value):
        self.data = value
        self.next = None

class Queue:
    def __init__(self):
        self.head = self.tail = None
        
    def enqueue(self,value):
        newNode = Node(value)
        if self.head is None:
            self.head = self.tail = newNode
            return
        else:
            self.tail.next = newNode
            self.tail = newNode
            
    def dequeue(self):
        if self.head is None:
            print("List is empty! ")
            return
        else:
            self.head = self.head.next
            
            
    def printList(self):
        if self.head is None:
            print("List is empty! ")
            return
        else:
            temp = self.head
            while temp:
                print(temp.data)
                temp = temp.next
                
                
q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)


q.printList()
q.dequeue()
q.printList()