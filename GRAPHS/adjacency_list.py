"""
In Python, the most common way to represent a graph 
is using an Adjacency List, typically implemented 
with a dictionary where keys are nodes and values 
are lists of connected neighbors.
"""

"""
1. Building a Basic Graph
A graph consists of Vertices (nodes) and Edges (connections).
"""

class Graph: 

    def __init__(self): 
        # We use a dictionary to store the graph 
        self.graph = {}


    def add_vertex(self, vertex): 
        if vertex not in self.graph: 
            self.graph[vertex] = []

    def add_edge(self, v1, v2): 

        # For an undirected graph, add connection both ways 

        if v1 in self.graph and v2 in self.graph: 
            self.graph[v1].append(v2)
            self.graph[v2].append(v1)

    def remove_edge(self, v1, v2): 
        if v1 in self.graph and v2 in self.graph: 
            if v2 in self.graph[v1]: self.graph[v1].remove(v2)
            if v1 in self.graph[v2]: self.graph[v2].remove(v1)

    
    def remove_vertex(self, vertex): 
        if vertex in self.graph: 

            # First, remove this vertex from all its neighbor's lists
            for neighbor in self.graph[vertex]: 
                self.graph[neighbor].remove(vertex)

            # Then delete the vertex itseld 

            del self.graph[vertex]

    def display(self): 
        for vertex, neighbors in self.graph.items(): 
            print(f"{vertex}: {', '.join(map(str, neighbors))}")



my_graph = Graph() 
my_graph.add_vertex("A")
my_graph.add_vertex("B")
my_graph.add_vertex("C")
my_graph.add_edge("A", "B")
my_graph.add_edge("A", "C")

my_graph.display()






