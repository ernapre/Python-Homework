class InvalidQuantityError(Exception):
    pass


def quantity(q):
    if q <= 0 or q > 1000:
        raise InvalidQuantityError("Invalid quantity")
    return "Valid quantity"


try:
    print(quantity(int(input("Type the quantity number:"))))
except InvalidQuantityError as e:
    print("Error:", e)
