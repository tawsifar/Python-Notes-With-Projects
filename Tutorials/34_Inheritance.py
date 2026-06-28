# Parent class
class Animal:

    def __init__(self, name):
        self.name = name
        self.is_alive = True

    # Common behavior
    def eat(self):
        print(f"{self.name} is eating")

    # Common behavior
    def sleep(self):
        print(f"{self.name} is sleeping")


# Child class
class Dog(Animal):

    # Dog specific behavior
    def speak(self):
        print("WOOF!")


class Cat(Animal):

    # Cat specific behavior
    def speak(self):
        print("MEOW!")


class Mouse(Animal):

    # Mouse specific behavior
    def speak(self):
        print("SQUEEK!")


# Creating Objects
dog = Dog("Scooby")
cat = Cat("Garfield")
mouse = Mouse("Mickey")


dog.eat()      # Inherited method
dog.sleep()    # Inherited method
dog.speak()    # Child method


