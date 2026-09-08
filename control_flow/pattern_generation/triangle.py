
rows = int(input("Enter number of rows: "))

for i in range(1, rows + 1):
    spaces = " " * (rows - i)     # leading spaces to center the pyramid
    stars = "*" * (2 * i - 1)
    print(spaces + stars)
5