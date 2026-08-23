class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        Given a string s, return true if it is a palindrome, or false otherwise.
        
        :type s: str
        :rtype: bool
        """
        left, right = 0, len(s) - 1

        while left < right:
            
            while left < right and not s[left].isalnum():
                left += 1
        
            while left < right and not s[right].isalnum():
                right -= 1

            if s[left].lower() != s[right].lower():
                return False
                
            left += 1
            right -= 1
                
        
        return True

if __name__ == "__main__":
    test_cases = [
        # (s, expected)
        ("A man, a plan, a canal: Panama", True),
        ("race a car", False),
        (" ", True),
        ("0P", False),
        ("a.", True)
    ]
    
    solution = Solution()
    all_passed = True
    
    for i, (s, expected) in enumerate(test_cases):
        print(f"Test case {i+1}: s = \"{s}\"")
        
        try:
            result = solution.isPalindrome(s)
            
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
