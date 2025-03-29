from product import Product
from product_manager import ProductManager
from cart import Cart

manager = ProductManager()


product1 = Product("Laptop", 3000, 10)
product2 = Product("Telefon", 1500, 20)
product3 = Product("Tableta", 800, 15)

manager.add_product(product1)
manager.add_product(product2)
manager.add_product(product3)


manager.display_all_products()

manager.calculate_total_value()

manager.remove_product("Telefon")

manager.display_all_products()

manager.remove_product("Televizor")

cart = Cart()

cart.add_to_cart(product1, 2)
cart.add_to_cart(product2, 1)
cart.add_to_cart(product3, 3)

cart.display_cart()

print(f"Valoarea totala de plata: {cart.calculate_total()} RON")
