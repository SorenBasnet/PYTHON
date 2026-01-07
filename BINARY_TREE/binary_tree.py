class TreeNode: 
    def __init__(self, val=0, left=None, right=None): 
        self.val = val 
        self.left = left 
        self.right = right



# How to initiate this 

root = TreeNode(12)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.left = TreeNode(5)


    