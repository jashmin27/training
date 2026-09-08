def factorial(n):
    result = 1
    for i in range(1, n + 1):     
        result *= i
    return result

def sum_of_digits(n):
    total = 0
    n = abs(n)
    while n > 0:                  
        total += n % 10
        n = n // 10
    return total

num = int(input("Enter a number: "))
print(f"Factorial of {num}: {factorial(num)}")
print(f"Sum of digits: {sum_of_digits(num)}")
