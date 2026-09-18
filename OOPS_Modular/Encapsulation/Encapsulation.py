class Customer:
    def __init__(self, name, email):
        self.name = name          # public attribute
        self.__email = None       # private attribute
        self.email = email        # goes through the setter (validation)

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, value):
        if "@" not in value:
            raise ValueError("Invalid email address")
        self.__email = value


class Product:
    def __init__(self, name, price):
        self.name = name
        self.__price = None       # private attribute
        self.price = price        # goes through the setter (validation)

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value <= 0:
            raise ValueError("Price must be greater than 0")
        self.__price = value


class Order:
    def __init__(self, customer, product, quantity):
        self.customer = customer
        self.product = product
        self.__quantity = None    # private attribute
        self.quantity = quantity  # goes through the setter (validation)

    @property
    def quantity(self):
        return self.__quantity

    @quantity.setter
    def quantity(self, value):
        if value <= 0:
            raise ValueError("Quantity must be at least 1")
        self.__quantity = value

    def total_price(self):
        return self.product.price * self.__quantity


# ---------- Using the classes (valid objects) ----------

customer1 = Customer("Ravi Kumar", "ravi@example.com")
product1 = Product("Laptop", 50000)
order1 = Order(customer1, product1, 2)

print("Customer Email:", customer1.email)
print("Product Price:", product1.price)
print("Order Total:", order1.total_price())

print()

# ---------- Trying invalid data (validation in action) ----------

try:
    customer2 = Customer("Anita", "invalid-email")
except ValueError as e:
    print("Error creating customer:", e)

try:
    product2 = Product("Phone", -100)
except ValueError as e:
    print("Error creating product:", e)

try:
    order2 = Order(customer1, product1, 0)
except ValueError as e:
    print("Error creating order:", e)
