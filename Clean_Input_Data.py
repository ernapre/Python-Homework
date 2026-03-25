values = ["30", "45", "invalid", "100", "", "75"]
cleaned_values = []

for v in values:
    if v.isdigit():
        cleaned_values.append(int(v))

print(cleaned_values)
