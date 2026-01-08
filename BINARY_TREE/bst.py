""" 
A Binary Search Tree (BST) is a specific type of binary tree that 
maintains a strict order. This order allows for very fast searching, 
adding, and deleting of data.


The BST Rule

For every node in the tree:

All values in the left subtree are smaller than the node's value.

All values in the right subtree are greater than the node's value.

"""


class Node: 

    def __init__(self, key): 
        self.left = None 
        self.right = None 
        self.val = key 


def insert(root, key): 

    # if the tree is empty, return a new node 
    if root is None: 
        return Node(key)
    
    # Otherwise, revur down the tree 

    if key < root.val: 
        root.left = insert(root.left, key)

    else: 
        root.right = insert(root.right, key)
    return root 


def search(root, key): 

    # base cases : we hit the end of the branch without finding it 

    if root is None : 
        return False 
    
    #2. Base case: we found the key 

    if root.val == key: 
        return True 
    
    #3. Recursive steps 

    if key < root.val:
        return search(root.left, key)

    else: 
        return search(root.right, key) 
    

def inorder_traversal(root): 
    if root: 
        inorder_traversal(root.left)
        print(root.val, end = " ")
        inorder_traversal(root.right)


# ---- Example Usage 

root = None 
keys = [50, 30, 20, 40, 70, 60, 80]

for k in keys: 
    root = insert(root, k)

print("In order Traversal (Sorted) : ")
inorder_traversal(root)

print()
print(search(root, 100))

    
