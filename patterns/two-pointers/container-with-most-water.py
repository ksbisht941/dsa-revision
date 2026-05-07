from typing import List


def max_area(height: List[int]) -> int:
    """
    Calculate the maximum water container area.

    This uses two pointers at both ends of the height list. By moving the pointer
    at the shorter line inward, we search for a larger possible area efficiently.

    Args:
        height (List[int]): Heights of vertical lines

    Returns:
        int: Maximum area between any two lines

    Time Complexity: O(n)
    Space Complexity: O(1)
    """

    max_area_value = 0
    left = 0
    right = len(height) - 1

    while left < right:
        width = right - left
        current_area = width * min(height[left], height[right])
        max_area_value = max(max_area_value, current_area)

        if height[left] <= height[right]:
            left += 1
        else:
            right -= 1

    return max_area_value


if __name__ == "__main__":
    examples = [
        [1, 8, 6, 2, 5, 4, 8, 3, 7],
        [1, 1],
        [4, 3, 2, 1, 4],
        [1, 2, 1],
    ]

    for heights in examples:
        print(f"max_area({heights}) = {max_area(heights)}")
