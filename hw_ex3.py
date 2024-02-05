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

    def nodes_Counter(self):
        count = 0
        current = self.head
        while current:
            count  += 1
            current = current.next
        return count

    def mult_Nodes(self):
        result = 1
        current = self.head
        while current:
            result *= current.data
            current = current.next
        return  result

my_linked_list = LinkedList()
my_linked_list.insert_Into_Empty_List(2)
my_linked_list.insert_Into_Empty_List(2)
my_linked_list.insert_Into_Empty_List(4)

print('Lista actual')
my_linked_list.print_List()

mult_nodes_result = my_linked_list.mult_Nodes()
print(f'El resultado de la multiplicacion de los nodos es: {mult_nodes_result}')