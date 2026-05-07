from typing import Set


def length_of_longest_substring(s: str) -> int:
    """
    Return the length of the longest substring without repeating characters.

    This uses a sliding window and a set to maintain the current window's unique
    characters. When a duplicate is encountered, move the left pointer until the
    window is valid again.

    Args:
        s (str): Input string

    Returns:
        int: Length of the longest substring with all unique characters

    Time Complexity: O(n)
    Space Complexity: O(min(n, m)) where m is the character set size
    """

    char_set: Set[str] = set()
    left = 0
    longest = 0

    for right in range(len(s)):
        # If current character already exists in window, shrink window from left
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1

        char_set.add(s[right])
        longest = max(longest, right - left + 1)

    return longest


if __name__ == "__main__":
    examples = [
        "abcabcbb",
        "bbbbb",
        "pwwkew",
        "",
        "abba",
    ]

    for s in examples:
        print(f"length_of_longest_substring('{s}') = {length_of_longest_substring(s)}")
    