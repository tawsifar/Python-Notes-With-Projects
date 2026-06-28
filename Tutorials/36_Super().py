# Parent class — holds attributes common to all shapes
class Shape:
    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled

    def describe(self):
        # ternary expression: if is_filled is True prints "filled", else "not filled"
        print(f"It is {self.color} and {'filled' if self.is_filled else 'not filled'}")


# Circle inherits from Shape, adds its own attribute: radius
class Circle(Shape):
    def __init__(self, color, is_filled, radius):
        super().__init__(color, is_filled)  # calls Shape's __init__ to set color and is_filled
        self.radius = radius

    # overrides Shape's describe() but still calls it at the end via super()
    def describe(self):
        print(f"It is a circle with an area of {3.14 * self.radius * self.radius}cm^2")
        super().describe()  # runs Shape's describe() after Circle's own line


# Square inherits from Shape, adds its own attribute: width
class Square(Shape):
    def __init__(self, color, is_filled, width):
        super().__init__(color, is_filled)
        self.width = width

    def describe(self):
        print(f"It is a square with an area of {self.width * self.width}cm^2")
        super().describe()


# Triangle inherits from Shape, adds its own attributes: width and height
class Triangle(Shape):
    def __init__(self, color, is_filled, width, height):
        super().__init__(color, is_filled)
        self.width = width
        self.height = height

    def describe(self):
        print(f"It is a triangle with an area of {self.width * self.height / 2}cm^2")
        super().describe()


# keyword arguments used here — order doesnt matter when you name them
circle   = Circle(color="red", is_filled=True, radius=5)
square   = Square(color="blue", is_filled=False, width=6)
triangle = Triangle(color="yellow", is_filled=True, width=7, height=8)

circle.describe()
# It is a circle with an area of 78.5cm^2
# It is red and filled

square.describe()
# It is a square with an area of 36cm^2
# It is blue and not filled

triangle.describe()
# It is a triangle with an area of 28.0cm^2
# It is yellow and filled 