# class variables = Shared among all instances of a class
# Defined outside the constructor
# Allow you to share data among all objects created from that class



class Dog:
    species = "Canis lupus"  # class variable — shared by all dogs
    count = 0

    def __init__(self, name):
        self.name = name      # instance variable — unique to each dog

d1 = Dog("Rex")
d2 = Dog("Bruno")

# 3 ways to access
print(d1.species)   # Canis lupus
print(d2.species)   # Canis lupus
print(Dog.species)  # Canis lupus


print(d1.name)      # Rex
print(d2.name)      # Bruno



# Modify via class : affects ALL instances
Dog.count = 5
print(d1.count)  # 5
print(d2.count)  # 5

# Modify via instance : creates a NEW instance variable, doesn't touch the class variable
d1.species = "changed"
print(d1.species)  # changed  ← now d1 has its OWN species
print(d2.species)  # Canis lupus  ← d2 still uses class variable
print(Dog.species) # Canis lupus  ← class variable untouched



#anither practical example of class variables
class Student:
    class_year = 2025
    num_students = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.num_students += 1 # every time a new student is created, the class variable num_students increases by 1

student1 = Student("Spongebob", 30)
student2 = Student("Patrick", 35)
student3 = Student("Squidward", 55)
student4 = Student("Sandy", 27)

print(f"My graduating class of {Student.class_year} has {Student.num_students} students")








