from collections import deque 

def levelOrder(root): 
    if not root: 
        return []
    
    result = []

    q = deque([root])

    while q: 
        node = q.popleft()
        result.append(node.val)

        if node.left: 
            q.append(node.left) 

        if node.right: 
            q.append(node.right)

    return result

