#Types of Inheritance
#SINGLE INHERITANCE
# Single Inheritance Example
# Single Inheritance Example with __init__

# Single Inheritance Example with __init__ and self

class Animal:
    def __init__(self, name):
        self.name = name
        print(f"Animal '{self.name}' created")

    def eat(self):
        print(f"{self.name} eats food.")

class Dog(Animal):  # Dog inherits from Animal
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed
        print(f"Dog of breed '{self.breed}' created")

    def bark(self):
        print(f"{self.name} the {self.breed} barks.")

# Object Creation
d = Dog("Tommy", "Labrador")
d.eat()
d.bark()




#MULTILEVEL INHERITANCE
# Multilevel Inheritance Example with __init__ and self

class Animal:
    def __init__(self, name):
        self.name = name
        print(f"Animal '{self.name}' created")

    def eat(self):
        print(f"{self.name} eats food.")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed
        print(f"Dog of breed '{self.breed}' created")

    def bark(self):
        print(f"{self.name} the {self.breed} barks.")

class Puppy(Dog):
    def __init__(self, name, breed, age):
        super().__init__(name, breed)
        self.age = age
        print(f"Puppy aged {self.age} months created")

    def weep(self):
        print(f"{self.name} the puppy weeps.")

# Object Creation
p = Puppy("Bruno", "Beagle", 6)
p.eat()
p.bark()
p.weep()


#MULTIPLE INHERITANCE
# Multiple Inheritance Example with __init__ and self

class Animal:
    def __init__(self, name):
        self.name = name
        print(f"Animal '{self.name}' created")

    def eat(self):
        print(f"{self.name} eats food.")

class Pet:
    def __init__(self, owner):
        self.owner = owner
        print(f"Pet owned by '{self.owner}' created")

    def play(self):
        print(f"Pet plays with {self.owner}.")

class Parrot(Animal, Pet):  # Multiple Inheritance
    def __init__(self, name, owner):
        Animal.__init__(self, name)  # explicitly call Animal's init
        Pet.__init__(self, owner)    # explicitly call Pet's init
        print(f"Parrot '{self.name}' created")

    def speak(self):
        print(f"{self.name} says hello to {self.owner}!")

# Object Creation
par = Parrot("Mithu", "Alice")
par.eat()
par.play()
par.speak()




#HIERARCHIAL INHERITANCE
# Hierarchical Inheritance Example with __init__ and self

class Animal:
    def __init__(self, name):
        self.name = name
        print(f"Animal '{self.name}' created")

    def eat(self):
        print(f"{self.name} eats food.")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed
        print(f"Dog of breed '{self.breed}' created")

    def bark(self):
        print(f"{self.name} the {self.breed} barks.")

class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color
        print(f"Cat with color '{self.color}' created")

    def meow(self):
        print(f"{self.name} the {self.color} cat meows.")

# Object Creation
d = Dog("Max", "German Shepherd")
d.eat()
d.bark()

c = Cat("Kitty", "White")
c.eat()
c.meow()






#HYBRID INHERITANCE
