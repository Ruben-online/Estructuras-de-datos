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

    def nodes_counter(self):
        count = 0
        current = self.head
        while current:
            count  += 1
            current = current.next
        return count

my_linked_list = LinkedList()
my_linked_list.insert_Into_Empty_List(10)
my_linked_list.insert_Into_Empty_List(15)
my_linked_list.insert_Into_Empty_List(20)
my_linked_list.insert_Into_Empty_List(25)
my_linked_list.insert_Into_Empty_List(30)
my_linked_list.insert_Into_Empty_List(35)

nodes = my_linked_list.nodes_counter()
print(f'Numero de nodos en la lista es: {nodes}')