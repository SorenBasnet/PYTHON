"""

A Generator is a special, simplified way to create an iterator. 
Instead of storing a whole list in memory, a generator "yields" 
items one by one on the fly.

Key Keyword: It uses yield instead of return.

Why use it? Memory efficiency. If you have a list of a billion numbers, 
your RAM might crash. A generator only calculates one number at a time, 
so it uses almost no memory.

"""

# Example 1
# --------------------------------------------------
def my_generator():
    yield "First"
    yield "Second"

gen = my_generator()
print(next(gen)) # Output: First

# Example 2
# --------------------------------------------------
def square_generator(limit):
    for i in range(limit):
        yield i * i  # 'yield' pauses the function and returns a value

# Create the generator object
my_squares = square_generator(5)

print(next(my_squares)) # 0
print(next(my_squares)) # 1
print(next(my_squares)) # 4

# You can also loop through the rest
for val in my_squares:
    print(val) # 9, 16

"""
Generators are functions that act like iterators but are much 
more memory-efficient. Instead of creating a list of 1 million 
items and keeping them in your RAM, a generator calculates each 
item only when you ask for it.
"""


"""
3. Real-World Use Case: Reading a Massive File
If you try to read a 10GB log file into a List (Iterable), your computer 
will likely crash because it tries to load the whole file into RAM.

If you use a Generator, you only load one line at a time.
"""
def read_huge_file(file_path):
    with open(file_path, "r") as file:
        for line in file:
            yield line.strip()

# This uses almost NO memory, even if the file is 100GB
log_gen = read_huge_file("massive_log.txt")

# We only pull the first 2 lines
print(next(log_gen))
print(next(log_gen))


"""
The "Golden Rule"
All Generators are Iterators.

All Iterators are Iterables.

Not all Iterables are Iterators (e.g., a List is an iterable, 
but it is not its own iterator).

"""


