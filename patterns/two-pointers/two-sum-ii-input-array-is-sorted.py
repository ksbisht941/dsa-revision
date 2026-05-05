# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
from typing import List


def twoSum(numbers: List[int], target: int) -> List[int]:
    """
    Find two indices (1-indexed) in a sorted array that add up to the target sum.

    This function uses two pointers starting from both ends of the sorted array.
    Since the array is sorted, we can efficiently find the pair by moving pointers
    based on the sum comparison.

    Args:
        numbers (List[int]): Sorted array of integers
        target (int): Target sum to find

    Returns:
        List[int]: 1-indexed indices [i, j] where numbers[i-1] + numbers[j-1] == target,
                   or [-1, -1] if no solution exists

    Time Complexity: O(n) where n is the length of the array
    Space Complexity: O(1) - only uses constant extra space
    """

    left = 0
    right = len(numbers) - 1

    while left < right:
        current_sum = numbers[left] + numbers[right]

        if current_sum == target:
            # Return 1-indexed positions
            return [left + 1, right + 1]
        elif current_sum > target:
            # Sum is too large, move right pointer left to decrease sum
            right -= 1
        else:
            # Sum is too small, move left pointer right to increase sum
            left += 1

    # No solution found
    return [-1, -1]


if __name__ == "__main__":
    # Test case 1: Standard case
    numbers1 = [2, 7, 11, 15]
    target1 = 9
    result1 = twoSum(numbers1, target1)
    print(f"twoSum({numbers1}, {target1}) = {result1}")

    # Test case 2: Another valid pair
    numbers2 = [2, 3, 4]
    target2 = 6
    result2 = twoSum(numbers2, target2)
    print(f"twoSum({numbers2}, {target2}) = {result2}")

    # Test case 3: No solution exists
    numbers3 = [1, 2, 3, 4]
    target3 = 10
    result3 = twoSum(numbers3, target3)
    print(f"twoSum({numbers3}, {target3}) = {result3}")

    # Test case 4: Negative numbers
    numbers4 = [-3, -1, 0, 2, 4]
    target4 = -1
    result4 = twoSum(numbers4, target4)
    print(f"twoSum({numbers4}, {target4}) = {result4}")

    # Test case 5: Duplicate numbers
    numbers5 = [1, 2, 2, 3]
    target5 = 4
    result5 = twoSum(numbers5, target5)
    print(f"twoSum({numbers5}, {target5}) = {result5}")

        