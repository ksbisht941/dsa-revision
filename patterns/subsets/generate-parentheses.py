# https://leetcode.com/problems/generate-parentheses/
from typing import List


def generate_parenthesis(n: int) -> List[str]:
    """
    Generate all valid combinations of n pairs of parentheses.

    This uses backtracking to build each valid string one character at a time.
    We can add an opening bracket while open_count < n, and we can add a closing
    bracket only when it will not exceed the number of opening brackets.

    Args:
        n (int): Number of parentheses pairs

    Returns:
        List[str]: All valid parentheses combinations

    Time Complexity: O(4^n / sqrt(n))
    Space Complexity: O(n)
    """

    result = []

    def backtrack(current: str, open_count: int, close_count: int) -> None:
        # A complete valid combination has exactly n opening and n closing chars.
        if len(current) == n * 2:
            result.append(current)
            return

        # Add "(" if we still have opening brackets available.
        if open_count < n:
            backtrack(
                current + "(",
                open_count + 1,
                close_count,
            )

        # Add ")" only when there is an unmatched "(" to close.
        if close_count < open_count:
            backtrack(
                current + ")",
                open_count,
                close_count + 1,
            )

    backtrack("", 0, 0)
    return result


# LeetCode uses camelCase for this function name.
def generateParenthesis(n: int) -> List[str]:
    """Generate all valid combinations of n pairs of parentheses."""
    return generate_parenthesis(n)


if __name__ == "__main__":
    examples = [1, 2, 3]

    for n in examples:
        print(f"generate_parenthesis({n}) = {generate_parenthesis(n)}")
