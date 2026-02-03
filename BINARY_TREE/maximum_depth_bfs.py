from collections import deque 

class Node: 
    def __init__(self, value): 
        self.value = value 
        self.left = None
        self.right = None



def max_depth_bfs(root): 

    