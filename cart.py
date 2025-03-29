class Cart:
    def __init__(self):
        self.cart_items = []

    def add_to_cart(self, product, quantity):
        if quantity > product.quantity:
            print(f"Stoc insuficient pentru produsul {product.name}.")
            return

        product.quantity -= quantity

        self.cart_items.append((product, quantity))
        print(f"{quantity} x {product.name} a fost adaugat în cos.")

    def calculate_total(self):
        total = sum(product.price * quantity for product, quantity in self.cart_items)
        return total

    def display_cart(self):
        if not self.cart_items:
            print("Cosul este gol.")
        else:
            print("Continutul cosului:")
            for product, quantity in self.cart_items:
                print(f"{quantity} x {product.name} - {product.price} RON fiecare")
            print(f"Valoarea totala: {self.calculate_total()} RON")