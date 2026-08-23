from typing import List

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        # Approch 1: Brute Force
        # max_count = 0
        # for left_count in range(k + 1):
        #     right_count = k - left_count

        #     left_sum = sum(cardPoints[:left_count])
        #     right_sum = sum(cardPoints[len(cardPoints) - right_count:])

        #     max_count = max(max_count, left_sum + right_sum)
        # return max_count


        # Approch 2: Left/Right Exchange
        n = len(cardPoints)
        current = sum(cardPoints[:k])
        max_sum = 0

        for idx in range(k):
            current -= cardPoints[k - idx - 1]
            current += cardPoints[n - idx - 1]
            
            max_sum = max(max_sum, current)

        return max_sum

        

if __name__ == "__main__":
    test_cases = [
        ([1, 2, 3, 4, 5, 6, 1], 3, 12),
        ([2, 2, 2], 2, 4),
        ([9, 7, 7, 9, 7, 7, 9], 7, 55),
        ([1, 1000, 1], 1, 1),
        ([1, 79, 80, 1, 1, 1, 200, 1], 3, 202)
    ]
    
    solution = Solution()
    all_passed = True
    
    for i, (cardPoints, k, expected) in enumerate(test_cases):
        print(f"Test case {i+1}: cardPoints = {cardPoints}, k = {k}")
        try:
            result = solution.maxScore(cardPoints, k)
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
