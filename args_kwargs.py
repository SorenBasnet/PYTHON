"""
*args and **kwargs allow a function to accept a variable 
number of arguments. This means you don't have to define 
exactly how many inputs a user provides.
"""


"""
1. *args (Non-Keyword Arguments)
The * is the important part; args is just a naming 
convention (you could call it *numbers or *stuff).

When you use *args, Python takes all the extra "positional" 
arguments passed to the function and packs them into a Tuple.
"""

# Example: A "Sum Anything" Function If you don't know if 
# the user wants to add 2 numbers or 20 numbers:

def add_everything(*args):
    print(f"I received: {args}") # args is a tuple
    return sum(args)

print(add_everything(1, 2))        # Output: 3
print(add_everything(10, 5, 5, 20)) # Output: 40







"""
2. **kwargs (Keyword Arguments)
The ** (double star) allows you to pass a variable number of 
keyword arguments (named arguments). Python packs these into a Dictionary.
"""

#Example: A User Profile Function Imagine you want to store info about a user, 
# but some users have a "city" and others have a "twitter_handle."

def build_profile(name, **kwargs):
    print(f"Name: {name}")
    print(f"Extra Info: {kwargs}") # kwargs is a dictionary

build_profile("Alice", age=25, city="New York", job="Engineer")

# Output:
# Name: Alice
# Extra Info: {'age': 25, 'city': 'New York', 'job': 'Engineer'}


"""
3. Using them together
You can actually combine standard arguments, *args, and **kwargs in 
one function. They must follow this specific order:

- Standard arguments

- *args

- **kwargs
"""

def master_function(a, b, *args, **kwargs):
    print(f"Fixed: {a}, {b}")
    print(f"Extra Positional: {args}")
    print(f"Extra Named: {kwargs}")

master_function(1, 2, 3, 4, 5, color="Red", size="Large")


"""
*args,Single *,Tuple,When you want a list of items without specific names.
**kwargs,Double **,Dictionary,"When you want named ""key-value"" pairs as arguments.
"""


"""
Why use them?
You’ll see these everywhere in professional libraries (like Django or Pandas). 
\They allow developers to write functions that act as "wrappers"—passing whatever 
the user provides down to another function without needing to know exactly what 
those arguments are.
"""


