class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.birthdate = ""
        self.phone_number = ""
    
    def set_birthdate(self, birthdate):
        self.birthdate = birthdate
    
    def set_phone_number(self, phone_number):
        self.phone_number = phone_number
    
    def print_info(self):
        print("First Name:", self.first_name)
        print("Last Name:", self.last_name)
        print("Birthdate:", self.birthdate)
        print("Phone Number:", self.phone_number)

class Employee(Person):
    def __init__(self, first_name, last_name, company, salary):
        super().__init__(first_name, last_name)
        self.company = company
        self.salary = salary
    
    def print_info(self):
        super().print_info()
        print("Company:", self.company)
        print("Salary:", self.salary)

person1 = Person("Alice", "Smith")
person1.set_birthdate("1990-05-12")
person1.set_phone_number("123-456-7890")

print("Person Info:")
person1.print_info()
print("--------------------")

# Create an Employee
employee1 = Employee("Bob", "Johnson", "TechCorp", 55000)
employee1.set_birthdate("1985-11-20")
employee1.set_phone_number("987-654-3210")

print("Employee Info:")
employee1.print_info()