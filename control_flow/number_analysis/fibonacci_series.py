count = int(input("How many Fibonacci terms? "))
a, b = 0, 1
series = []
for i in range(count):
    if i >= count:         
        break
    series.append(a)
    a, b = b, a + b
print("Fibonacci series:", series)
