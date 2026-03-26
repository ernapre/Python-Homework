input_words = input("Enter a word you want to turn to uppercase:")
words = input_words.split()

upper_words = list(map(str.upper, words))

print(upper_words)
