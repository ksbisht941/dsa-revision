# https://leetcode.com/problems/3sum/
from typing import List


def threeSum(nums: List[int]) -> List[List[int]]:
    """
    Find all unique triplets in the list that sum to zero.

    This implementation uses a sorted array and two pointers to efficiently
    search for valid triplets while skipping duplicates.

    Args:
        nums (List[int]): List of integers

    Returns:
        List[List[int]]: A list of unique triplets [a, b, c] such that a + b + c == 0

    Time Complexity: O(n^2)
    Space Complexity: O(n) for the output list, O(1) extra otherwise
    """

    nums.sort()
    result: List[List[int]] = []

    for idx in range(len(nums)):
        # Skip duplicate values for the first element of the triplet
        if idx > 0 and nums[idx] == nums[idx - 1]:
            continue

        left = idx + 1
        right = len(nums) - 1

        while left < right:
            current_sum = nums[idx] + nums[left] + nums[right]

            if current_sum < 0:
                # Need a larger sum, move left pointer to the right
                left += 1
            elif current_sum > 0:
                # Need a smaller sum, move right pointer to the left
                right -= 1
            else:
                result.append([nums[idx], nums[left], nums[right]])
                left += 1
                right -= 1

                # Skip duplicate values for the second element of the triplet
                while left < right and nums[left] == nums[left - 1]:
                    left += 1

                # Skip duplicate values for the third element of the triplet
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1

    return result


if __name__ == "__main__":
    test_cases = [
        ([ -1, 0, 1, 2, -1, -4 ], [[-1, -1, 2], [-1, 0, 1]]),
        ([0, 0, 0, 0], [[0, 0, 0]]),
        ([1, 2, -2, -1], []),
        ([-2, 0, 1, 1, 2], [[-2, 0, 2], [-2, 1, 1]]),
    ]

    for nums, expected in test_cases:
        result = threeSum(nums)
        print(f"threeSum({nums}) = {result}")
        print(f"Expected: {expected}\n")

        