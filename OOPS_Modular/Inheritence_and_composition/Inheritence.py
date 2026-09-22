# Inheritance Example
# Notification, Payment and Reporting using inheritance


# ---------------- Notification ----------------
class Notification:
    def __init__(self, message):
        self.message = message

    def send(self):
        print("Sending Notification:", self.message)


# child class - is a Notification, extends it
class EmailNotification(Notification):
    def send(self):
        print("Sending Email:", self.message)


class SMSNotification(Notification):
    def send(self):
        print("Sending SMS:", self.message)


# ---------------- Payment ----------------
class Payment:
    def __init__(self, amount):
        self.amount = amount

    def pay(self):
        print("Paying", self.amount)

    def show_receipt(self):
        print("Receipt: Paid", self.amount)


class CreditCardPayment(Payment):
    def pay(self):
        print("Paying", self.amount, "using Credit Card")


class UpiPayment(Payment):
    def pay(self):
        print("Paying", self.amount, "using UPI")

    # overriding the parent method
    def show_receipt(self):
        print("UPI Receipt: Paid", self.amount)


# ---------------- Reporting ----------------
class Report:
    def __init__(self, data):
        self.data = data

    def generate(self):
        print("Simple Report:", self.data)


class PDFReport(Report):
    def generate(self):
        print("PDF Report:", self.data)


class ExcelReport(Report):
    def generate(self):
        print("Excel Report:", self.data)


# ---------------- Main ----------------
print("--- Notification ---")
n1 = EmailNotification("Your order is placed")
n2 = SMSNotification("Your OTP is 1234")
n1.send()
n2.send()

print()
print("--- Payment ---")
p1 = CreditCardPayment(500)
p2 = UpiPayment(300)
p1.pay()
p1.show_receipt()
p2.pay()
p2.show_receipt()

print()
print("--- Reporting ---")
r1 = PDFReport("Sales data")
r2 = ExcelReport("Sales data")
r1.generate()
r2.generate()
