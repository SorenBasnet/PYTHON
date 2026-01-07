# left root right

class TreeNode: 
    def __init__(self, val=0, left=None, right=None): 
        self.val = val 
        self.left = left
        self.right = left 

    
    def inorderTraversal(self, root): # left root right
        if not root: 
            return []
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)
    
