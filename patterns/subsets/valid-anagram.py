# https://leetcode.com/problems/valid-anagram/

def isAnagram(s: str, t: str) -> bool:
    """
    Check if two strings are anagrams of each other.
    An anagram is a word formed by rearranging the letters of another word.

    This function uses a hash table approach to count character frequencies.

    Args:
        s (str): First string to compare
        t (str): Second string to compare

    Returns:
        bool: True if strings are anagrams, False otherwise

    Time Complexity: O(n) where n is the length of the strings
    Space Complexity: O(k) where k is the number of unique characters
    """

    # Early exit: if lengths differ, they can't be anagrams
    if len(s) != len(t):
        return False

    # Create a dictionary to count character frequencies in string s
    count = {}

    # Count frequency of each character in string s
    for ch in s:
        count[ch] = count.get(ch, 0) + 1

    # Debug print to show character counts
    print(f"Character counts for '{s}':", count)

    # Check string t against the character counts
    for ch in t:
        # If character not in count or count is zero, not an anagram
        if ch not in count or count[ch] == 0:
            return False
        # Decrement the count for this character
        count[ch] -= 1

    # If we reach here, all characters matched
    return True


# Test the function with example inputs
if __name__ == "__main__":
    # Test case 1: Valid anagrams
    s1 = "listen"
    t1 = "silent"
    result1 = isAnagram(s1, t1)
    print(f"isAnagram('{s1}', '{t1}') = {result1}")

    print()  # Empty line for readability

    # Test case 2: Invalid anagrams (different lengths)
    s2 = "hello"
    t2 = "world"
    result2 = isAnagram(s2, t2)
    print(f"isAnagram('{s2}', '{t2}') = {result2}")

    print()  # Empty line for readability

    # Test case 3: Invalid anagrams (same length, different characters)
    s3 = "rat"
    t3 = "car"
    result3 = isAnagram(s3, t3)
    print(f"isAnagram('{s3}', '{t3}') = {result3}")
