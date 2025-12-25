class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


class Singly_linked_list:
    def __init__(self):
        self.head = self.tail = None

    def pushFront(self, value):
        newNode = Node(value)
        if self.head is None:
            self.head = self.tail = newNode
        else:
            newNode.next = self.head
            self.head = newNode

    def print_list(self, head=None):
        if head is None:
            head = self.head
            return
        print(head.data, end=" -> ")
        self.print_list(head.next)



sll = Singly_linked_list()

head = sll.pushFront(10)
sll.pushFront(20)
sll.pushFront(30)
sll.pushFront(40)

sll.print_list(head)