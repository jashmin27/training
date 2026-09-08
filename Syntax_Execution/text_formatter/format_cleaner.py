
text = input("Enter text with extra spaces/punctuation: ")

cleaned = text.strip()                      # remove leading/trailing spaces
cleaned = cleaned.replace("  ", " ")        # collapse double spaces
cleaned = cleaned.replace(",", "").replace(".", "")  # remove punctuation

print("Original :", repr(text))
print("Cleaned  :", repr(cleaned))
