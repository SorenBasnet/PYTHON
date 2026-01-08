"""
Improved BST search     
"""

class Node: 

    def __init__(self, key): 
        self.val = key 
        self.left = None
        self.right = None 

class BST: 

    def __init__(self): 
        self.root = None 

    def insert(self, key): 
        if self.root is None: 
            self.root = Node(key)
        else: 
            self._insert_recursive(self.root, key)

    
    def _insert_recursive(self, node, key): 
        if key < node.val: 
            if node.left is None: 
                node.left = Node(key)
            else: 
                self._insert_recursive(node.left, key)

        else: 
            if node.right is None: 
                node.right = Node(key)
            else: 
                self._insert_recursive(node.right, key)

    
    def exists(self, key): 
        """Return True is key is found, False otherwise."""

        return self._search_recursive(self.root, key)
    
    def _search_recursive(self, node, key): 

        #1. Base case: we hit the end of a branch without finding it 
        if node is None: 
            return False 
        
        #2. base case: we found the key 
        if node.val == key: 
            return True 
        
        #3. Recursive steps: 

        if key < node.val: 
            return self._search_recursive(node.left, key)
        
        else: 
            return self._search_recursive(node.right, key)
        


# --- Usage --- 

tree = BST() 
for val in [5,3,7,2,4]: 
    tree.insert(val)

print(tree.exists(4)) 
print(tree.exists(99))