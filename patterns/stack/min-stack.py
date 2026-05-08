# https://leetcode.com/problems/min-stack/

class MinStack:
    """
    Stack that can return the minimum value in O(1) time.

    This uses two stacks:
    - stack stores all pushed values
    - min_stack stores the minimum value available at each stack level

    Time Complexity:
        push: O(1)
        pop: O(1)
        top: O(1)
        get_min: O(1)

    Space Complexity: O(n)
    """

    def __init__(self) -> None:
        """Create an empty min stack."""
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        """
        Push a value onto the stack.

        The min_stack stores the smaller value between the new value and the
        previous minimum, so its top is always the current minimum.
        """
        self.stack.append(val)

        if not self.min_stack:
            self.min_stack.append(val)
        else:
            self.min_stack.append(
                min(
                    self.min_stack[-1],
                    val,
                )
            )

    def pop(self) -> None:
        """Remove the top value from both stacks."""
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        """Return the top value from the stack."""
        return self.stack[-1]

    def get_min(self) -> int:
        """Return the current minimum value in the stack."""
        return self.min_stack[-1]

    # LeetCode uses camelCase for this method name.
    def getMin(self) -> int:
        """Return the current minimum value in the stack."""
        return self.get_min()


if __name__ == "__main__":
    min_stack = MinStack()

    min_stack.push(-2)
    min_stack.push(0)
    min_stack.push(-3)
    print(f"get_min() = {min_stack.get_min()}")

    min_stack.pop()
    print(f"top() = {min_stack.top()}")
    print(f"get_min() = {min_stack.get_min()}")
