class Orders:
    def __init__(self):
        self.cart = []
    def add_to_cart(self, item):
        self.cart.append(item)
    def remove(self, item):
        self.cart.remove(item)
    
    def __len__(self):
        return len(self.cart)
    def __str__(self):
        for order in self.cart:
            print(f"Cart Contains: {order}")