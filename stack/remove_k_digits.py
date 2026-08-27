class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        """
        Given string num representing a non-negative integer num, and an integer k, 
        return the smallest possible integer after removing k digits from num.
        
        :type num: str
        :type k: int
        :rtype: str
        """
        stack = []
        for x in num:
            while stack and k > 0 and stack[-1] > x:
                stack.pop()
                k -= 1
            
            stack.append(x)

        if k > 0:
            stack = stack[:-k]

        result = "".join(stack).lstrip("0")
        return result if result else "0"

if __name__ == "__main__":
    test_cases = [
        # (num, k, expected)
        ("1432219", 3, "1219"),
        ("10200", 1, "200"),
        ("10", 2, "0"),
        ("9", 1, "0"),
        ("112", 1, "11")
    ]
    
    solution = Solution()
    all_passed = True
    
    for i, (num, k, expected) in enumerate(test_cases):
        print(f"Test case {i+1}: num = {num}, k = {k}")
        
        try:
            result = solution.removeKdigits(num, k)
            
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
