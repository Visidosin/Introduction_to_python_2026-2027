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