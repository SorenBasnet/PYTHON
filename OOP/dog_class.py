"""
1. Classes and Objects: The Blueprint
A Class is the blueprint (e.g., a "Car" design), and an Object is the actual instance (e.g., the specific red Tesla in your driveway).

__init__: The "constructor" method. It runs automatically when you create a new object.

self: A reference to the current instance of the class. It’s how the object accesses its own data.
"""

class Dog: 
    def __init__(self, name, breed):
        self.name = name # Attribute
        self.breed = breed # Attribute

    def bark(self): 
        return f"{self.name} says Woof!"
    
my_dog = Dog("Buddy", "Golden Retriever")
print(my_dog.bark())