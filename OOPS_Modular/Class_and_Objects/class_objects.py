class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def show_info(self):
        print("Customer Name:", self.name)
        print("Customer Email:", self.email)


class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def show_info(self):
        print("Product:", self.name, "- Price:", self.price)


class Order:
    def __init__(self, customer, product, quantity):
        self.customer = customer
        self.product = product
        self.quantity = quantity

    def total_price(self):
        return self.product.price * self.quantity

    def show_info(self):
        print("Order for:", self.customer.name)
        print("Product:", self.product.name)
        print("Quantity:", self.quantity)
        print("Total Price:", self.total_price())


class Invoice:
    invoice_count = 0   # class attribute to track number of invoices

    def __init__(self, order):
        Invoice.invoice_count += 1
        self.invoice_id = Invoice.invoice_count
        self.order = order

    def print_invoice(self):
        print("---- INVOICE ----")
        print("Invoice ID:", self.invoice_id)
        print("Customer:", self.order.customer.name)
        print("Email:", self.order.customer.email)
        print("Product:", self.order.product.name)
        print("Quantity:", self.order.quantity)
        print("Total Amount:", self.order.total_price())
        print("-----------------")

    @classmethod
    def total_invoices(cls):
        return cls.invoice_count


# ---------- Using the classes (creating objects) ----------

# Create a customer
customer1 = Customer("Ravi Kumar", "ravi@example.com")

# Create a product
product1 = Product("Laptop", 50000)

# Create an order
order1 = Order(customer1, product1, 2)

# Show order details
order1.show_info()

print()

# Create an invoice for the order
invoice1 = Invoice(order1)
invoice1.print_invoice()

# Show how many invoices have been created (class/static method usage)
print("Total Invoices Created:", Invoice.total_invoices())
