# Payment
import datetime
from random import randint
from Customer import Customer

class Payment:
    name = ""
    total_money = 0
    mode = ""

    def final_Payment(self, money):
        global name, total_money
        if money == 0:
            print("You have 0 items in the cart, So your cart is not billable...")
        else:
            self.total_money = money
            print(f"Your bill is {money}")
            off = Payment().offers()
            if off == "offer":
                if self.total_money >= 200:
                    discount = randint(0, 10)
                    print(f"Congrats you got {discount}% discount from your bill")
                    discount_money = (discount / 100) * self.total_money
                    bill = self.total_money - discount_money
                    print(f"After discount your bill is : {bill}")
                else:
                    print("You are not eligible to monthly offer")
            else:
                print("Not Offer month")
            self.mode = Customer().mode_of_payment()
            self.name = Customer().name()
            Payment().billing(self.name, money, self.mode)

    def billing(self, name, money, mode):
        if name == "not paid":
            print("You have not paid the bill. Your items in cart is deleted...")
        else:
            bill = datetime.datetime.now()
            print("Bill:")
            print(f"\tMode of payment: {mode}")
            print(f"\ton {bill} {name} paid {money} for the products he bought in shop 'X'")

    def offers(self):
        random_month = randint(1, 12)
        current_month = datetime.datetime.now().month
        offer_months = [1, 8]
        if 6 == current_month or random_month == offer_months:
            return "offer"