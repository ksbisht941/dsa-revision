# https://leetcode.com/problems/two-sum/
from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    """
    Find two indices in an array that add up to a target sum.

    This function uses a hash table to store numbers we've seen and their indices.
    For each number, we check if its complement (target - number) exists in the hash table.
    If found, we return the indices; otherwise, we store the current number.

    Args:
        nums (List[int]): Array of integers
        target (int): Target sum to find

    Returns:
        List[int]: Indices [i, j] where nums[i] + nums[j] == target, or [] if no solution

    Time Complexity: O(n) where n is the length of the array
    Space Complexity: O(n) for the hash table
    """

    # Dictionary to store number -> index mapping
    seen = {}

    # Iterate through each number with its index
    for idx in range(len(nums)):
        # Calculate the complement needed to reach the target
        complement = target - nums[idx]

        # Check if complement exists in our seen dictionary
        if complement in seen:
            # Found the pair! Return indices
            return [seen[complement], idx]

        # Store current number and its index for future complements
        seen[nums[idx]] = idx

    # No solution found
    return []


# Test the function with example inputs
if __name__ == "__main__":
    # Test case 1: Standard case with solution
    nums1 = [2, 7, 11, 15]
    target1 = 9
    result1 = twoSum(nums1, target1)
    print(f"twoSum({nums1}, {target1}) = {result1}")

    # Test case 2: Multiple possible pairs, returns first found
    nums2 = [3, 2, 4]
    target2 = 6
    result2 = twoSum(nums2, target2)
    print(f"twoSum({nums2}, {target2}) = {result2}")

    # Test case 3: No solution exists
    nums3 = [1, 2, 3, 4]
    target3 = 10
    result3 = twoSum(nums3, target3)
    print(f"twoSum({nums3}, {target3}) = {result3}")

    # Test case 4: Same number used twice
    nums4 = [3, 3]
    target4 = 6
    result4 = twoSum(nums4, target4)
    print(f"twoSum({nums4}, {target4}) = {result4}")
