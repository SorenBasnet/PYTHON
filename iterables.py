"""

1. The Iterable (The "Book")
An Iterable is any object that can return its members one at a time.
It’s like a book: it contains all the information, and you can go 
through it, but it doesn't remember where you left off by itself.

Examples: Lists, Tuples, Strings, and Dictionaries.

Key Characteristic: If you can use it in a for loop, it’s an iterable.

Behind the scenes: It implements the __iter__() method.

2. The Iterator (The "Bookmark")
An Iterator is the object that actually does the work of "traversing" 
the iterable. It’s like a bookmark: it knows exactly where you are and 
what comes next.

How to get one: You create an iterator by passing an iterable to the 
iter() function.

Key Characteristic: It remembers its state (position). Once you consume 
an item using the next() function, it’s gone. You cannot "reset" an 
iterator; once you reach the end, it raises a StopIteration error.

Behind the scenes: It implements the __next__() method.

"""

# Example 1
# --------------------------------------------------
my_list = [1, 2]          # Iterable
my_iterator = iter(my_list) # Iterator

print(next(my_iterator)) # Output: 1
print(next(my_iterator)) # Output: 2
# print(next(my_iterator)) # This would raise StopIteration


# Example 2
# --------------------------------------------------
# --- THE ITERABLE (The Playlist) ---
songs = ["Bohemian Rhapsody", "Stairway to Heaven", "Imagine"]

# --- THE ITERATOR (The Music Player) ---
# We use iter() to get the iterator from the iterable
player = iter(songs)

print(next(player))  # Output: Bohemian Rhapsody
print(next(player))  # Output: Stairway to Heaven

# The iterator remembers where it is. 
# If we use a for loop now, it starts from where we left off:
for song in player:
    print(f"Playing remaining: {song}") # Output: Playing remaining: Imagine



"""
The "Golden Rule"
All Generators are Iterators.

All Iterators are Iterables.

Not all Iterables are Iterators 
(e.g., a List is an iterable, but it is not its own iterator).
"""