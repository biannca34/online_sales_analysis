from product import Product

class ProductManager:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)
        print(f"Produsul {product.name} a fost adaugat cu succes.")

    def remove_product(self, product_name):
        for product in self.products:
            if product.name == product_name:
                self.products.remove(product)
                print(f"Produsul {product_name} a fost eliminat cu succes.")
                return
        print(f"Produsul {product_name} nu exista in lista.")

    def display_all_products(self):
        if not self.products:
            print("Nu exista produse disponibile.")
        else:
            print("Produse disponibile:")
            for product in self.products:
                product.display_info()
                print("-" * 20)

    def calculate_total_value(self):
        total_value = sum(product.price * product.quantity for product in self.products)
        print(f"Valoarea totala a tuturor produselor: {total_value} RON")
        return total_value

manager = ProductManager()