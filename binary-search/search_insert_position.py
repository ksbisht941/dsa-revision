from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        """
        Given a sorted array of distinct integers and a target value, return the index if the target is found.
        If not, return the index where it would be if it were inserted in order.
        
        You must write an algorithm with O(log n) runtime complexity.
        
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        low, high = 0, len(nums) - 1
        answer = len(nums)

        while low <= high:
            mid = (low + high) // 2

            if nums[mid] >= target:
                answer = mid
                high = mid - 1
            else:
                low = mid + 1

        return answer

if __name__ == "__main__":
    test_cases = [
        # (nums, target, expected)
        ([1, 3, 5, 6], 5, 2),
        ([1, 3, 5, 6], 2, 1),
        ([1, 3, 5, 6], 7, 4),
        ([1, 3, 5, 6], 0, 0),
        ([1], 0, 0)
    ]
    
    solution = Solution()
    all_passed = True
    
    for i, (nums, target, expected) in enumerate(test_cases):
        print(f"Test case {i+1}: nums = {nums}, target = {target}")
        
        try:
            result = solution.searchInsert(nums[:], target)
            
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
