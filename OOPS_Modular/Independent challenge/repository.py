# repository.py
# Repository layer, this is just the storage part.
# Only an in-memory version exists right now, a real one (SQL, etc.)
# could be swapped in later since the service only depends on this interface.


class OrderRepository:
    """Base class - defines what any storage backend needs to support."""

    def add(self, order):
        raise NotImplementedError

    def get(self, order_id):
        raise NotImplementedError

    def get_all(self):
        raise NotImplementedError

    def delete(self, order_id):
        raise NotImplementedError


class InMemoryOrderRepository(OrderRepository):
    """Mock repository that just stores orders in a dict. Used for tests."""

    def __init__(self):
        self._orders = {}

    def add(self, order):
        if order.order_id in self._orders:
            raise ValueError(f"order '{order.order_id}' already exists")
        self._orders[order.order_id] = order

    def get(self, order_id):
        return self._orders.get(order_id)

    def get_all(self):
        return list(self._orders.values())

    def delete(self, order_id):
        if order_id in self._orders:
            del self._orders[order_id]
