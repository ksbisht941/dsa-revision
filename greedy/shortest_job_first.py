from typing import List

class Solution:
    def sjf(self, n: int, jobs: List[List[int]]) -> float:
        """
        Calculate and return the average waiting time for the given processes using the 
        Shortest Job First (SJF) non-preemptive scheduling algorithm.
        
        :type n: int
        :type jobs: List[List[int]] (where each inner list is [arrival_time, burst_time])
        :rtype: float
        """
        # TODO: Implement this method
        raise NotImplementedError("Implement your solution here")

if __name__ == "__main__":
    test_cases = [
        # (n, jobs, expected_average_waiting_time)
        # Job 0: at=0, bt=3 (starts 0, ends 3, wt=0)
        # Job 2: at=2, bt=1 (starts 3, ends 4, wt=1)
        # Job 1: at=1, bt=4 (starts 4, ends 8, wt=3)
        # Total wt = 0 + 1 + 3 = 4. Average = 4/3 = 1.33
        (3, [[0, 3], [1, 4], [2, 1]], 1.33),
        
        # Job 0: at=0, bt=5 (starts 0, ends 5, wt=0)
        # Job 1: at=1, bt=2 (starts 5, ends 7, wt=4)
        # Job 2: at=2, bt=1 (starts 7, ends 8, wt=5)
        # Total wt = 0 + 4 + 5 = 9. Average = 9/3 = 3.00
        (3, [[0, 5], [1, 2], [2, 1]], 3.00),
    ]
    
    solution = Solution()
    all_passed = True
    
    for i, (n, jobs, expected) in enumerate(test_cases):
        print(f"Test case {i+1}: n = {n}, jobs = {jobs}")
        
        try:
            # Pass a deep copy of the jobs list to prevent in-place modifications from affecting our test runner log
            jobs_copy = [job[:] for job in jobs]
            result = solution.sjf(n, jobs_copy)
            
            # Using absolute difference to handle floating point precision issues
            if result is not None and abs(result - expected) <= 0.01:
                print(f"  [+] PASS (Expected: {expected}, Got: {result:.2f})")
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
