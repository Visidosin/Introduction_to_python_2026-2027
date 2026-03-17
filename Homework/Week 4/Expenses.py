file = open("expenses.txt", "a")

while True:
    category = input("Enter expense category: ")
    amount = input("Enter amount: ")

    file.write(category + "," + amount + "\n")

    answer = input("Do you want to add another expense? (yes/no): ").lower()

    if answer != "yes":
        break

file.close()

print("Expenses saved to file.")