"""
In Python development, "utility programs" (often consolidated 
into a utils.py or helpers.py file) serve as the "toolbox" of your 
project. They house reusable, generic code that doesn't strictly belong 
to your main business logic but is necessary for the app to function.

Think of them as the Swiss Army Knife of your codebase.

1. Why use them?
As a project grows, you’ll find yourself performing the same small tasks 
repeatedly—formatting dates, cleaning strings, or connecting to a database.

Instead of rewriting that code in every file (which violates the 
DRY principle: Don't Repeat Yourself), you tuck those functions into a 
helper file. This makes your main logic much cleaner and easier to read.

2. Common Categories of Helpers
A typical helpers.py might contain:

Data Formatting: Converting "2024-05-12" into "May 12th, 2024."

Validation: Checking if an email address is valid or if a password meets 
security requirements.

File I/O: Simple functions to read a JSON file or create a folder if it 
doesn’t exist.

Wrappers: Adding logging or timing decorators to other functions.
"""

import datetime 
import re 

def slugify(text): 
    """Converts 'Hello World' to hello-world' for URLs."""
    return re.sub(r'\W+', '-', text.lower()).strip('-')

def get_current_timestamp():
    """Returns a formatted string of the current time."""
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


"""
5. The "Golden Rule" of Utils
The most important thing to remember is that utility functions should be 
"pure" whenever possible. This means:

They should take an input and return an output.

They shouldn't rely on "global" variables from your main program.

They should be "context-agnostic" (they don't care if they are being used 
in a web app, a data script, or a bot).

"""