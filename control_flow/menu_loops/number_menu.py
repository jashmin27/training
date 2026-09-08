def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

while True:
    print("\n--- Number Menu ---")
    print("1. Check Even/Odd")
    print("2. Check Prime")
    print("3. Exit")
    choice = input("Choose an option: ")

    if choice == "3":
        print("Goodbye!")
        break

    if choice not in ("1", "2"):
        print("Invalid choice, try again.")
        continue                   # skip straight to the next loop iteration

    num = int(input("Enter a number: "))
    if choice == "1":
        print("Even" if num % 2 == 0 else "Odd")
    elif choice == "2":
        print("Prime" if is_prime(num) else "Not Prime")
