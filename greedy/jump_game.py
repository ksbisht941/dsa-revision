from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
        Return true if you can reach the last index, or false otherwise.
        
        :type nums: List[int]
        :rtype: bool
        """
        # TODO: Implement this method
        raise NotImplementedError("Implement your solution here")

if __name__ == "__main__":
    test_cases = [
        # (nums, expected)
        ([2, 3, 1, 1, 4], True),
        ([3, 2, 1, 0, 4], False),
        ([0], True),
        ([2, 0, 0], True),
        ([2, 5, 0, 0], True)
    ]
    
    solution = Solution()
    all_passed = True
    
    for i, (nums, expected) in enumerate(test_cases):
        print(f"Test case {i+1}: nums = {nums}")
        
        try:
            # We copy the list to prevent in-place modifications from affecting our test runner log if printed later
            result = solution.canJump(nums[:])
            
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
