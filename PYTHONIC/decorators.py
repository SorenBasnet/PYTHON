"""
A Decorator is a function that takes another function and extends 
its behavior without permanently modifying it. Think of it like adding 
"sprinkles" to a cupcake—the cupcake is still a cupcake, but now it has 
something extra.

How They Work (The Mechanics)
In Python, functions are "first-class objects," meaning they can be 
passed around as arguments just like strings or integers. A decorator leverages this by:

Taking a function (let’s call it original_func) as input.

Defining a "wrapper" function inside itself.

Executing the original_func inside that wrapper, along with any extra code.

Returning the wrapper function.
"""


# Manual way 
def my_logger(func):
    def wrapper(*args, **kwargs):
        print(f"Logging: {func.__name__} is starting...")
        return func(*args, **kwargs)
    return wrapper

def say_hello(name):
    print(f"Hello, {name}!")

# --- THE OLD WAY ---
# We manually overwrite 'say_hello' with the wrapped version
say_hello = my_logger(say_hello)

# Now when we call it, it uses the decorated version
say_hello("Alice")



# Decorator 
def my_logger(func):
    def wrapper(*args, **kwargs):
        print(f"--- Log: Running '{func.__name__}' ---")
        result = func(*args, **kwargs)
        print(f"--- Log: Finished '{func.__name__}' ---")
        return result
    return wrapper

# Using the @ symbol is the 'syntactic sugar' for decorators
@my_logger
def say_hello(name):
    print(f"Hello, {name}!")

# When we call the function, the decorator logic runs automatically
say_hello("Alice")


#--- Log: Running 'say_hello' ---
#Hello, Alice!
#--- Log: Finished 'say_hello' ---
