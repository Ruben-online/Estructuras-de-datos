# 1. Si la lista esta vacia devolver #0

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def print_List(self):
        current =  self.head
        while current is not None:
            print(current.data, end = '->')
            current = current.next
        print('None')

    def insert_Into_Empty_List(self, element):
        newNode = Node(element)
        newNode.next = self.head
        self.head = newNode

    def is_Empty(self):
        return self.head is None

my_linked_list = LinkedList()

if my_linked_list.is_Empty():
    print('#0, la lista esta vacia')
else:
    print('#1, la lista no esta vacia')