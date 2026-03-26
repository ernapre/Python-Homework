numbers = [2, 4, 6, 7, 9, 12, 15]

result = list(filter(lambda x: x % 2 == 0 and x > 5, numbers))

print(result)
