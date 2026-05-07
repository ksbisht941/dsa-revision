from typing import List


def bubble_sort(nums: List[int]) -> List[int]:
    """
    Sort an array using the bubble sort algorithm.

    Bubble sort repeatedly compares adjacent elements and swaps them when they
    are in the wrong order. After each full pass, the largest remaining element
    has moved to its correct position at the end of the array.

    Args:
        nums (List[int]): Array of integers to sort

    Returns:
        List[int]: Sorted array in ascending order

    Time Complexity: O(n^2)
    Space Complexity: O(1)
    """

    # Work on a copy so the original input list stays unchanged.
    sorted_nums = nums.copy()
    n = len(sorted_nums)

    # Each pass places the next largest value at the end.
    for idx in range(n - 1):
        # Last idx elements are already sorted, so skip them.
        for jdx in range(n - 1 - idx):
            # Swap adjacent values if they are in the wrong order.
            if sorted_nums[jdx] > sorted_nums[jdx + 1]:
                sorted_nums[jdx], sorted_nums[jdx + 1] = (
                    sorted_nums[jdx + 1],
                    sorted_nums[jdx],
                )

    return sorted_nums


if __name__ == "__main__":
    examples = [
        [5, 1, 4, 2, 8],
        [64, 34, 25, 12, 22, 11, 90],
        [1, 2, 3, 4, 5],
        [3, 3, 2, 1],
    ]

    for nums in examples:
        print(f"bubble_sort({nums}) = {bubble_sort(nums)}")
