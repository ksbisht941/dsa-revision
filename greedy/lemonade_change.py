from typing import List

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        """
        Return true if and only if you can provide every customer with correct change.
        
        :type bills: List[int]
        :rtype: bool
        """
        change = {
            5: 0,
            10: 0
        }

        for bill in bills:
            if bill == 5:
                change[5] += 1
            elif bill == 10:
                if not change[5]:
                    return False

                change[5] -= 1
                change[10] += 1
            else:
                if change[5] and change[10]:
                    change[5] -= 1
                    change[10] -= 1
                elif change[5] >= 3:
                    change[5] -= 3
                else:
                    return False

        return True
        

if __name__ == "__main__":
    test_cases = [
        ([5, 5, 5, 10, 20], True),
        ([10, 20], False),
        ([5, 5, 10, 10, 20], False),
        ([5, 5, 5, 10, 5, 20, 5, 10, 5, 20], True)
    ]
    
    solution = Solution()
    all_passed = True
    
    for i, (bills, expected) in enumerate(test_cases):
        print(f"Test case {i+1}: bills = {bills}")
        
        try:
            result = solution.lemonadeChange(bills[:])
            
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
