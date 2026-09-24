# repositories layer
# This layer is only about saving and loading data (the file).
# It does not care about business rules like "amount must be positive".

from settings import FILE_NAME
from helpers import parse_line


class ExpenseRepository:

    def __init__(self):
        # make sure the file exists
        open(FILE_NAME, "a").close()

    def save(self, name, amount):
        with open(FILE_NAME, "a") as f:
            f.write(f"{name},{amount}\n")

    def get_all(self):
        expenses = []
        with open(FILE_NAME, "r") as f:
            for line in f:
                if line.strip() != "":
                    expenses.append(parse_line(line))
        return expenses
