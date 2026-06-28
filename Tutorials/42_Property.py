# @property = lets you access a method like an attribute, no parentheses needed
# main benefit: you can add validation, formatting, or logic
#               when someone reads, writes, or deletes an attribute
# three parts: getter (@property), setter (@x.setter), deleter (@x.deleter)

# convention: _width means "private" — not enforced by Python but signals
# other developers should not access it directly from outside the class
# the @property acts as the controlled public interface for _width

class Rectangle:
    def __init__(self, width, height):
        # stored with underscore to mark as private/internal
        # actual validation happens in the setter, not here
        self._width = width
        self._height = height

    # GETTER — called when you READ the attribute: rectangle.width
    # formats the raw number into a readable string with 1 decimal place
    # without @property you would need rectangle.width() with parentheses
    @property
    def width(self):
        return f"{self._width:.1f}cm"

    @property
    def height(self):
        return f"{self._height:.1f}cm"

    # SETTER — called when you WRITE to the attribute: rectangle.width = 10
    # lets you validate the value before storing it
    # without a setter, the property is read-only and assignment throws AttributeError
    @width.setter
    def width(self, new_width):
        if new_width > 0:
            self._width = new_width
        else:
            print("Width must be greater than zero")

    @height.setter
    def height(self, new_height):
        if new_height > 0:
            self._height = new_height
        else:
            print("Height must be greater than zero")

    # DELETER — called when you use: del rectangle.width
    # lets you define cleanup logic when an attribute is removed
    @width.deleter
    def width(self):
        del self._width
        print("Width has been deleted")

    @height.deleter
    def height(self):
        del self._height
        print("Height has been deleted")

    @property
    def area(self):
        # read-only property — no setter defined, so rectangle.area = x would throw AttributeError
        # calculated on the fly from the raw _width and _height values, not the formatted strings
        return f"{self._width * self._height:.1f}cm²"


rectangle = Rectangle(3, 4)

# getter called here — looks like attribute access but runs the method
print(rectangle.width)     # 3.0cm
print(rectangle.height)    # 4.0cm
print(rectangle.area)      # 12.0cm²

# setter called here — looks like normal assignment but runs validation first
rectangle.width = 10
rectangle.height = 5
print(rectangle.width)     # 10.0cm
print(rectangle.height)    # 5.0cm
print(rectangle.area)      # 50.0cm²

# setter blocks invalid values
rectangle.width = -5       # Width must