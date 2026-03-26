orders = [{"order_id": 1, "product": "Book", "price": 20},
          {"order_id": 2, "product": "", "price": 15},
          {"order_id": 3, "product": "Pen", "price": -5},
          {"order_id": None, "product": "Notebook", "price": 25}
          ]
invalid_records = []

for i in orders:
    reasons = []

    if i["order_id"] is None:
        reasons.append("order_id must not be None")

    if i["product"] == "":
        reasons.append("product must not be empty")

    if i["price"] <= 0:
        reasons.append("price must be positive")

    if reasons:
        invalid_records.append({
            "invalid records": i,
            "reason for issue": reasons
        })

for i in invalid_records:
    print(i)
