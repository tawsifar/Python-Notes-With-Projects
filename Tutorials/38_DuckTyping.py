# Duck Typing = object doesnt need to be from a specific class
# it just needs to have the required method or attribute
# Python never asks "what are you?" — it only asks "can you do this?"

class Animal:
    alive = True  # class variable, shared across all Animal instances

class Dog(Animal):
    def speak(self):
        print("WOOF!")

class Cat(Animal):
    def speak(self):
        print("MEOW!")

# Car has zero relation to Animal — doesnt inherit from it at all
# but it has speak() and alive, so Python treats it the same in the loop
class Car:
    alive = True

    def speak(self):
        print("HONK!")


# Duck typing in action
# Python doesnt verify that Car is an Animal
# it just calls speak() and reads alive — both exist, so no error
animals = [Dog(), Cat(), Car()]

for animal in animals:
    animal.speak()
    print(animal.alive)
# WOOF!
# True
# MEOW!
# True
# HONK!   <- Car, not an Animal, but has speak() so it works
# True    <- Car has alive too, so this works as well


# what if an object is missing the required method?
class Stone:
    alive = False
    # no speak() method

mixed = [Dog(), Cat(), Stone()]

print("\n-- missing method example --")
for animal in mixed:
    if hasattr(animal, "speak"):   # hasattr() checks if the attribute/method exists before calling
        animal.speak() #--------------------------------Till this part is enough for basics-------------------------------------------------------------------------------------
    else:
        print(f"{animal.__class__.__name__} has no speak() method, skipping")
# WOOF!
# MEOW!
# Stone has no speak() method, skipping


# without hasattr(), Python crashes the moment it hits Stone
# uncomment to see the error:
# for animal in [Dog(), Stone()]:
#     animal.speak()  -> AttributeError: 'Stone' object has no attribute 'speak'
# Python doesnt catch this ahead of time , it only fails when it actually hits that line
# this is duck typings weakness vs inheritance + abstract methods


# isinstance() check : proves Car is NOT an Animal
print("\n-- isinstance checks --")
dog = Dog()
car = Car()

print(isinstance(dog, Animal))   # True  <- Dog inherits from Animal
print(isinstance(car, Animal))   # False <- Car has nothing to do with Animal
print(isinstance(car, object))   # True  <- everything in Python is an object

# but despite isinstance returning False for Car,
# it still ran perfectly inside the loop above — thats duck typing


# duck typing vs inheritance side by side
# inheritance: Car would need to extend Animal to be in the loop safely
# duck typing:  Car just needs speak() and alive — class tree doesnt matter

print("\n-- duck typing vs inheritance --")

class Robot:        # again, no inheritance
    alive = False   # robots arent alive

    def speak(self):
        print("BEEP BOOP!")

everyone = [Dog(), Cat(), Car(), Robot()]

for thing in everyone:
    thing.speak()
    print(f"alive: {thing.alive}")
# WOOF!        alive: True
# MEOW!        alive: True
# HONK!        alive: True
# BEEP BOOP!   alive: False  <- Robot works fine, alive is just False