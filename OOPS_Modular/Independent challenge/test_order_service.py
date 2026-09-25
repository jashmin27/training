# test_order_service.py
# quick tests for the order service, using the in-memory repo as our mock

import unittest
from repository import InMemoryOrderRepository
from service import OrderService


class TestOrderService(unittest.TestCase):

    def setUp(self):
        # fresh repo + service before every test so they don't affect each other
        self.repo = InMemoryOrderRepository()
        self.service = OrderService(self.repo)

    def test_create_order_success(self):
        items = [{"name": "Keyboard", "price": 40, "qty": 2}]
        order = self.service.create_order("O1", "Rahul", items)
        self.assertEqual(order.order_id, "O1")
        self.assertEqual(order.total(), 80)

    def test_create_order_with_empty_items_fails(self):
        with self.assertRaises(ValueError):
            self.service.create_order("O2", "Rahul", [])

    def test_create_order_with_empty_name_fails(self):
        items = [{"name": "Mouse", "price": 20, "qty": 1}]
        with self.assertRaises(ValueError):
            self.service.create_order("O3", "   ", items)

    def test_duplicate_order_id_fails(self):
        items = [{"name": "Mouse", "price": 20, "qty": 1}]
        self.service.create_order("O4", "Anita", items)
        with self.assertRaises(ValueError):
            self.service.create_order("O4", "Anita", items)

    def test_get_order_not_found(self):
        with self.assertRaises(ValueError):
            self.service.get_order("does-not-exist")

    def test_cancel_order(self):
        items = [{"name": "Chair", "price": 100, "qty": 1}]
        self.service.create_order("O5", "Vikram", items)
        cancelled = self.service.cancel_order("O5")
        self.assertEqual(cancelled.status, "CANCELLED")

    def test_cancel_shipped_order_fails(self):
        items = [{"name": "Chair", "price": 100, "qty": 1}]
        order = self.service.create_order("O6", "Vikram", items)
        order.status = "SHIPPED"  # pretending it already shipped out
        with self.assertRaises(ValueError):
            self.service.cancel_order("O6")

    def test_negative_price_fails(self):
        items = [{"name": "Broken item", "price": -5, "qty": 1}]
        with self.assertRaises(ValueError):
            self.service.create_order("O7", "Divya", items)

    def test_get_order_total(self):
        items = [{"name": "Book", "price": 15, "qty": 3}]
        self.service.create_order("O8", "Divya", items)
        self.assertEqual(self.service.get_order_total("O8"), 45)


if __name__ == "__main__":
    unittest.main()
