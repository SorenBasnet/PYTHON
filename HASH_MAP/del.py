# Imagine this is your graph or maybe a dictionary 

graph = {
    "A": ["B", "C"], 
    "B": ["A"], 
    "C": ["A"]
}

# If we run: 
del graph["B"] 

print(graph)