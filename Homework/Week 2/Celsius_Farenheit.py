def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) / 1.8

print("Temperature Conversion")

c = float(input("Enter temperature in Celsius: "))
print("Fahrenheit:", celsius_to_fahrenheit(c))

f = float(input("Enter temperature in Fahrenheit: "))
print("Celsius:", fahrenheit_to_celsius(f))