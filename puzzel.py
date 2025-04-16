from collections import deque

# Defining the goal state
GOAL_STATE = [
    [5, 3, 6],
    [7, 0, 2],
    [4, 1, 8]
]

# Defining the possible moves (left, right, up, down)
MOVES = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # up, down, left, right

def is_valid_move(x, y):
    """Check if the position is within bounds of the puzzle grid."""
    return 0 <= x < 3 and 0 <= y < 3

def get_blank_position(state):
    """Find the position of the blank tile (represented by 0)."""
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j
    return -1, -1  # This should never happen if the puzzle is valid

def is_goal_state(state):
    """Check if the current state is the goal state."""
    return state == GOAL_STATE

def get_possible_states(state):
    """Generate all possible states from the current state by moving the blank tile."""
    x, y = get_blank_position(state)
    possible_states = []
    
    for dx, dy in MOVES:
        new_x, new_y = x + dx, y + dy
        if is_valid_move(new_x, new_y):
            # Create a new state by swapping the blank tile with its neighbor
            new_state = [row[:] for row in state]  # Make a copy of the state
            new_state[x][y], new_state[new_x][new_y] = new_state[new_x][new_y], new_state[x][y]
            possible_states.append(new_state)
    
    return possible_states

def bfs(start_state):
    """Perform BFS to find the shortest path from the start state to the goal state."""
    visited = set()
    queue = deque([(start_state, [])])  # (state, path)
    visited.add(tuple(map(tuple, start_state)))  # Add the start state to visited

    while queue:
        current_state, path = queue.popleft()
        
        if is_goal_state(current_state):
            return path  # Return the sequence of moves leading to the goal
        
        for next_state in get_possible_states(current_state):
            state_tuple = tuple(map(tuple, next_state))
            if state_tuple not in visited:
                visited.add(state_tuple)
                queue.append((next_state, path + [next_state]))
    
    return None  # If no solution is found

def print_state(state):
    """Print the state in a human-readable format."""
    for row in state:
        print(row)
    print()

# Example start state (this can be changed)
start_state = [
    [3, 7, 6],
    [5, 1, 2],
    [4, 0, 8]
]

# Solve the puzzle using BFS
path = bfs(start_state)

# Print the solution path
if path:
    print("Solution path:")
    for state in path:
        print_state(state)
else:
    print("No solution found.")
