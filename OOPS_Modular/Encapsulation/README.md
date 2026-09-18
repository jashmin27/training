# 5.2 Encapsulation

## What I Learned
- Public and private attributes (using `_` and `__` naming convention)
- Properties (`@property` and `@<name>.setter`)
- Validation inside setters
- Preventing invalid object state

## Task
I updated the `Customer`, `Product`, and `Order` classes to protect their data:
- **Customer** – email must contain "@", otherwise it raises an error.
- **Product** – price must be greater than 0.
- **Order** – quantity must be at least 1.

The real value (like `__email`, `__price`, `__quantity`) is kept private using double underscore, and access is only allowed through properties. This way, no one can set a wrong value directly.

## How it Works
1. When we try to set a value (example: `customer1.email = "wrong"`), Python calls the setter method.
2. The setter checks if the value is valid.
3. If the value is invalid, it raises a `ValueError` and the object is NOT updated.
4. If the value is valid, it is stored safely in the private attribute.

## How to Run
```
python encapsulation.py
```

## Example Output
```
Customer Email: ravi@example.com
Product Price: 50000
Order Total: 100000

Error creating customer: Invalid email address
Error creating product: Price must be greater than 0
Error creating order: Quantity must be at least 1
```

## Simple Explanation
Encapsulation means hiding the internal data of an object and only allowing changes through controlled methods (getters/setters). This keeps the object always in a valid state, without adding too many extra rules (no overengineering — just simple checks where needed).
