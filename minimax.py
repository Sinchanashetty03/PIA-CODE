# Define the Minimax function
def minimax(depth, nodeIndex, isMax, scores, targetDepth):
    # If we have reached the target depth, return the score
    if depth == targetDepth:
        return scores[nodeIndex]
    
    if isMax:
        # Maximizing player (Max)
        best = -float('inf')
        
        # There are two children, check both
        for i in range(2):
            value = minimax(depth + 1, nodeIndex * 2 + i, False, scores, targetDepth)
            best = max(best, value)
        return best
    else:
        # Minimizing player (Min)
        best = float('inf')
        
        # There are two children, check both
        for i in range(2):
            value = minimax(depth + 1, nodeIndex * 2 + i, True, scores, targetDepth)
            best = min(best, value)
        return best

# Example tree values (leaf scores)
scores = [3, 5, 2, 9]  # Leaf scores

# Call the minimax function
result = minimax(0, 0, True, scores, 2)

# Output the result
print(f"Optimal score: {result}")
