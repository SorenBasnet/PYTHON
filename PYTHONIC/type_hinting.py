"""
1. The Basics: Variables and Functions
You can annotate simple variables and function parameters using a colon : and the return value using ->.
"""

# Variable hinting
name: str = "Alice"
age: int = 30
is_student: bool = False

# Function hinting
def greet(name: str) -> str:
    return f"Hello, {name}"


"""
2. Hinting Collections (Lists, Dicts, Sets)
When you have a list, you don't just want to say it's a list; you want to say what is inside the list.

Modern Python (3.9+): You can use the built-in types directly.

Older Python: You had to import List, Dict, etc., from the typing module.
"""

# A list of strings
users: list[str] = ["Alice", "Bob", "Charlie"]

# A dictionary with string keys and integer values
scores: dict[str, int] = {"Alice": 10, "Bob": 15}

# A tuple with specific fixed elements
coordinates: tuple[float, float] = (40.7128, 74.0060)



"""
. Advanced Hints from the typing Module
As your code gets complex, you'll need the "special powers" found in the typing module.

A. Union and Optional
Sometimes a variable can be more than one type.

Union: Can be Type A OR Type B. (In Python 3.10+, you can use the pipe | operator instead).

Optional: A shortcut for "This type OR None."
"""

from typing import Union, Optional

# New way (3.10+)
def get_id(id_val: int | str):
    print(f"ID is {id_val}")

# Optional (If a user might not have a middle name)
def print_name(first: str, middle: str | None = None):
    print(first, middle)


"""
B. Any
If you truly don't know what a variable will be, or it could be anything, use Any. Use this sparingly!
"""

from typing import Any

def log_anything(data: Any):
    print(data)


"""
C. Callable
When you are using those Higher-Order Functions we talked about, you need to hint that a parameter is a function.
"""

from typing import Callable

# A function that takes two ints and returns an int
def operate(a: int, b: int, func: Callable[[int, int], int]) -> int:
    return func(a, b)


"""
4. Hinting Classes (Self-Referencing)
If a method in a class needs to return an instance of that same class, you might run into trouble because the class isn't "finished" yet. Use strings or from __future__ import annotations.
"""

class Position:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def copy(self) -> "Position":
        return Position(self.x, self.y)
    


"""
6. Type Aliases
If you have a very complex type that you use everywhere, you can give it a nickname.
"""

# Define a nickname for a complex type
CoordinateList = list[tuple[float, float]]

def move_player(locations: CoordinateList):
    for x, y in locations:
        print(f"Moving to {x}, {y}")

        