"""
@classmethod --> cls --> Methods that act on the whole class (e.g., creating objects).
"""

"""
2. @classmethod (The Factory Worker)
A class method knows about the Class itself, but not the individual object. Instead of self, it takes cls as the first argument.

When to use: Usually for "Factory Methods"—different ways to create an object. For example, creating a User from a string instead of separate arguments.

"""

class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_birth_year(cls, name, birth_year):
        # cls refers to the 'User' class
        age = 2024 - birth_year
        return cls(name, age) # This creates and returns a new User object

# Creating a user normally
u1 = User("Alice", 30)

# Creating a user using the class method "factory"
u2 = User.from_birth_year("Bob", 1994)