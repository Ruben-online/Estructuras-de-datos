# Supermercado Sol

class Costumer:
    def __init__(self, first_name, last_name, phone_number, email):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.email = email
        self.next = None


class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.next = None


class Employee:
    def __init__(self, name, salary, date_of_hire):
        self.name = name
        self.salary = salary
        self.date_of_hire = date_of_hire
        self.next = None


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def search_Data(self, position_data):
        current = self.head
        while current:
            if current.data == position_data:
                return True
            current = current.next
        return False

    def add_Element(self, element):
        newNode = Node(element)
        newNode.next = self.head
        self.head = newNode

    def remove_Element(self, position_data):
        current = self.head
        prev = None

        while current:
            if current.data == position_data:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                return True
            prev = current
            current = current.next

        return False

    def replace_Element(self, old_element, new_element):
        current = self.head
        while current is not None:
            if current.data == old_element:
                current.data = new_element
                break
            current = current.next

    def print_List(self):
        current = self.head
        while current is not None:
            print(current.data, end='->')
            current = current.next
        print('None')

costumers = []
inventory = []
employees = []

costumers_linked_list = LinkedList()
inventory_linked_list = LinkedList()
employees_linked_list = LinkedList()

while True:
    print('Bienvenido al supermercado sol')
    print('1. Administrar clientes')
    print('2. Administrar inventario')
    print('3. Administrar turnos')
    print('4. Salir del programa')

    option = input('\nIngrese una opcion (1-4): ')

    if option == '1':
        while True:
            print('Menu de administracion de clientes')
            print('1. Buscar cliente')
            print('2. Añadir cliente')
            print('3. Borrar cliente')
            print('4. Editar cliente')
            print('5. Mostrar todos los clientes')
            print('6. Regresar al menu')

            client_option_menu = input('\nIngrese una opcion (1-6): ')

            if client_option_menu == '1':
                pass

            elif client_option_menu == '2':
                print("\nAñadir cliente:")
                first_name = input("Ingrese el primer nombre: ")
                last_name = input("Ingrese el Apellido: ")
                phone = input("Ingrese el numero de telefono: ")
                email = input("Ingrese el email: ")

                new_client = Costumer(first_name, last_name, phone, email)
                costumers_linked_list.add_Element(new_client)
                print('El cliente ha sido añadido')

            elif client_option_menu == '3':
                pass

            elif client_option_menu == '4':
                pass

            elif client_option_menu == '5':
                print('Lista de clientes: ')
                costumers_linked_list.print_List()

            elif client_option_menu == '6':
                break
            else:
                print('Por favor ingrese una opcion valida')

    elif option == '2':
        while True:
            print('Menu de administracion de productos')
            print('1. Buscar producto')
            print('2. Añadir producto')
            print('3. Borrar producto')
            print('4. Editar producto')
            print('5. Mostrar todos los productos')
            print('6. Regresar al menu')

            product_option_menu = input('\nIngrese una opcion del (1-6): ')

            if product_option_menu == '1':
                pass

            elif product_option_menu == '2':
                pass

            elif product_option_menu == '3':
                pass

            elif product_option_menu == '4':
                pass

            elif product_option_menu == '5':
                pass

            elif product_option_menu == '6':
                break
            else:
                print('Por favor ingrese una opcion valida')

    elif option == '3':
        while True:
            print('Menu de administracion de empleados')
            print('1. Buscar empleado')
            print('2. Añadir empleado')
            print('3. Borrar empleado')
            print('4. Editar empleado')
            print('5. Mostrar todos los empleados')
            print('6. Regresar al menu')

            employee_option_menu = input('\nIngrese una opcion del (1-6): ')

            if employee_option_menu == '1':
                pass

            elif employee_option_menu == '2':
                pass

            elif employee_option_menu == '3':
                pass

            elif employee_option_menu == '4':
                pass

            elif employee_option_menu == '5':
                pass

            elif employee_option_menu == '6':
                break
            else:
                print('Por favor ingrese una opcion valida')
