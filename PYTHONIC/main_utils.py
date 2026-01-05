"""
Made this file to show how to run functions mentions in 
utils
"""

from utils import slugify

title = "My First Blog Post!"
url_path = slugify(title) # output: my-first-blog-post


"""
5. The "Golden Rule" of Utils
The most important thing to remember is that utility functions should be 
"pure" whenever possible. This means:

They should take an input and return an output.

They shouldn't rely on "global" variables from your main program.

They should be "context-agnostic" (they don't care if they are being used 
in a web app, a data script, or a bot).

"""