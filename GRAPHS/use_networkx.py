import networkx as nx 

G = nx.Graph() 
G.add_edge("A", "B", weight=4)
G.add_edge("B", "C", weight=2)

print(G.nodes)
print(G.edges)