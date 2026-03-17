import random

numbers = []

for i in range(20):
    numbers.append(random.randint(1, 100))

print("List:", numbers)

total = 0

print("Even numbers:")
for num in numbers:
    if num % 2 == 0:
        print(num)
        total = total + num

print("Total of even numbers:", total)

numbers2 = []
for i in range(20):
    numbers2.append(random.randint(1, 100))

print("Second list:", numbers2)

print("Numbers from the second list that appear in the first list:")
for num in numbers2:
    if num in numbers:
        print(num)