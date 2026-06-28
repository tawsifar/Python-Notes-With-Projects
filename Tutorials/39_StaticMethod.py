class Employee:

    def __init__(self, name, position):
        self.name = name
        self.position = position

    # instance method — needs self, works on this specific object's data
    def get_info(self):
        return f"{self.name} = {self.position}"

    # static method — no self, no access to any object or class data
    # just a utility function that logically belongs to Employee
    @staticmethod
    def is_valid_position(position):
        valid_positions = ["Manager", "Cashier", "Cook", "Janitor"]
        return position in valid_positions

    @staticmethod
    def is_valid_email(email):
        return "@" in email and "." in email

    @staticmethod
    def calculate_tax(salary):
        return salary * 0.2  # flat 20% tax


# calling static method directly on the class — no object needed
print(Employee.is_valid_position("Manager"))          # True
print(Employee.is_valid_position("Rocket Scientist")) # False
print(Employee.is_valid_email("bob@work.com"))        # True
print(Employee.is_valid_email("bobwork.com"))         # False
print(Employee.calculate_tax(50000))                  # 10000.0

# creating objects to show instance methods
emp1 = Employee("Bob", "Manager")
emp2 = Employee("Alice", "Cook")

print(emp1.get_info())   # Bob = Manager
print(emp2.get_info())   # Alice = Cook

# static method can also be called on an object, but its uncommon
# the result is exactly the same — object data is never touched
print(emp1.is_valid_position("Cashier"))  # True

# real world use — validate before creating the object
print("\n-- validate before creating employee --")
name = "Charlie"
position = "Pilot"

if Employee.is_valid_position(position):
    emp = Employee(name, position)
    print(emp.get_info())
else:
    print(f"{position} is not a valid position, employee not created")
# Pilot is not a valid position, employee not created