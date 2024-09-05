from itertools import permutations

def calculate_distance(path, distance_matrix):
    """Calculate the total distance of a given path based on the distance matrix."""
    total_distance = 0
    for i in range(len(path) - 1):
        total_distance += distance_matrix[path[i]][path[i + 1]]
    # Return to the starting point
    total_distance += distance_matrix[path[-1]][path[0]]
    return total_distance

def travelling_salesman_brute_force(distance_matrix):
    """Solve the TSP using brute force."""
    n = len(distance_matrix)
    shortest_path = None
    min_distance = float('inf')

    for perm in permutations(range(n)):
        current_distance = calculate_distance(perm, distance_matrix)
        if current_distance < min_distance:
            min_distance = current_distance
            shortest_path = perm

    return shortest_path, min_distance

# Example usage
if __name__ == "__main__":
    # Distance matrix for 4 cities
    distance_matrix = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
    ]

    path, distance = travelling_salesman_brute_force(distance_matrix)
    print("Shortest path:", path)
    print("Minimum distance:", distance)
