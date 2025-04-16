def cb():
    """Creates a board from user input."""
    board = []
    print("Enter 4 rows, each with 4 characters (1 or Q):")
    for _ in range(4):
        row_input = input("Enter row: ")
        if len(row_input) != 4 or not all(c in '1Q' for c in row_input):
            print("Invalid input. Please enter 4 characters (1 or Q).")
            return None  # Indicate invalid input
        board.append(list(row_input))  # Convert input string to list of characters
    return board

def get_queens_positions(board):
    """Returns the queen positions from a given board."""
    queens = []
    for row_index, row in enumerate(board):
        for col_index, cell in enumerate(row):
            if cell == 'Q':
                queens.append((row_index, col_index))
    return queens

def is_safe(queens):
    for i in range(len(queens)):
        for j in range(i + 1, len(queens)):
            r1, c1 = queens[i]
            r2, c2 = queens[j]
            if r1 == r2 or c1 == c2 or abs(r1 - r2) == abs(c1 - c2):
                return False
    return True

def show_result(board, queens):
    for row in board:
        print(row)
    print("Safe. Game Won." if is_safe(queens) else "Unsafe. Game Lost.")

def main():
    board = cb()
    if board: #if board is not none.
        queens = get_queens_positions(board)
        show_result(board, queens)
    else:
        print("Game aborted due to invalid input.")

if __name__ == "__main__":
    main()