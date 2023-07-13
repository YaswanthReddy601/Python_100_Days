# Cart

class Cart:
    quantity = []
    cost = []
    total_cost = 0
    cart = {"pens": 0, "pencils": 0, "notebooks": 0, "erasers": 0, "chocolates": 0, "biscuits": 0}

    def add_cart(self, item, item_quantity, item_cost):
        global cart, cost, total_cost
        self.cart[item] += item_quantity
        self.cost.append(item_cost)
        self.total_cost = sum(self.cost)
        print("Your cart : ")
        for key, value in self.cart.items():
            if value > 0:
                print(f"\t{key} : {value}")
        print(f"your cart costs : {self.total_cost}")
        return self.total_cost

    def cleaning_cart(self):
        global cart, cost, total_cost
        self.quantity = []
        self.cost = []
        self.total_cost = 0
        self.cart = {"pens": 0, "pencils": 0, "notebooks": 0, "erasers": 0, "chocolates": 0, "biscuits": 0}