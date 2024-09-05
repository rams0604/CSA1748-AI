# Function to check if the current color assignment is valid
def is_safe(graph, node, color, colors):
    for neighbor in graph[node]:
        if colors[neighbor] == color:
            return False
    return True

# Backtracking function to solve the map coloring problem
def map_coloring(graph, colors, node, num_colors):
    # If all nodes have been colored, return True
    if node == len(graph):
        return True
    
    # Try assigning each color to the current node
    for color in range(num_colors):
        if is_safe(graph, node, color, colors):
            colors[node] = color  # Assign color
            if map_coloring(graph, colors, node + 1, num_colors):
                return True
            colors[node] = -1  # Backtrack
    
    return False

# Function to solve the map coloring problem
def solve_map_coloring(graph, num_colors):
    colors = [-1] * len(graph)  # Initialize all colors as unassigned (-1)
    
    if not map_coloring(graph, colors, 0, num_colors):
        return "No solution exists"
    
    # Return the color assignment
    return colors

# Example usage:
# Adjacency list of a graph (map)
graph = {
    0: [1, 2],
    1: [0, 2, 3],
    2: [0, 1, 3],
    3: [1, 2]
}

num_colors = 3  # Number of colors (for example, 3 colors)

# Solve the map coloring problem
solution = solve_map_coloring(graph, num_colors)

# Output the result
print("Color assignment:", solution)
