# BASE CLASS — every animal has a name, can eat and sleep
class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")


# Prey inherits from Animal, adds flee()
class Prey(Animal):
    def flee(self):
        print(f"{self.name} is fleeing")


# Predator inherits from Animal, adds hunt()
class Predator(Animal):
    def hunt(self):
        print(f"{self.name} is hunting")


# Rabbit is only a Prey — can flee, eat, sleep but cannot hunt
class Rabbit(Prey):
    pass


# Hawk is only a Predator — can hunt, eat, sleep but cannot flee
class Hawk(Predator):
    pass


# Fish inherits from BOTH Prey and Predator
# gets flee() + hunt() + eat() + sleep()
# MRO left to right: Fish -> Prey -> Predator -> Animal
class Fish(Prey, Predator):
    pass


rabbit = Rabbit("Bugs")
hawk = Hawk("Tony")
fish = Fish("Nemo")

rabbit.flee()       # Bugs is fleeing
rabbit.eat()        # Bugs is eating
rabbit.sleep()      # Bugs is sleeping
# rabbit.hunt()     # AttributeError — Rabbit has no hunt()

hawk.hunt()         # Tony is hunting
hawk.eat()          # Tony is eating
hawk.sleep()        # Tony is sleeping
# hawk.flee()       # AttributeError — Hawk has no flee()

fish.flee()         # Nemo is fleeing
fish.hunt()         # Nemo is hunting
fish.eat()          # Nemo is eating
fish.sleep()        # Nemo is sleeping

print(Fish.__mro__)
# (<class '__main__.Fish'>, <class '__main__.Prey'>, <class '__main__.Predator'>, <class '__main__.Animal'>, <class 'object'>)