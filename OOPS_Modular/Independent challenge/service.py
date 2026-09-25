# service.py
# Service layer. This is where the actual workflow / business rules live.
# It only talks to the repository interface, so it doesn't care whether
# that's the in-memory mock or a real database later on.

from domain import Order


class OrderService:
    def __init__(self, repository):
        self.repository = repository

    def create_order(self, order_id, customer_name, items):
        order = Order(order_id, customer_name, items)
        self.repository.add(order)
        return order

    def get_order(self, order_id):
        order = self.repository.get(order_id)
        if order is None:
            raise ValueError(f"no order found with id '{order_id}'")
        return order

    def list_orders(self):
        return self.repository.get_all()

    def cancel_order(self, order_id):
        order = self.get_order(order_id)
        order.cancel()
        return order

    def get_order_total(self, order_id):
        order = self.get_order(order_id)
        return order.total()
