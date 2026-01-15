"""
What is a Linked List?
A Linked List is a linear data structure where elements are not stored in adjacent memory locations (unlike an array). Instead, each element is a separate object called a Node.
+1

Each Node contains two parts:

Data: The actual value you want to store (like a number or string).

Next: A pointer (or reference) to the next node in the sequence.

The list starts with a pointer to the first node, called the Head. The last node points to Null, signaling the end of the list.
"""

"""
When Should You Use a Linked List?
Linked Lists aren't always better than arrays; they are specialized tools. Here is when they shine:

1. Frequent Insertions and Deletions
In an array, if you want to add an item to the beginning, you have to shift every other item over one spot. In a Linked List, you just change where the pointers point. It’s much faster.

2. Unknown Size
If you don't know how many items you'll need to store, a Linked List is great because it grows dynamically. You don't have to "resize" it like you do with a dynamic array.

3. Implementing Other Data Structures
Linked Lists are the "building blocks" for more complex structures like Stacks and Queues.
"""

"""
Common Types of Linked Lists
Singly Linked List: Each node points only to the next node (one-way street).

Doubly Linked List: Each node points to both the next node and the previous node (two-way street). This makes it easier to move backward.

Circular Linked List: The last node points back to the Head instead of Null, forming a loop.
"""

