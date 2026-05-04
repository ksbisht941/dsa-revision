# https://leetcode.com/problems/contains-duplicate/
from typing import List

def containsDuplicate(nums: List[int]) -> bool:
    """
    Check if an array contains any duplicate elements.

    This function uses a hash set to track seen numbers, providing O(1) lookup time.

    Args:
        nums (List[int]): Array of integers to check for duplicates

    Returns:
        bool: True if array contains duplicates, False otherwise

    Time Complexity: O(n) where n is the length of the array
    Space Complexity: O(n) in worst case (all unique elements)
    """

    # Use a set to track numbers we've seen
    seenNumbers = set()

    # Iterate through each number in the array
    for num in nums:
        # If we've seen this number before, we found a duplicate
        if num in seenNumbers:
            return True
        # Add the number to our set of seen numbers
        seenNumbers.add(num)

    # If we reach here, no duplicates were found
    return False


# Test the function with example inputs
if __name__ == "__main__":
    # Test case 1: Array with duplicates
    nums1 = [1, 2, 3, 1]
    result1 = containsDuplicate(nums1)
    print(f"containsDuplicate({nums1}) = {result1}")

    # Test case 2: Array with no duplicates
    nums2 = [1, 2, 3, 4]
    result2 = containsDuplicate(nums2)
    print(f"containsDuplicate({nums2}) = {result2}")

    # Test case 3: Empty array
    nums3 = []
    result3 = containsDuplicate(nums3)
    print(f"containsDuplicate({nums3}) = {result3}")

    # Test case 4: Array with multiple duplicates
    nums4 = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
    result4 = containsDuplicate(nums4)
    print(f"containsDuplicate({nums4}) = {result4}")
