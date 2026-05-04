# https://leetcode.com/problems/valid-anagram/description/
def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    
    count = {}
    
    for ch in s:
        count[ch] = count.get(ch, 0) + 1
    
    print(count)
    
    for ch in t:
        if ch not in count or count[ch] == 0:
            return False
        count[ch] -= 1
    
    return True
