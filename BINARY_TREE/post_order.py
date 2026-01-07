# left right root 

class TreeNode: 

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left 
        self.right = right 

    def postorderTraversal(self, root): 
        if not root: 
            return []
        return self.postorderTraversal[root.left] + self.postorderTraversal[root.right] + self.postorderTraversal[root.val]

