# Shop
from Cart import Cart
from Customer import Customer as Cust
from Payment import Payment
from Vendor import Vendor



class InventoryShop:
    pencils = {"quantity": 10, "price": 3}
    pens = {"quantity": 10, "price": 5}
    notebooks = {"quantity": 10, "price": 20}
    erasers = {"quantity": 10, "price": 2}
    chocolates = {"quantity": 10, "price": 1}
    biscuits = {"quantity": 10, "price": 5}
    total_cost = 0
    quantity = 0
    total = 0
    cart = Cart()
    count = 0
    name = ""


    def asking(self, shopping="yes"):
        self.cart.cleaning_cart()
        if "offer" == Payment().offers():
            print(
                "This is 'OFFER' month. you can get upto 10% discount if you buy products worth of minimun 200 rupees")
        while shopping == "yes" or shopping == "Yes":
            print("What do you want(one item and 10 pieces at a time)?")
            self.total_cost, shopping = Cust().selecting_items()
        Payment().final_Payment(self.total_cost)

    def out_of_stock(self, items):
        item = Vendor().refill(items)
        return item

    def pencil(self):
        global pencils
        if self.pencils["quantity"] >= 1:
            print(f"Ok! each pencil cost is {self.pencils['price']} rupees, How many pencils do you want?:")
            quantity = Cust().choose_quantity()
            if self.pencils["quantity"] >= quantity:
                self.pencils["quantity"] = self.pencils["quantity"] - quantity
                cost = self.pencils["price"] * quantity
                print(f"{quantity} pencils cost is {cost} rupees can i add to cart")
                opt = Cust().choose_decide()
                if opt == "yes" or opt == "Yes":
                    self.total = self.cart.add_cart("pencils", quantity, cost)
                    self.shopping = input("Do you want any thing else to buy(Yes/No)")
                    return self.total, self.shopping
                else:
                    self.total = self.cart.total_cost
                    self.shopping = input("Do you want any thing else to buy(Yes/No)")
                    return self.total, self.shopping
            else:
                print(
                    f"sorry sir, we have only {self.pencils['quantity']} pencils! please wait for 5 seconds to refill the pencils")
                self.pencils["quantity"] = InventoryShop().out_of_stock("pencils")
                self.total, self.shopping = InventoryShop().pencil()
                return self.total, self.shopping
        else:
            print("Sorry sir, we dont have pencils!! please wait for 5 seconds to refill the pencils")
            self.pencils["quantity"] = InventoryShop().out_of_stock("pencils")
            self.total, self.shopping = InventoryShop().pencil()
            return self.total, self.shopping

    def pen(self):
        global pens
        if self.pens["quantity"] >= 1:
            print(f"Ok! each pen cost is {self.pens['price']} rupees, How many pens do you want?:")
            quantity = Cust().choose_quantity()
            if self.pens["quantity"] >= quantity:
                self.pens["quantity"] = self.pens["quantity"] - quantity
                cost = self.pens["price"] * quantity
                print(f"{quantity} pens cost is {cost} rupees can i add to cart")
                opt = Cust().choose_decide()
                if opt == "yes" or opt == "Yes":
                    self.total = self.cart.add_cart("pens", quantity, cost)
                    self.shopping = input("Do you want any thing else (Yes/No)")
                    return self.total, self.shopping
                else:
                    self.total = self.cart.total_cost
                    self.shopping = input("Do you want any thing else (Yes/No)")
                    return self.total, self.shopping
            else:
                print(
                    f"Sorry sir, we have only {self.pens['quantity']} pens! please wait for 5 seconds to refill the pens")
                self.pens["quantity"] = InventoryShop().out_of_stock("pens")
                self.total, self.shopping = InventoryShop().pen()
                return self.total, self.shopping
        else:
            print("Sorry sir, we dont have pens!! please wait for 5 seconds to refill the pens")
            self.pens["quantity"] = InventoryShop().out_of_stock("pens")
            self.total, self.shopping = InventoryShop().pen()
            return self.total, self.shopping

    def notebook(self):
        global notebooks
        if self.notebooks["quantity"] >= 1:
            print(f"Ok! each notebook cost is {self.notebooks['price']} rupees, How many notebooks do you want?:")
            quantity = Cust().choose_quantity()
            if self.notebooks["quantity"] >= quantity:
                self.notebooks["quantity"] = self.notebooks["quantity"] - quantity
                cost = self.notebooks["price"] * quantity
                print(f"{quantity} notebooks cost is {cost} rupees can i add to cart")
                opt = Cust().choose_decide()
                if opt == "yes" or opt == "Yes":
                    self.total = self.cart.add_cart("notebooks", quantity, cost)
                    self.shopping = input("Do you want any thing else (Yes/No)")
                    return self.total, self.shopping
                else:
                    self.total = self.cart.total_cost
                    self.shopping = input("Do you want any thing else (Yes/No)")
                    return self.total, self.shopping
            else:
                print(
                    f"Sorry sir, we have only {self.notebooks['quantity']} notebooks! please wait for 5 seconds to refill the notebooks")
                self.notebooks["quantity"] = InventoryShop().out_of_stock("notebooks")
                self.total, self.shopping = InventoryShop().notebook()
                return self.total, self.shopping
        else:
            print("Sorry sir, we dont have notebooks!! please wait for 5 seconds to refill the notebooks")
            self.notebooks["quantity"] = InventoryShop().out_of_stock("notebooks")
            self.total, self.shopping = InventoryShop().notebook()
            return self.total, self.shopping

    def eraser(self):
        global erasers
        if self.erasers["quantity"] >= 1:
            print(f"Ok! each eraser cost is {self.erasers['price']} rupees, How many erasers do you want?:")
            quantity = Cust().choose_quantity()
            if self.erasers["quantity"] >= quantity:
                self.erasers["quantity"] = self.erasers["quantity"] - quantity
                cost = self.erasers["price"] * quantity
                print(f"{quantity} erasers cost is {cost} rupees can i add to cart")
                opt = Cust().choose_decide()
                if opt == "yes" or opt == "Yes":
                    self.total = self.cart.add_cart("erasers", quantity, cost)
                    self.shopping = input("Do you want any thing else (Yes/No)")
                    return self.total, self.shopping
                else:
                    self.total = self.cart.total_cost
                    self.shopping = input("Do you want any thing else (Yes/No)")
                    return self.total, self.shopping
            else:
                print(
                    f"Sorry sir, we have only {self.erasers['quantity']} erasers! please wait for 5 seconds to refill the erasers")
                self.erasers["quantity"] = InventoryShop().out_of_stock("erasers")
                self.total, self.shopping = InventoryShop().erasers()
                return self.total, self.shopping
        else:
            print("Sorry sir, we dont have erasers!! please wait for 5 seconds to refill the erasers")
            self.erasers["quantity"] = InventoryShop().out_of_stock("erasers")
            self.total, self.shopping = InventoryShop().erasers()
            return self.total, self.shopping

    def chocolate(self):
        global chocolates
        if self.chocolates["quantity"] >= 1:
            print(f"Ok! each chocolates cost is {self.chocolates['price']} rupees, How many chocolates do you want?:")
            quantity = Cust().choose_quantity()
            if self.chocolates["quantity"] >= quantity:
                self.chocolates["quantity"] = self.chocolates["quantity"] - quantity
                cost = self.chocolates["price"] * quantity
                print(f"{quantity} chocolates cost is {cost} rupees can i add to cart")
                opt = Cust().choose_decide()
                if opt == "yes" or opt == "Yes":
                    self.total = self.cart.add_cart("chocolates", quantity, cost)
                    self.shopping = input("Do you want any thing else (Yes/No)")
                    return self.total, self.shopping
                else:
                    self.total = self.cart.total_cost
                self.shopping = input("Do you want any thing else (Yes/No)")
                return self.total, self.shopping

            else:
                print(
                    f"sorry sir, we have only {self.chocolates['quantity']} chocolates! please wait for 5 seconds to refill the chocolates")
                self.chocolates["quantity"] = InventoryShop().out_of_stock("chocolates")
                self.total, self.shopping = InventoryShop().chocolate()
                return self.total, self.shopping
        else:
            print("Sorry sir, we dont have chocolates!! please wait for 5 seconds to refill the chocolates")
            self.chocolates["quantity"] = InventoryShop().out_of_stock("chocolates")
            self.total, self.shopping = InventoryShop().chocolate()
            return self.total, self.shopping

    def biscuit(self):
        global biscuits
        if self.biscuits["quantity"] >= 1:
            print(f"Ok! each biscuits cost is {self.biscuits['price']} rupees, How many biscuits do you want?:")
            quantity = Cust().choose_quantity()
            if self.biscuits["quantity"] >= quantity:
                self.biscuits["quantity"] = self.biscuits["quantity"] - quantity
                cost = self.biscuits['price'] * quantity
                print(f"{quantity} biscuits cost is {cost} rupees can i add to cart")
                opt = Cust().choose_decide()
                if opt == "yes" or opt == "Yes":
                    self.total = self.cart.add_cart("biscuits", quantity, cost)
                    self.shopping = input("Do you want any thing else (Yes/No)")
                    return self.total, self.shopping
                else:
                    self.total = self.cart.total_cost
                    self.shopping = input("Do you want any thing else (Yes/No)")
                    return self.total, self.shopping

            else:
                print(f"sorry sir, we have only {self.biscuits['quantity']} biscuits!  please wait for 5 seconds to refill the biscuits")
                self.biscuits["quantity"] = InventoryShop().out_of_stock("biscuits")
                self.total, self.shopping = InventoryShop().biscuit()
                return self.total, self.shopping
        else:
            print("Sorry sir, we dont have biscuits!! please wait for 5 seconds to refill the biscuits")
            self.biscuits["quantity"] = InventoryShop().out_of_stock("biscuits")
            self.total, self.shopping = InventoryShop().biscuit()
            return self.total, self.shopping


