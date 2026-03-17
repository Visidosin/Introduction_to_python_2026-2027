totals = {}

file = open("expenses.txt", "r")

for line in file:
    line = line.strip()
    if line == "":
        continue
    
    parts = line.split(",")
    category = parts[0]
    amount = float(parts[1])
    
    if category in totals:
        totals[category] += amount
    else:
        totals[category] = amount

file.close()

sorted_totals = sorted(totals.items(), key=lambda x: x[1], reverse=True)

print("Total expenses by category (descending order):")
for category, total in sorted_totals:
    print(category, ":", total)