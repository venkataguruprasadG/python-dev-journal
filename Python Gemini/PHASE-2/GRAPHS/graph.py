def create_graph(edges):
    # 1. Initialize the Adjacency List (Dictionary)
    graph = {}
    
    # 2. Iterate over the edges (O(E) time complexity)
    for u, v in edges:
        # 'u' is the start node, 'v' is the end node.

        # --- Handle the connection u -> v ---
        
        # Check if 'u' is already a key in the graph. 
        # If not, it uses the default value: an empty list [].
        if u not in graph:
            graph[u] = []
        
        # Add 'v' to the list of neighbors for 'u'.
        graph[u].append(v)
        
        # --- Handle the connection v -> u (since the graph is undirected) ---
        
        # Check if 'v' is already a key in the graph. 
        # If not, initialize it with an empty list [].
        if v not in graph:
            graph[v] = []
        
        # Add 'u' to the list of neighbors for 'v'.
        graph[v].append(u)
        
    return graph

# --- Test ---
edges = [('A', 'B'), ('A', 'C'), ('B', 'D')]
my_graph = create_graph(edges)
print("The Adjacency List is:")
print(my_graph)