# Composition Example
# Notification, Payment and Reporting using composition
# Here a class HAS another object inside it, instead of extending it


# ---------------- Notification ----------------
class EmailSender:
    def send(self, message):
        print("Sending Email:", message)


class SMSSender:
    def send(self, message):
        print("Sending SMS:", message)


class Notification:
    def __init__(self, sender):
        self.sender = sender  # Notification has a sender

    def notify(self, message):
        self.sender.send(message)


# ---------------- Payment ----------------
class CreditCard:
    def pay(self, amount):
        print("Paying", amount, "using Credit Card")


class Upi:
    def pay(self, amount):
        print("Paying", amount, "using UPI")


class Payment:
    def __init__(self, method, amount):
        self.method = method  # Payment has a payment method
        self.amount = amount

    def make_payment(self):
        self.method.pay(self.amount)
        print("Receipt: Paid", self.amount)


# ---------------- Reporting ----------------
class PDFFormat:
    def show(self, data):
        print("PDF Report:", data)


class ExcelFormat:
    def show(self, data):
        print("Excel Report:", data)


class Report:
    def __init__(self, data, report_format):
        self.data = data
        self.report_format = report_format  # Report has a format

    def generate(self):
        self.report_format.show(self.data)


# ---------------- Main ----------------
print("--- Notification ---")
n1 = Notification(EmailSender())
n1.notify("Your order is placed")

n2 = Notification(SMSSender())
n2.notify("Your OTP is 1234")

print()
print("--- Payment ---")
pay1 = Payment(CreditCard(), 500)
pay1.make_payment()

pay2 = Payment(Upi(), 300)
pay2.make_payment()

print()
print("--- Reporting ---")
rep1 = Report("Sales data", PDFFormat())
rep1.generate()

rep2 = Report("Sales data", ExcelFormat())
rep2.generate()
