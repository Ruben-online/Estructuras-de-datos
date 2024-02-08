# Ejercicio aplicando listas simplemente enlazadas
# Tienda de ropa de Mishell

class Product:

    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.next = None

class Inventory:

    def __init__(self):
        self.head = None

    def print_List(self):
        current = self.head
        while current is not None:
            print(current.name, current.price, end= '->')
            current = current.next
        print('None')

    def add_Product(self, name, price):
        new_product = Product(name, price)
        new_product.next = self.head
        self.head = new_product

    def delete_Product(self, name):
        current = self.head
        prev = None

        while current:
            if current.name == name:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                print(f"Producto '{name}' eliminado.")
                return
            prev = current
            current = current.next

        print(f"Producto '{name}' no encontrado en el inventario.")

    def product_In_Inventory(self, name):
        current = self.head
        while current:
            if current.name == name:
                return True
            current = current.next
        return False



store_inventory = Inventory()

while True:
    product_name = input('Ingrese el nombre del producto que desea agregar al inventario: ')
    print('o (salir) para dejar de ingresar productos')
    if product_name.lower() == 'salir':
        break

    product_price = float(input('Ingrese el precio del producto: '))

    store_inventory.add_Product(product_name, product_price)
    print(f"Producto '{product_name}' agregado al inventario.")

print('Inventario actual:')
store_inventory.print_List()

product = input('\nIngrese el nombre del producto que desea eliminar: ')
if store_inventory.product_In_Inventory(product):
    print(f'El producto {product} esta en el inventario')
    store_inventory.delete_Product(product)
else:
    print(f'El producto {product} no esta en el inventario')

print('\nInventario actualizado: ')
store_inventory.print_List()