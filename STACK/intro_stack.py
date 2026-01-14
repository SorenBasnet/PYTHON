"""
A stack is a linear data structure that follows the LIFO (Last-In, First-Out) principle.

Core Concepts
There are two primary operations in a stack:

Push: Adding an element to the top of the stack.

Pop: Removing the topmost element from the stack.
"""

"""
1. Implementing a Stack using a List
The simplest way to create a stack in Python is by using the built-in list. Python’s append() and pop() methods make this very efficient.
"""

# Initialize an empty stack 
stack = []

# PUSH : Adding elements 
stack.append('A') # O(1)
stack.append('B')
stack.append('C')
stack.append('D')
print(f"Stack adter pushes : {stack}")


# POP : Removing the top element 
top_element = stack.pop() #O(1)
print(f"Popped element : {top_element}")
print(f"Stack after pop : {stack}")

# Peek : looking at the top element without removing it 
if stack: 
    print(f"Top elenent is {stack[-1]}")



"""
Key Takeaways for your NotesLIFO: Remember "Last-In, First-Out.

"Time Complexity: Both Push and Pop operations are $O(1)$, meaning they take constant time regardless of how big the stack is.

Common Uses:

Undo/Redo functionality in word processors.

Backtracking (like finding your way out of a maze).

Function Calls: The "Call Stack" manages how your program runs functions inside other functions.
"""

