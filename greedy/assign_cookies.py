from typing import List

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        """
        Return the maximum number of your children you can assign cookies to.
        
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        # TODO: Implement this method
        raise NotImplementedError("Implement your solution here")

if __name__ == "__main__":
    test_cases = [
        # (g, s, expected)
        ([1, 2, 3], [1, 1], 1),
        ([1, 2], [1, 2, 3], 2),
        ([1, 2, 3], [], 0),
        ([], [1, 2, 3], 0),
        ([10, 9, 8, 7], [5, 6, 7, 8], 2)
    ]
    
    solution = Solution()
    all_passed = True
    
    for i, (g, s, expected) in enumerate(test_cases):
        print(f"Test case {i+1}: g = {g}, s = {s}")
        
        try:
            # We copy the lists to prevent in-place modifications from affecting our test runner log if printed later
            result = solution.findContentChildren(g[:], s[:])
            
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
