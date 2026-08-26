from typing import List

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        The next greater element of some element x in an array is the first greater
        element that is to the right of x in the same array.
        
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        stack = []
        d = {}
        for x in nums2[::-1]:
            while stack and stack[-1] < x:
                stack.pop()

            if stack:
                d[x] = stack[-1]
                
            stack.append(x)

        return [d.get(x, -1) for x in nums1]


# [6, 0, 8, 1, 3]
# [8, 0, 0, 3, -1]

if __name__ == "__main__":
    test_cases = [
        # (nums1, nums2, expected)
        ([4, 1, 2], [1, 3, 4, 2], [-1, 3, -1]),
        ([2, 4], [1, 2, 3, 4], [3, -1]),
        ([1, 3, 5, 2, 4], [6, 5, 4, 3, 2, 1, 7], [7, 7, 7, 7, 7]),
        ([4,1,2,0], [3,4,2,0,1], [1,-1,1,1])
    ]
    
    solution = Solution()
    all_passed = True
    
    for i, (nums1, nums2, expected) in enumerate(test_cases):
        print(f"Test case {i+1}: nums1 = {nums1}, nums2 = {nums2}")
        
        try:
            # Prevent in-place modification of lists from interfering with test runners
            result = solution.nextGreaterElement(nums1[:], nums2[:])
            
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
