
def is_palindrome(s):
    cleaned = s.lower().replace(" ", "")
    return cleaned == cleaned[::-1]

text = input("Enter a word or phrase: ")

print(f"Reversed: {text[::-1]}")
print(f"Centered (width 30): '{text.center(30, '*')}'")
print(f"Left aligned (width 20): '{text.ljust(20, '.')}'")
print(f"Right aligned (width 20): '{text.rjust(20, '.')}'")
print(f"Is Palindrome? {is_palindrome(text)}")
