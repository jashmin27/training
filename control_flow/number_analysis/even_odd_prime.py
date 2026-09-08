
num = int(input("Enter a number: "))

if num % 2 == 0:
    print(num, "is Even")
else:
    print(num, "is Odd")

if num < 2:
    print(num, "is Not Prime")
else:
    prime = True
    for i in range(2, num):
        if num % i == 0:
            prime = False
            break

    if prime:
        print(num, "is Prime")
    else:
        print(num, "is Not Prime")
