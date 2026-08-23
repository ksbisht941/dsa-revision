from typing import List

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        raise NotImplementedError("Implement your solution here")

if __name__ == "__main__":
    test_cases = [
        ([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2, 6),
        ([0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], 3, 10),
        ([0, 0, 0, 0], 0, 0),
        ([1, 1, 1, 1], 0, 4)
    ]
    
    solution = Solution()
    all_passed = True
    
    for i, (nums, k, expected) in enumerate(test_cases):
        print(f"Test case {i+1}: k = {k}, nums = {nums}")
        try:
            result = solution.longestOnes(nums, k)
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
