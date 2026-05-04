def containsDuplicate(self, nums: List[int]) -> bool:
    seenNumbers = set()
    
    for num in nums:
        if num in seenNumbers:
            return True
        seenNumbers.add(num)
    
    return False
