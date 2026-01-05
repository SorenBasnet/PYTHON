"""
2. The Four Pillars of OOP
A. Inheritance (The "is-a" Relationship)
Inheritance allows a "Child" class to take on the attributes and methods of a "Parent" class. This promotes code reuse.

Syntax: class Child(Parent):

super(): Used to call a method from the parent class (usually the constructor).
"""

class Animal: 
    def speak(self): 
        print("Animal makes a sound")

class Cat(Animal): 
    def speak(self): 
        super().speak() # Optional : calls the parent's version
        print("Meow")