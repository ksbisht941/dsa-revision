# https://leetcode.com/problems/group-anagrams/
from collections import defaultdict
from typing import List

def groupAnagrams(strs: List[str]) -> List[List[str]]:
    """
    Group strings that are anagrams of each other.

    This function uses a character count array as a hashable key to group anagrams.
    Each string is converted to a count of its characters (a-z), and strings with
    identical character counts are grouped together.

    Args:
        strs (List[str]): List of strings to group by anagrams

    Returns:
        List[List[str]]: List of groups, where each group contains anagrams

    Time Complexity: O(n * m) where n is number of strings, m is average string length
    Space Complexity: O(n * m) for storing the groups
    """

    # Use defaultdict to automatically create lists for new keys
    groups = defaultdict(list)

    # Process each word in the input list
    for word in strs:
        # Create a character count array for lowercase English letters (26 letters)
        count = [0] * 26

        # Count frequency of each character in the word
        for char in word:
            # Map character to index: 'a' -> 0, 'b' -> 1, ..., 'z' -> 25
            count[ord(char) - ord('a')] += 1

        # Use tuple of count array as key (since lists aren't hashable)
        # All anagrams will have the same count array, so they'll group together
        groups[tuple(count)].append(word)

    # Return the grouped anagrams as a list of lists
    return list(groups.values())


# Test the function with example inputs
if __name__ == "__main__":
    # Test case 1: Mixed anagrams
    strs1 = ["eat", "tea", "tan", "ate", "nat", "bat"]
    result1 = groupAnagrams(strs1)
    print(f"groupAnagrams({strs1}) = {result1}")

    # Test case 2: Empty string
    strs2 = [""]
    result2 = groupAnagrams(strs2)
    print(f"groupAnagrams({strs2}) = {result2}")

    # Test case 3: Single character strings
    strs3 = ["a"]
    result3 = groupAnagrams(strs3)
    print(f"groupAnagrams({strs3}) = {result3}")

    # Test case 4: No anagrams
    strs4 = ["abc", "def", "ghi"]
    result4 = groupAnagrams(strs4)
    print(f"groupAnagrams({strs4}) = {result4}")
