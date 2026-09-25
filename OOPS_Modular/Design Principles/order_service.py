# This class has ONE job: coordinate placing an order.
# It does not calculate discounts itself, does not save files itself,
# and does not know if the notifier sends email or something else.
# It just uses the other pieces (dependency inversion - it depends on
# the Notifier interface, not on a specific class like EmailNotifier).

class OrderService:

    def __init__(self, discount_calculator, repository, printer, notifier):
        self.discount_calculator = discount_calculator
        self.repository = repository
        self.printer = printer
        self.notifier = notifier

    def create_order(self, item, price, quantity, customer_email):
        if price <= 0 or quantity <= 0:
            print("Invalid order")
            return

        total = self.discount_calculator.calculate_total(price, quantity)
        self.repository.save(item, total)
        self.printer.print_receipt(item, total)
        self.notifier.send(customer_email, f"Your order for {item} is confirmed.")
