def logger(func):
    def wrapper(word):
        print("Input:", word)
        result = func(word)
        print("Output:", result)
        return result
    return wrapper


@logger
def make_upper(word):
    return word.upper()


text = input("Enter a word: ")
make_upper(text)
