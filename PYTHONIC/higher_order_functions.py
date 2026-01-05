"""
In Python, functions are "First-Class Citizens." This means you can treat a function just like a variable: you can pass it to another function, return it from a function, or store it in a list.

A Higher-Order Function is simply any function that does at least one of these two things:

Takes another function as an argument.

Returns a function as its result.
"""


"""
1. Taking a Function as an Argument
Imagine you have a list of prices and you want to apply different "strategies" to them (like a tax or a discount). Instead of writing ten different loops, you write one loop that accepts a "strategy function."
"""

def apply_action(prices, action_func):
    """This is a Higher-Order Function."""
    return [action_func(p) for p in prices]

def add_tax(price):
    return price * 1.10

def half_off(price):
    return price * 0.5

items = [100, 200, 300]

# We pass 'add_tax' or 'half_off' as if they were variables!
taxed_items = apply_action(items, add_tax)
sale_items = apply_action(items, half_off)

print(taxed_items) # [110.0, 220.0, 330.0]

"""
2. Returning a Function (Closures)
Sometimes you want a function to "manufacture" another function for you. This is how decorators are built behind the scenes.
"""

def make_multiplier(n):
    """This Higher-Order Function returns a new function."""
    def multiplier(x):
        return x * n
    return multiplier

# Create a 'double' function
double = make_multiplier(2)
# Create a 'triple' function
triple = make_multiplier(3)

print(double(10)) # 20
print(triple(10)) # 30

"""
3. Built-in HOFs you’ll see everywhere
Python has several built-in Higher-Order Functions that help you avoid writing for loops.

HOF,Purpose
map(),Applies a function to every item in a list.
filter(),Keeps only items that return True when passed into a function.
sorted(),Can take a key argument (a function) to decide how to sort objects.
"""

# Example using sorted() with a HOF approach:

names = ["Alice", "Bob", "Christopher", "Dan"]

# Sort by the length of the name (using the 'len' function as an argument)
longest_first = sorted(names, key=len, reverse=True)
print(longest_first) # ['Christopher', 'Alice', 'Dan', 'Bob']
