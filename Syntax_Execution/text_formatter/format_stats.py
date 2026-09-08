
text = input("Enter a sentence: ")

words = text.split()
num_words = len(words)
num_chars = len(text)
num_chars_no_spaces = len(text.replace(" ", ""))
num_sentences = text.count(".") + text.count("!") + text.count("?")

print(f"Words: {num_words}")
print(f"Characters (with spaces): {num_chars}")
print(f"Characters (no spaces): {num_chars_no_spaces}")
print(f"Sentences (approx): {max(num_sentences, 1)}")
