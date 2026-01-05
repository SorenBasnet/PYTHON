"""
In Python, __repr__ is a special method (often called a "Dunder" method for Double Underscore) that defines how an object is represented as a string.

If you don’t define it, and you try to print your object, Python gives you a "memory address" which is usually useless for debugging.
"""



"""
1. The Problem: The "Ghost" Object
Imagine you have a Book class without __repr__:
"""

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

my_book = Book("The Hobbit", "J.R.R. Tolkien")
print(my_book) 
# Output: <__main__.Book object at 0x102715cd0>  <-- Not very helpful!

"""
2. The Solution: __repr__
The goal of __repr__ is to be unambiguous. It should ideally look like the code you would use to recreate that object.
"""

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __repr__(self):
        return f"Book(title='{self.title}', author='{self.author}')"

my_book = Book("The Hobbit", "J.R.R. Tolkien")
print(my_book)
# Output: Book(title='The Hobbit', author='J.R.R. Tolkien')



# -------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------

"""
3. __repr__ vs __str__
This is where most beginners get confused. Python actually has two ways to turn an object into a string:

__repr__ : Intended Audience -Developers	
Unambiguous; helpful for debugging/logging.

__str__ : Intended Audience -End Users	
Readable; pretty; "user-friendly."
"""


# Both in an example 

import datetime

today = datetime.datetime.now()

# __str__ is simple and readable
print(str(today))   # 2024-05-12 10:30:00

# __repr__ shows exactly how the object is built
print(repr(today))  # datetime.datetime(2024, 5, 12, 10, 30, 0, 123456)


"""
4. Why should you care?
Easier Debugging: When you have a list of 100 objects, seeing [Book(title='A'), Book(title='B')] is much better than seeing [<Book object at 0x1>, <Book object at 0x2>].

Interactive Shell: When you just type a variable name in a Python terminal (REPL) and hit Enter, Python calls __repr__.

The "Safety Net": If you define __repr__ but forget to define __str__, Python will use __repr__ for both. So, it's the most important one to implement!

Pro Tip for Noobs
If you use the @dataclass decorator we talked about earlier, Python writes the __repr__ for you automatically! It’s one of the biggest reasons people love dataclasses.

"""
