"""
n Python, map() is a tool that allows you to transform every item in an iterable (like a list) without using a manual for loop.

Think of it like a factory assembly line:

You have a raw material (your list of data).

You have a machine (your function/rule).

The map() function puts each piece of material through the machine and gives you a finished product.
"""

"""
1. The Basic SyntaxThe syntax looks like this:

$$map(function, iterable)

$$Function: The "rule" you want to apply.

Iterable: The list, tuple, or set you want to change.
"""

# For example 

# Old way 
nums = [1,2,3,4]
squared = []
for x in nums: 
    squared.append(x**2)



# Map way 
def square(n): 
    return n**2 

nums = [1,2,3,4,5]
result = map(square, nums)

# Convert the result back to a list to see it 
print(result) # <map object at 0x102be5300>
print(list(result))

