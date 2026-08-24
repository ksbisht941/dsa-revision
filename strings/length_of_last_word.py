class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        """
        Return the length of the last word in the string.
        
        :type s: str
        :rtype: int
        """
        # Approch 1
        # right = len(s) - 1

        # while right >= 0 and s[right] == " ":
        #     right -= 1

        # max_len = 0
        # while right >= 0 and s[right] != " ":
        #     right -= 1
        #     max_len += 1

        # return max_len

        # Approch 2
        max_len = 0

        for idx in range(len(s) - 1, -1, -1):
            if s[idx] == " " and max_len > 0:
                break

            if s[idx] != " ":
                max_len += 1

        return max_len

if __name__ == "__main__":
    test_cases = [
        # (s, expected)
        ("Hello World", 5),
        ("   fly me   to   the moon  ", 4),
        ("luffy is still joyboy", 6),
        ("a", 1),
        ("    day", 3)
    ]
    
    solution = Solution()
    all_passed = True
    
    for i, (s, expected) in enumerate(test_cases):
        print(f"Test case {i+1}: s = \"{s}\"")
        
        try:
            result = solution.lengthOfLastWord(s)
            
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
