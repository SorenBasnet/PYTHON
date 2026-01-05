"""
This works exactly like list comprehensions, but you define a 
key and a value using curly braces {}.

The Syntax: {key_expression: value_expression for item in iterable}
"""


"""
Example: Creating a Price Map
Imagine you have a list of items and you want to create a 
dictionary where the item is the key and its length is the value.
"""

# Old way : 
fruits = ["apple", "mango", "banana"]

# 1. Initialize an empty dictionary
fruit_lengths = {}

# 2. Loop through the list
for f in fruits:
    # 3. Assign the fruit name as the key and its length as the value
    fruit_lengths[f] = len(f)

print(fruit_lengths)
# Output: {'apple': 5, 'mango': 5, 'banana': 6}



# New way 
fruits = ["apple", "mango", "banana"]

# Dictionary Comprehension
fruit_lengths = {f: len(f) for f in fruits}

print(fruit_lengths)
# Output: {'apple': 5, 'mango': 5, 'banana': 6}


"""
3. Bonus: Generator Expressions
Since we just talked about Generators, you should know they 
have their own comprehension-style syntax too!

If you use parentheses () instead of brackets [], you aren't 
creating a list; you are creating a Generator Object. This is 
the ultimate memory-saver.
"""

# List comprehension (Uses memory for all 1 million items)
big_list = [i for i in range(1000000)] 

# Generator expression (Uses almost NO memory)
big_gen = (i for i in range(1000000)) 

print(next(big_gen)) # 0
print(next(big_gen)) # 1

# Generator Expression : you only need to loop once 



"""
Why the Dictionary Comprehension is often preferred:
Atomicity: The dictionary is created in one single step rather than 
being created empty and then modified.

Performance: Comprehensions are usually slightly faster in Python because 
the construction happens at the C-level inside the interpreter.

Readability: Once you are comfortable with the syntax, it's easier to see 
exactly what the dictionary contains without tracing the "steps" of a loop.
"""


