"""

"""

try:
    # Code that might cause an error
    number = int(input("Enter a number: "))
    result = 10 / number
except ZeroDivisionError:
    # Runs ONLY if you divide by zero
    print("You can't divide by zero!")
except ValueError:
    # Runs ONLY if the input isn't a number
    print("That wasn't a valid number.")
else:
    # Runs ONLY if the 'try' block succeeded (no errors)
    print(f"Success! The result is {result}")
finally:
    # Runs NO MATTER WHAT (error or no error)
    print("Cleaning up resources...")


    