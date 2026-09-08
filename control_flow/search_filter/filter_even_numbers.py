
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = []

for n in numbers:
    if n % 2 != 0:
        continue          
    evens.append(n)

print("Even numbers :", evens)


