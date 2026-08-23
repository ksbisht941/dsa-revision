class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        bucket = set()
        left = 0
        longest = 0

        for right in range(len(s)):
            while s[right] in bucket:
                bucket.remove(s[left])
                left += 1

            bucket.add(s[right])

            longest = max(longest, right - left + 1)

        print(bucket)
        return longest

if __name__ == "__main__":
    test_cases = [
        ("abcabcbb", 3),
        ("bbbbb", 1),
        ("pwwkew", 3),
        ("", 0),
        (" ", 1),
        ("au", 2),
        ("dvdf", 3)
    ]
    
    solution = Solution()
    all_passed = True
    
    for i, (s, expected) in enumerate(test_cases):
        print(f"Test case {i+1}: s = {repr(s)}")
        try:
            result = solution.lengthOfLongestSubstring(s)
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
