"""
The Key Difference: The Node
The Node now has three parts instead of two:

Data

Next (Pointer to the next node)

Prev (Pointer to the previous node)
"""


"""
The Trade-offs (The Cons)
Memory: Every node now has to store an extra pointer (prev). This adds up if you have millions of nodes.

Complexity: When you insert or delete a node, you have to update four pointers instead of two to make sure the "forward" and "backward" links stay intact.
"""




