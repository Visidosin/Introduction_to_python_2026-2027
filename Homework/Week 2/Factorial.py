def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result = result * i
    return result

print("Factorial Calculation")

num = int(input("Enter a number: "))
print("Factorial of", num, "is", factorial(num))