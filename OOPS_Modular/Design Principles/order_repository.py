# This class has ONE job: save orders to a file.
# It does not know about discounts, receipts, or email.

class OrderRepository:

    def __init__(self, filename="orders.txt"):
        self.filename = filename

    def save(self, item, total):
        with open(self.filename, "a") as f:
            f.write(f"{item},{total}\n")
