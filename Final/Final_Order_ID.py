import csv
import os

FILE = "orders.csv"

# create file if it doesn't exist
if not os.path.exists(FILE):
    with open(FILE, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["id", "name", "address", "description", "date", "amount", "status"])


def get_next_id():
    with open(FILE, "r") as f:
        lines = list(csv.reader(f))
        return len(lines)


def add_order():
    name = input("Customer name: ")
    address = input("Address: ")
    desc = input("Description: ")
    date = input("Date (YYYY/MM/DD): ")
    amount = input("Total amount: ")

    order_id = get_next_id()

    with open(FILE, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([order_id, name, address, desc, date, amount, "pending"])

    print("Order added!")


def mark_delivered():
    order_id = input("Enter order ID: ")
    rows = []

    with open(FILE, "r") as f:
        reader = csv.reader(f)
        rows = list(reader)

    for row in rows:
        if row[0] == order_id:
            row[6] = "delivered"

    with open(FILE, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(rows)

    print("Order updated!")


def stats():
    name = input("Customer name: ")
    pending = 0
    count = 0

    with open(FILE, "r") as f:
        reader = csv.reader(f)
        next(reader)

        for row in reader:
            if row[1] == name:
                count += 1
                if row[6] == "pending":
                    pending += 1

    print("Total orders:", count)
    print("Pending orders:", pending)


while True:
    print("1. Add order")
    print("2. Order delivered")
    print("3. Statistics")
    print("4. Exit")

    choice = input("Choose: ")

    if choice == "1":
        add_order()
    elif choice == "2":
        mark_delivered()
    elif choice == "3":
        stats()
    elif choice == "4":
        break