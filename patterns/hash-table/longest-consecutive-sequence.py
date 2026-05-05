# https://leetcode.com/problems/longest-consecutive-sequence/
from typing import List


def longestConsecutive(nums: List[int]) -> int:
    """
    Find the length of the longest consecutive sequence in an unsorted array.

    This function uses a hash set for O(1) lookups. For each number, we check
    if it's the start of a sequence (i.e., num-1 not in set) and then count how
    many consecutive numbers follow it.

    Args:
        nums (List[int]): Array of integers

    Returns:
        int: Length of the longest consecutive sequence

    Time Complexity: O(n) - each number is visited at most twice
    Space Complexity: O(n) - for the set
    """

    # Convert list to set for O(1) lookup
    num_set = set(nums)
    longest = 1 if nums else 0

    # Iterate through unique numbers
    for num in num_set:
        # Only start counting from the beginning of a sequence
        # (when num-1 is not in the set)
        if num - 1 not in num_set:
            length = 1

            # Count how many consecutive numbers follow this one
            while num + length in num_set:
                length += 1

            # Update the longest sequence length
            longest = max(longest, length)

    return longest


if __name__ == "__main__":
    # Test case 1: Standard case with multiple sequences
    nums1 = [100, 4, 200, 1, 3, 2]
    result1 = longestConsecutive(nums1)
    print(f"longestConsecutive({nums1}) = {result1}")

    # Test case 2: Already sorted sequence
    nums2 = [1, 2, 3, 4, 5]
    result2 = longestConsecutive(nums2)
    print(f"longestConsecutive({nums2}) = {result2}")

    # Test case 3: No consecutive numbers
    nums3 = [10, 20, 30, 40]
    result3 = longestConsecutive(nums3)
    print(f"longestConsecutive({nums3}) = {result3}")

    # Test case 4: Empty list
    nums4 = []
    result4 = longestConsecutive(nums4)
    print(f"longestConsecutive({nums4}) = {result4}")

    # Test case 5: Single element
    nums5 = [42]
    result5 = longestConsecutive(nums5)
    print(f"longestConsecutive({nums5}) = {result5}")
