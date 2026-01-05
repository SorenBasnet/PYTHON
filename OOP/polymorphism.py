"""
C. Polymorphism (Many Forms)
Polymorphism allows different classes to be treated as instances of the same class through the same interface. Most commonly, it means different classes can have methods with the same name.
"""

# Look at dog_class, inheritance first

animals = [Dog("Buddy", "Lab"), Cat()]
for animal in animals:
    animal.speak() # Both have a speak() method, but behave differently