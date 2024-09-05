from heapq import heappop, heappush

# Heuristic function (in this case, we are using the Manhattan distance as the heuristic)
def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

# A* Algorithm function
def astar(grid, start, goal):
    # Priority queue to store (cost, node) where cost = g(n) + h(n)
    open_set = []
    heappush(open_set, (0, start))
    
    # Dictionaries to store the cost from the start node and the parent node
    came_from = {}
    g_score = {start: 0}
    
    # While there are still nodes to process
    while open_set:
        # Get the node in open_set with the lowest cost
        current = heappop(open_set)[1]
        
        # If we reached the goal, reconstruct the path
        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            path.reverse()
            return path
        
        # Get the possible neighbors of the current node
        neighbors = get_neighbors(grid, current)
        
        for neighbor in neighbors:
            # Tentative g_score of the neighbor
            tentative_g_score = g_score[current] + 1  # Assuming all edges have weight 1
            
            if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                # Update the cost and parent of the neighbor
                g_score[neighbor] = tentative_g_score
                f_score = tentative_g_score + heuristic(neighbor, goal)
                heappush(open_set, (f_score, neighbor))
                came_from[neighbor] = current
    
    return None  # Return None if no path is found

# Function to get the valid neighbors of a given node
def get_neighbors(grid, node):
    neighbors = []
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Four possible directions: right, down, left, up
    
    for direction in directions:
        neighbor = (node[0] + direction[0], node[1] + direction[1])
        
        # Check if the neighbor is within the grid and is not a wall (represented by 1)
        if 0 <= neighbor[0] < len(grid) and 0 <= neighbor[1] < len(grid[0]) and grid[neighbor[0]][neighbor[1]] == 0:
            neighbors.append(neighbor)
    
    return neighbors

# Example usage:
grid = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]

start = (0, 0)
goal = (4, 4)

# Find the shortest path using A*
path = astar(grid, start, goal)

# Output the result
print("Shortest path:", path)
