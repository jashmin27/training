# main.py
# This is where all the pieces are connected together.

from discount import DiscountCalculator
from order_repository import OrderRepository
from receipt_printer import ReceiptPrinter
from notifier import EmailNotifier
from order_service import OrderService

discount_calculator = DiscountCalculator()
repository = OrderRepository()
printer = ReceiptPrinter()
notifier = EmailNotifier()

service = OrderService(discount_calculator, repository, printer, notifier)
service.create_order("Laptop", 500, 3, "test@example.com")
