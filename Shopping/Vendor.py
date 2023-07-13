# Vendor
import time


class Vendor:

    def refill(self, items):
        item = 10
        print(f"{items} are refilling...")
        time.sleep(5)
        print(f"{items} are refilled")
        return item