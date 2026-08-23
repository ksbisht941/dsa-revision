from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        """
        Given n non-negative integers representing an elevation map where the width of each bar is 1,
        compute how much water it can trap after raining.
        
        :type height: List[int]
        :rtype: int
        """
        n = len(height)

        if n < 3:
            return 0

        left_max = [0] * n
        right_max = [0] * n

        left_max[0] = height[0]
        for idx in range(1, n):
            left_max[idx] = max(height[idx], left_max[idx - 1])

        right_max[n - 1] = height[n - 1]
        for idx in range(n - 2, -1, -1):
            right_max[idx] = max(height[idx], right_max[idx + 1])

        trapped_water = 0

        for idx in range(n):
            trapped_water += min(left_max[idx], right_max[idx]) - height[idx]

        return trapped_water

# input =           [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
# left_max =        [0, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 3]
# right_max =       [3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 1]
# trapped_water =    0, 0, 1, 0, 1, 2, 1, 0, 0, 1, 0, 0  -> 6

if __name__ == "__main__":
    test_cases = [
        # (height, expected)
        ([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], 6),
        ([4, 2, 0, 3, 2, 5], 9),
        ([], 0),
        ([3, 0, 2, 0, 4], 7),
        ([1, 1, 1, 1], 0)
    ]
    
    solution = Solution()
    all_passed = True
    
    for i, (height, expected) in enumerate(test_cases):
        print(f"Test case {i+1}: height = {height}")
        
        try:
            # We copy the list to prevent in-place modifications from affecting our test runner log if printed later
            result = solution.trap(height[:])
            
            if result == expected:
                print(f"  [+] PASS (Expected: {expected}, Got: {result})")
            else:
                print(f"  [-] FAIL (Expected: {expected}, Got: {result})")
                all_passed = False
        except NotImplementedError as e:
            print(f"  [-] ERROR: {e}")
            all_passed = False
        except Exception as e:
            print(f"  [-] ERROR: Exception thrown: {e}")
            all_passed = False
        print("-" * 30)
        
    if all_passed:
        print("\nResult: All test cases passed!")
    else:
        print("\nResult: Some test cases failed. Keep trying!")
