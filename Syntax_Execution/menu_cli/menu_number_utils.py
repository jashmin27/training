def is_even(n):
    return n % 2 == 0

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

while True:
    print("\n--- Number Utilities ---")
    print("1. Even or Odd\n2. Check Prime\n3. Factorial\n4. Exit")
    choice = input("Choose an option: ")

    if choice == "4":
        break
    elif choice in ("1", "2", "3"):
        num = int(input("Enter a number: "))
        if choice == "1":
            print("Even" if is_even(num) else "Odd")
        elif choice == "2":
            print("Prime" if is_prime(num) else "Not prime")
        elif choice == "3":
            print(f"Factorial: {factorial(num)}")
    else:
        print("Invalid choice.")
