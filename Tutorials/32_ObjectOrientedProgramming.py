# object = a bundle of related attributes (variables) and methods (functions)
# class  = a blueprint used to design the structure and layout of an object
# example real world objects: phone, cup, book, car
# you define a class once, then create as many objects from it as you need

# to use this class from another file:
# from MyOOP import Car


class Car:
    # __init__ is a special method that runs automatically when an object is created
    # self refers to the specific instance calling the method
    # every method in a class must have self as the first parameter
    def __init__(self, model, year, color, for_sale):
        self.model    = model       # instance attribute - unique to each object
        self.year     = year
        self.color    = color
        self.for_sale = for_sale

    def drive(self):
        print(f"You drive the {self.color} {self.model}")

    def stop(self):
        print(f"You stop the {self.color} {self.model}")

    def describe(self):
        print(f"{self.year} {self.color} {self.model}")

    def sell(self):
        if self.for_sale:
            print(f"The {self.model} is available for sale")
        else:
            print(f"The {self.model} is not for sale")


# creating objects (instances) from the Car class
car1 = Car("Mustang", 2024, "red",    False)
car2 = Car("Corvette", 2025, "blue",  True)
car3 = Car("Charger",  2026, "yellow", True)

# calling methods
car2.drive()     # You drive the blue Corvette
car2.stop()      # You stop the blue Corvette
car3.describe()  # 2026 yellow Charger
car1.sell()      # The Mustang is not for sale
car2.sell()      # The Corvette is available for sale

# accessing attributes directly
print(car2.model)     # Corvette
print(car3.year)      # 2026
print(car1.color)     # red
print(car1.for_sale)  # False

# modifying attributes after creation
car1.color = "green"
print(car1.color)     # green

# every object is independent - changing car1 doesnt affect car2
car1.year = 2020
print(car1.year)   # 2020
print(car2.year)   # 2025 - unchanged