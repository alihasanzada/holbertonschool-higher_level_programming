#!/usr/bin/python3
"""Solves the N queens problem using backtracking"""
import sys


def solve(n, row, cols, solution, results):
    """Place queens row by row, recording every valid board"""
    if row == n:
        results.append(solution[:])
        return
    for col in range(n):
        ok = True
        for r, c in solution:
            if c == col or abs(c - col) == abs(r - row):
                ok = False
                break
        if ok:
            solution.append([row, col])
            solve(n, row + 1, cols, solution, results)
            solution.pop()


if __name__ == "__main__":
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
    results = []
    solve(n, 0, [], [], results)
    for res in results:
        print(res)
