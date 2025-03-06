import sys


def is_safe(board, row, col, N):
    # Check the column
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True


def solve_nqueens(board, row, N):
    if row == N:
        # Print the solution
        for i in range(N):
            line = ['.' for _ in range(N)]
            line[board[i]] = 'Q'
            print("".join(line))
        return True

    solution_found = False
    for col in range(N):
        if is_safe(board, row, col, N):
            board[row] = col
            solution_found |= solve_nqueens(board, row + 1, N)
    return solution_found


def nqueens(N):
    if not isinstance(N, int):
        print("N must be a number")
        sys.exit(1)
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [-1] * N  # Initialize the board
    if not solve_nqueens(board, 0, N):
        print("No solution")
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    nqueens(N)
