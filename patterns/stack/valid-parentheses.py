# https://leetcode.com/problems/valid-parentheses/


def is_valid_parentheses(s: str) -> bool:
    """
    Check if a string has valid parentheses.

    This uses a stack to track opening brackets. When a closing bracket appears,
    it must match the most recent opening bracket on top of the stack.

    Args:
        s (str): String containing only bracket characters

    Returns:
        bool: True if all brackets are correctly opened and closed

    Time Complexity: O(n)
    Space Complexity: O(n)
    """

    stack = []
    pairs = {
        ")": "(",
        "}": "{",
        "]": "[",
    }

    for char in s:
        # Closing brackets must match the latest opening bracket.
        if char in pairs:
            # Invalid if there is no opener or the opener does not match.
            if not stack or stack[-1] != pairs[char]:
                return False

            stack.pop()
        else:
            # Opening brackets are saved until their matching closer appears.
            stack.append(char)

    # Valid only when every opening bracket has been closed.
    return len(stack) == 0


if __name__ == "__main__":
    examples = [
        "()[]{}",
        "(]",
        "([])",
        "([)]",
        "{[]}",
        "",
    ]

    for s in examples:
        print(f"is_valid_parentheses({s!r}) = {is_valid_parentheses(s)}")
