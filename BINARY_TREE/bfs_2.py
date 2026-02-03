from collections import deque 

class Node: 

    def __init__(self, value): 
        self.val = value 
        self.left = None 
        self.right = None 


def bfs_traversal(root): 
    if not root: 
        return []
    

    results = []
    queue = deque([root]) # Initialize queue with the root 

    while queue: 
        # Remove the element from the front of the queue 
        current_node = queue.popleft()
        results.append(current_node.val)


        # Add left child to queue
        if current_node.left: 
            queue.append(current_node.left)


        # add right child to queue 
        if current_node.right: 
            queue.append(current_node.right)

    return results



# Example Usage:
#        1
#       / \
#      2   3
#     / \
#    4   5



root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print(f"BFS Result : {bfs_traversal(root)}")

# Output : [1,2,3,4,5]


