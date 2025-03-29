class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def display_info(self):
        print(f"Numele produsului: {self.name}")
        print(f"Pret: {self.price} RON")
        print(f"Cantitate: {self.quantity}")

    def update_quantity(self, amount):
        self.quantity += amount
        print(f"Cantitate actualizata {self.name}: {self.quantity}")