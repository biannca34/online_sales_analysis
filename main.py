from product import Product
from product_manager import ProductManager


manager = ProductManager()


product1 = Product("Laptop", 3000, 10)
product2 = Product("Telefon", 1500, 20)
product3 = Product("Tableta", 800, 15)

manager.add_product(product1)
manager.add_product(product2)
manager.add_product(product3)

# Display all products
manager.display_all_products()

manager.calculate_total_value()