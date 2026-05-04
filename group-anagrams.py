# https://leetcode.com/problems/group-anagrams/
from collections import defaultdict
from typing import List

def groupAnagrams(strs: List[str]) -> List[List[str]]:
    groups = defaultdict(list)
    # print('groups', groups)

    for word in strs:
        count = [0] * 26

        for char in word:
            count[ord(char) - ord('a')] += 1
            
        groups[tuple(count)].append(word)

    return list(groups.values())
