#!/usr/bin/python3
import sys


def is_safe(queens, row, col, n):
    """Check if placing a queen at (row, col) is safe."""
    for i in range(row):
        if (
            queens[i] == col or
            queens[i] - i == col - row or
            queens[i] + i == col + row
        ):
            return False
    return True


def solve_nqueens(n, row=0, queens=[]):
    """Solve the N-Queens problem using backtracking."""
    if row == n:
        print([[i, queens[i]] for i in range(n)])
        return

    for col in range(n):
        if is_safe(queens, row, col, n):
            solve_nqueens(n, row + 1, queens + [col])


def main():
    """Handle input validation and call the solver."""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    solve_nqueens(n)


if __name__ == "__main__":
    main()
