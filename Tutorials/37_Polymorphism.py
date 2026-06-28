from abc import ABC, abstractmethod

# ABC = Abstract Base Class
# any class that inherits from ABC can have abstract methods
# abstract method = a method that MUST be overridden by every child class
# if a child doesnt implement it, Python throws a TypeError on object creation

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass  # no body here, child classes are forced to write their own


# each child class inherits from Shape and MUST implement area()

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2  # π × r²


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2  # side × side


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return self.base * self.height * 0.5  # ½ × base × height


# Pizza inherits from Circle, not directly from Shape
# it doesnt write its own area() so it uses Circle's area()
# chain: Pizza -> Circle -> Shape
class Pizza(Circle):
    def __init__(self, topping, radius):
        super().__init__(radius)  # calls Circle's __init__ to set self.radius
        self.topping = topping


# what happens if you try to instantiate the abstract class directly?
# s = Shape()  -> TypeError: Can't instantiate abstract class Shape

# what if a child forgets to implement area()?
# class Hexagon(Shape):
#     pass
# h = Hexagon()  -> TypeError: Can't instantiate abstract class Hexagon
#                              without an implementation for abstract method 'area'


# polymorphism via inheritance
# every object here is a different type, but all share the same interface: area()
# the loop doesnt care what shape it is, it just calls area() and Python figures out the rest
shapes = [Circle(4), Square(5), Triangle(6, 7), Pizza("pepperoni", 15)]

print("-- polymorphism via inheritance --")
for shape in shapes:
    print(f"{shape.__class__.__name__}: {shape.area()}cm²")
# Circle: 50.24cm²
# Square: 25cm²
# Triangle: 21.0cm²
# Pizza: 706.5cm²     <- uses Circle's formula since Pizza never overrode area()


# polymorphism via duck typing
# Rectangle does NOT inherit from Shape at all
# but it has an area() method, so it works inside the same loop without any issues
# Python only checks: "does this object have area()?" — it doesnt care about the class tree
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height  # width × height


print("\n-- polymorphism via duck typing --")
duck_shapes = [Circle(3), Square(4), Rectangle(5, 6)]

for shape in duck_shapes:
    print(f"{shape.__class__.__name__}: {shape.area()}cm²")
# Circle: 28.26cm²
# Square: 16cm²
# Rectangle: 30cm²   <- not a Shape subclass, but still works because it has area()


# quick proof that Pizza is still a Shape despite being two levels deep
print("\n-- isinstance checks --")
pizza = Pizza("pepperoni", 15)
print(isinstance(pizza, Pizza))    # True
print(isinstance(pizza, Circle))   # True  <- Pizza inherits from Circle
print(isinstance(pizza, Shape))    # True  <- Circle inherits from Shape
print(isinstance(pizza, Square))   # False <- no relation to Square