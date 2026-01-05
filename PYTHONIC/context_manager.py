"""
A Context Manager is a more elegant way to handle setup and teardown logic. The most 
common example is opening a file.

The Problem: Manual Cleanup
If you open a file manually, you must remember to close it. If your code crashes 
before it reaches file.close(), the file stays open in memory, which can lead 
to data corruption.
"""

f = open("data.txt", "w")
f.write("Hello!")
# If an error happens here, the file never closes!
f.close()

"""
The Solution: The with keyword
The with statement automatically handles the closing for you, even if an error 
occurs inside the block.

"""

with open("data.txt", "w") as f:
    f.write("Hello!")
# The file is automatically closed as soon as we indent back out.


"""
3. Creating Your Own Context Manager
You can turn any class into a context manager by defining two 
"magic methods": __enter__ and __exit__.

"""

class DatabaseConnection:
    def __enter__(self):
        print("Connecting to database...")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Closing database connection...")
        # This runs even if an error happened in the 'with' block

with DatabaseConnection() as db:
    print("Doing work with the database...")
    # (The connection closes automatically after this line)
