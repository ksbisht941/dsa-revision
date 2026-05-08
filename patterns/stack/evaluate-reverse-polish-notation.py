# https://leetcode.com/problems/evaluate-reverse-polish-notation/
from typing import List


def eval_rpn(tokens: List[str]) -> int:
    """
    Evaluate an arithmetic expression in Reverse Polish Notation.

    Reverse Polish Notation places operators after their operands. This uses a
    stack to store numbers until an operator appears, then applies that operator
    to the last two numbers.

    Args:
        tokens (List[str]): Expression tokens containing integers and operators

    Returns:
        int: Result of the evaluated expression

    Time Complexity: O(n)
    Space Complexity: O(n)
    """

    operators = {"+", "-", "*", "/"}
    stack = []

    for token in tokens:
        if token in operators:
            # The second popped value is the right operand.
            right = stack.pop()
            left = stack.pop()

            if token == "+":
                stack.append(left + right)
            elif token == "-":
                stack.append(left - right)
            elif token == "*":
                stack.append(left * right)
            else:
                # int() truncates division toward zero, as required by LeetCode.
                stack.append(int(left / right))
        else:
            # Number tokens are stored until an operator needs them.
            stack.append(int(token))

    return stack[0]


if __name__ == "__main__":
    examples = [
        ["2", "1", "+", "3", "*"],
        ["4", "13", "5", "/", "+"],
        ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"],
    ]

    for tokens in examples:
        print(f"eval_rpn({tokens}) = {eval_rpn(tokens)}")
