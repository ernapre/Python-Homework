def valid_transactions(transactions):
    valid_elements = []

    for t in transactions:
        if t["amount"] <= 0:
            continue
        if t["status"] != "success":
            continue

        valid_elements.append(t)

    return valid_elements


transactions = [
    {"customer_id": 1, "amount": 80, "status": "success"},
    {"customer_id": 2, "amount": -10, "status": "success"},
    {"customer_id": 3, "amount": 120, "status": "failed"},
    {"customer_id": 4, "amount": 60, "status": "success"}
]

result = valid_transactions(transactions)
for t in result:
    print(t)
