"""
1. List Comprehensions
Instead of creating an empty list and using .append(), you can 
do everything in one line.

The Syntax: [expression for item in iterable if condition]
"""



"""
Example: Squaring Numbers
Suppose we want to take a list of numbers and create a new 
list containing only the squares of the even numbers.
"""

# The "Old" Way (Loop):
nums = [1, 2, 3, 4, 5]
squares = []
for n in nums:
    if n % 2 == 0:
        squares.append(n * n)
# Result: [4, 16]


# The Comprehension Way:
nums = [1, 2, 3, 4, 5]
squares = [n * n for n in nums if n % 2 == 0]
# Result: [4, 16]