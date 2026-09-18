# 5.1 Classes & Objects

## What I Learned
- Classes and Objects
- Attributes (data stored inside an object)
- Methods (functions inside a class)
- Constructor (`__init__` method)
- Class methods (using `@classmethod`)

## Task
I created four simple classes:
1. **Customer** – stores name and email of a customer.
2. **Product** – stores product name and price.
3. **Order** – connects a Customer and a Product, and calculates total price.
4. **Invoice** – generates an invoice for an order and keeps count of how many invoices were created using a class attribute.

## How it Works (Object Lifecycle)
1. We create a `Customer` object.
2. We create a `Product` object.
3. We create an `Order` object using the customer and product.
4. We create an `Invoice` object from the order, which prints the final bill.

## How to Run
```
python classes_objects.py
```

## Example Output
```
Order for: Ravi Kumar
Product: Laptop
Quantity: 2
Total Price: 100000

---- INVOICE ----
Invoice ID: 1
Customer: Ravi Kumar
Email: ravi@example.com
Product: Laptop
Quantity: 2
Total Amount: 100000
-----------------
Total Invoices Created: 1
```

## Simple Explanation
- **State** = the data stored inside an object (like `name`, `price`, `quantity`).
- **Behavior** = what an object can do (like `show_info()`, `total_price()`).
- **Lifecycle** = an object is created using the constructor, used through its methods, and then it exists until the program ends.
