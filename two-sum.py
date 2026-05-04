# https://leetcode.com/problems/two-sum/
def twoSum(self, nums: List[int], target: int) -> List[int]:
    seen = {}

    for idx in range(len(nums)):
        complement = target - nums[idx]

        if complement in seen:
            return [seen[complement], idx]

        seen[nums[idx]] = idx
    
    return []
