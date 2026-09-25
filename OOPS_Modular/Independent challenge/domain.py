# domain.py
# This holds the actual business object for our order system.
# Keeping validation here so an Order can never exist in a broken state.


class Order:
    def __init__(self, order_id, customer_name, items, status="PENDING"):
        self.order_id = order_id
        self.customer_name = customer_name
        self.items = items  # list of dicts like {"name": ..., "price": ..., "qty": ...}
        self.status = status
        self._validate()

    def _validate(self):
        if not self.order_id:
            raise ValueError("order_id is required")

        if not self.customer_name or not self.customer_name.strip():
            raise ValueError("customer_name cannot be empty")

        if not self.items:
            raise ValueError("an order must have at least one item")

        for item in self.items:
            if item.get("qty", 0) <= 0:
                raise ValueError(f"quantity must be positive for item '{item.get('name')}'")
            if item.get("price", 0) < 0:
                raise ValueError(f"price cannot be negative for item '{item.get('name')}'")

    def total(self):
        return sum(item["price"] * item["qty"] for item in self.items)

    def cancel(self):
        if self.status == "SHIPPED":
            raise ValueError("cannot cancel an order that has already shipped")
        self.status = "CANCELLED"

    def __repr__(self):
        return f"Order({self.order_id}, {self.customer_name}, status={self.status}, total={self.total()})"
