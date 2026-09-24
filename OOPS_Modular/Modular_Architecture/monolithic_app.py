# This is the "before" version.
# Everything (settings, saving data, business logic, printing) is mixed
# together in one single file. This is called a "monolithic" app.

FILE_NAME = "expenses.txt"


def add_expense(name, amount):
    if amount <= 0:
        print("Amount must be greater than 0")
        return
    with open(FILE_NAME, "a") as f:
        f.write(f"{name},{amount}\n")
    print(f"Added expense: {name} - {amount}")


def get_total():
    total = 0
    with open(FILE_NAME, "r") as f:
        for line in f:
            name, amount = line.strip().split(",")
            total += float(amount)
    return total


def show_expenses():
    with open(FILE_NAME, "r") as f:
        for line in f:
            name, amount = line.strip().split(",")
            print(f"{name}: {amount}")


# main program
open(FILE_NAME, "a").close()
add_expense("Bus ticket", 20)
add_expense("Lunch", 100)
show_expenses()
print("Total spent:", get_total())
