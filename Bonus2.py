input_number = int(input("Enter a number:"))


def even_numbers(n):
    for i in range(1, n + 1):
        if i % 2 == 0:
            yield i


for numbers in even_numbers(input_number):
    print(numbers)
