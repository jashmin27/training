# utils layer
# Small reusable helper functions that don't belong to one specific layer.


def parse_line(line):
    # turns "Lunch,100" into ("Lunch", 100.0)
    name, amount = line.strip().split(",")
    return name, float(amount)
