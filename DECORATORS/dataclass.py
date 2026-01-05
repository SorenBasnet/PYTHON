"""
3. @dataclass (The Shortcut)
This is a game-changer for "noobs" and pros alike. Normally, writing a class that just holds data is tedious because you have to write __init__, __repr__ (for pretty printing), and comparison logic yourself.

@dataclass writes all that boring code for you automatically.
"""

# Old way
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __repr__(self):
        return f"Point(x={self.x}, y={self.y})"
    

# New way 
from dataclasses import dataclass

@dataclass
class Point:
    x: int
    y: int

p = Point(10, 20)
print(p)  # Automatically prints: Point(x=10, y=20)