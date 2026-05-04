# https://leetcode.com/problems/top-k-frequent-elements/
import heapq
from collections import Counter
from typing import List

def topKFrequent(nums: List[int], k: int) -> List[int]:
    """
    Find the k most frequent elements in an array.

    This function uses a Counter to count frequencies and heapq.nlargest to
    efficiently find the top k elements by frequency.

    Args:
        nums (List[int]): Array of integers
        k (int): Number of most frequent elements to return

    Returns:
        List[int]: The k most frequent elements (order may vary)

    Time Complexity: O(n log k) where n is array length
    Space Complexity: O(n) for the Counter
    """

    # Count frequency of each number using Counter
    count = Counter(nums)
    print(f"Frequency count: {count}")

    # Use heapq.nlargest to get k elements with highest frequency
    # nlargest uses a heap internally for efficiency
    return heapq.nlargest(
        k,           # Number of elements to return
        count.keys(), # Elements to choose from
        key=count.get # Key function: get frequency of each element
    )


# Test the function with example inputs
if __name__ == "__main__":
    # Test case 1: Standard case
    nums1 = [1, 1, 1, 2, 2, 3]
    k1 = 2
    result1 = topKFrequent(nums1, k1)
    print(f"topKFrequent({nums1}, {k1}) = {result1}")

    print()  # Empty line for readability

    # Test case 2: All elements unique
    nums2 = [1, 2, 3, 4, 5]
    k2 = 3
    result2 = topKFrequent(nums2, k2)
    print(f"topKFrequent({nums2}, {k2}) = {result2}")

    print()  # Empty line for readability

    # Test case 3: k equals array length
    nums3 = [1, 2, 2, 3, 3, 3]
    k3 = 3
    result3 = topKFrequent(nums3, k3)
    print(f"topKFrequent({nums3}, {k3}) = {result3}")

    print()  # Empty line for readability

    # Test case 4: Single element repeated
    nums4 = [5, 5, 5, 5, 5]
    k4 = 1
    result4 = topKFrequent(nums4, k4)
    print(f"topKFrequent({nums4}, {k4}) = {result4}")
