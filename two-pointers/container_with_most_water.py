from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai).
        n vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0).
        Find two lines, which, together with the x-axis forms a container, such that the container contains the most water.
        
        :type height: List[int]
        :rtype: int
        """
        left, right = 0, len(height) - 1
        max_water = 0

        while left < right:
            area = (right - left) * min(height[left], height[right])
            max_water = max(max_water, area)

            if height[left] >= height[right]:
                right -= 1
            else:
                left += 1



        return max_water
        


if __name__ == "__main__":
    test_cases = [
        # (height, expected)
        ([1, 8, 6, 2, 5, 4, 8, 3, 7], 49),
        ([1, 1], 1),
        ([4, 3, 2, 1, 4], 16),
        ([1, 2, 1], 2),
        ([2, 3, 4, 5, 18, 17, 6], 17)
    ]
    
    solution = Solution()
    all_passed = True
    
    for i, (height, expected) in enumerate(test_cases):
        print(f"Test case {i+1}: height = {height}")
        
        try:
            # We copy the list to prevent in-place modifications from affecting our test runner log if printed later
            result = solution.maxArea(height[:])
            
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
