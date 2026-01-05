"""
1. @staticmethod (The Independent Helper)
A static method is just a regular function that happens to live inside a class because it's conceptually related. It does not know anything about the class or the specific object (it doesn't use self or cls).

When to use: When you have a "utility" function (like a math calculation) that belongs with the class but doesn't need to change any data inside it.
"""

class Calculator:
    @staticmethod
    def add(a, b):
        return a + b

# You don't even need to create a "Calculator" object to use it!
print(Calculator.add(5, 10))
