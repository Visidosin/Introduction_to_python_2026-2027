sales = [
    [2020, 2.3, 2.2, 1.8, 3.1],
    [2021, 2.4, 2.0, 1.7, 3.0],
    [2022, 1.7, 1.2, 1.0, 1.8],
    [2023, 1.9, 1.0, 0.7, 2.0],
    [2024, 2.0, 2.4, 2.0, 3.2]
]

print("Total sales per year:")
for row in sales:
    year = row[0]
    total = row[1] + row[2] + row[3] + row[4]
    print(year, ":", total)

print("\nAverage sales per year:")
for row in sales:
    year = row[0]
    avg = (row[1] + row[2] + row[3] + row[4]) / 4
    print(year, ":", avg)

max_sale = 0
min_sale = 10
max_year = 0
min_year = 0
max_quarter = 0
min_quarter = 0

for row in sales:
    year = row[0]
    for i in range(1, 5):
        sale = row[i]

        if sale > max_sale:
            max_sale = sale
            max_year = year
            max_quarter = i

        if sale < min_sale:
            min_sale = sale
            min_year = year
            min_quarter = i

print("\nMax sale:", max_sale, "Year:", max_year, "Quarter:", max_quarter)
print("Min sale:", min_sale, "Year:", min_year, "Quarter:", min_quarter)