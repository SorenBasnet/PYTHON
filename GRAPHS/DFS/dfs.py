"""
If a graph is like a maze, DFS is the strategy where you pick a path and just keep going until you hit a dead end. Once you hit that wall, you backtrack to the last place you saw a fork in the road and try the next path.
"""

"""
To keep track of where we’ve been and where we need to go back to, DFS usually uses a Stack (Last-In, First-Out). In Python, we usually implement this using Recursion (because Python handles the stack for us behind the scenes).
"""

"""
The "Rules" of DFS:
Visit a node.

Mark it as "visited" (so you don't walk in circles forever).

Check its neighbors.

Move to the first unvisited neighbor and repeat from Step 1.

If there are no unvisited neighbors, Backtrack.
"""

def dfs(graph, node, visited = None): 
    if visited is None: 
        visited = set() 

    #1. Mark the current node as visited 
    visited.add(node) 
    print(node, end=" ") # Print the path as we go 

    # 2. Look at all neighbors 
    for neighbor in graph[node]: 
        #3. If neighbor hasn't been visited, go deep into it 
        if neighbor not in visited: 
            dfs(graph, neighbor, visited)



graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

print("DFS Path:")
dfs(graph, 'A') 
# Likely Output: A B D E F C

"""
4. When should you use DFS?
DFS isn't always the best choice, but it shines in these specific spots:

Pathfinding: Finding if a path exists between two nodes.

Solving Mazes: It naturally explores one path to the end.

Topological Sorting: Useful for scheduling tasks (like "I must take Algebra before Calculus").

Detecting Cycles: Checking if a graph has a loop.
"""


