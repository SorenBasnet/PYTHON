from collections import deque 

class Node: 

    def __init__(self, value): 
        self.value = value 
        self.left = None 
        self.right = None 


def bfs_traversal(root): 

    if not root: 
        return []
    

    results = []
    queue = deque([root])


    while queue: 

        level_size = len(queue) # How many nodes are in each level 
        current_level_nodes = []

        for _ in range(level_size): 
            node = queue.popleft() 
            current_level_nodes.append(node.value)

            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)


        results.append(current_level_nodes)



    return results 


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print(f"BFS Result : {bfs_traversal(root)}")
# BFS Result : [[1], [2, 3], [4, 5]]