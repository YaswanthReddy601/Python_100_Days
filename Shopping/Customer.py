# Customer
import getpass
from Inventory_Shop import InventoryShop
import Length_Exception

class Customer:
    name = ""
    total = 0

    def selecting_items(self):
        global total
        item = input("I want : ")
        if item == "pens":
            self.total = InventoryShop().pen()
            return self.total
        elif item == "pencils":
            self.total = InventoryShop().pencil()
            return self.total
        elif item == "notebooks":
            self.total = InventoryShop().notebook()
            return self.total
        elif item == "erasers":
            self.total = InventoryShop().eraser()
            return self.total
        elif item == "chocolates":
            self.total = InventoryShop().chocolate()
            return self.total
        elif item == "biscuits":
            self.total = InventoryShop().biscuit()
            return self.total
        else:
            print("Sorry we dont have that item")
            self.shopping = input("Do you want any thing else (Yes/No)")
            return self.total, self.shopping

    def choose_quantity(self):
        quant = int(input("I want : "))
        if quant > 10:
            print("Sorry you can only buy 10 at a time")
            InventoryShop().asking()
        elif quant < 0:
            print("Sorry invalid input")
            InventoryShop().asking()
        else:
            return quant

    def choose_decide(self):
        option = str(input("choose yes or no : "))
        return option

    def mode_of_payment(self):
        mode = input("Mode of payment cash or card :")
        if mode == "cash":
            return mode
        elif mode == "card":
            try:
                card_number_int = int(input("please enter your 16 digits card number : "))
                card_number = str(card_number_int)
                if len(card_number) > 16:
                    raise Length_Exception("Card number should not exeed 16 digits ")
                card_cvv_int = int(getpass.getpass("please enter your card 'CVV' : "))
                card_cvv = str(card_cvv_int)
                if len(card_cvv) > 3:
                    raise Length_Exception("Card cvv should not exeed 3 digits ")

            except ValueError:
                raise Length_Exception("You can only give integers as input")

            card_date = input("please enter expiry of the card : ")
            return mode

    def name(self):
        self.name = input("Enter your name :")
        return self.name