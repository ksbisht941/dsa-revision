# https://leetcode.com/problems/valid-sudoku/
from typing import List
from collections import defaultdict


def isValidSudoku(board: List[List[str]]) -> bool:
    """
    Check whether a given 9x9 Sudoku board is valid.

    A valid board must satisfy three conditions:
    1. Each row contains unique digits 1-9 (ignoring empty cells).
    2. Each column contains unique digits 1-9.
    3. Each 3x3 sub-box contains unique digits 1-9.

    Args:
        board (List[List[str]]): 2D list representing the Sudoku board

    Returns:
        bool: True if the board is valid, False otherwise
    """

    rows = defaultdict(set)
    cols = defaultdict(set)
    boxes = defaultdict(set)

    # Iterate through every cell in the 9x9 board
    for r in range(9):
        for c in range(9):
            value = board[r][c]

            # Ignore empty cells represented with a dot
            if value == ".":
                continue

            box = (r // 3, c // 3)

            # If the value already exists in the row, column, or 3x3 box, the board is invalid
            if (
                value in rows[r]
                or value in cols[c]
                or value in boxes[box]
            ):
                return False

            rows[r].add(value)
            cols[c].add(value)
            boxes[box].add(value)

    return True


if __name__ == "__main__":
    sample_board = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    ]

    result = isValidSudoku(sample_board)
    print(f"isValidSudoku(sample_board) = {result}")

