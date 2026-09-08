numbers = [23, 5, 67, 12, 89, 34]

maximum = numbers[0]
minimum = numbers[0]

for n in numbers:
    if n > maximum:
        maximum = n
    elif n < minimum:
        minimum = n

print(f"List: {numbers}")
print(f"Maximum: {maximum}")
print(f"Minimum: {minimum}")
