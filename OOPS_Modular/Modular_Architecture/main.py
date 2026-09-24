# main.py
# This is the entry point. It connects all the layers together.

from expense_repository import ExpenseRepository
from expense_service import ExpenseService

repository = ExpenseRepository()
service = ExpenseService(repository)

service.add_expense("Bus ticket", 20)
service.add_expense("Lunch", 100)
service.show_expenses()
print("Total spent:", service.get_total())
