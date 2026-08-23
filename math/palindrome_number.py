class Solution:
    def isPalindrome(self, x: int) -> bool:
        """
        Given an integer x, return true if x is a palindrome, and false otherwise.
        
        :type x: int
        :rtype: bool
        """
        temp = x
        reverse = 0

        while x > 0:
            remain = x % 10
            reverse = (reverse * 10) + remain
            x = x // 10

        return temp == reverse

if __name__ == "__main__":
    test_cases = [
        # (x, expected)
        (121, True),
        (-121, False),
        (10, False),
        (0, True),
        (12321, True)
    ]
    
    solution = Solution()
    all_passed = True
    
    for i, (x, expected) in enumerate(test_cases):
        print(f"Test case {i+1}: x = {x}")
        
        try:
            result = solution.isPalindrome(x)
            
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
