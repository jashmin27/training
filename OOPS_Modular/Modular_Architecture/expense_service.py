# services layer
# This is where business rules live, like checking the amount is valid
# or calculating the total. It uses the repository, but does not know
# HOW the repository saves data (file, memory, database, etc).


class ExpenseService:

    def __init__(self, repository):
        self.repository = repository

    def add_expense(self, name, amount):
        if amount <= 0:
            print("Amount must be greater than 0")
            return
        self.repository.save(name, amount)
        print(f"Added expense: {name} - {amount}")

    def show_expenses(self):
        expenses = self.repository.get_all()
        for name, amount in expenses:
            print(f"{name}: {amount}")

    def get_total(self):
        expenses = self.repository.get_all()
        total = 0
        for name, amount in expenses:
            total += amount
        return total
