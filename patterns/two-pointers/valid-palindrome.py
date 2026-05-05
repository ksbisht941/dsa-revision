# https://leetcode.com/problems/valid-palindrome/
def isPalindrome(s: str) -> bool:
    """
    Check if a string is a valid palindrome, ignoring case and non-alphanumeric characters.

    This function uses two pointers starting from both ends of the string, moving towards
    the center while skipping non-alphanumeric characters.

    Args:
        s (str): Input string to check

    Returns:
        bool: True if the string is a palindrome, False otherwise

    Time Complexity: O(n) where n is the length of the string
    Space Complexity: O(1) - only uses constant extra space
    """

    left = 0
    right = len(s) - 1

    while left < right:
        # Skip non-alphanumeric characters from the left
        while left < right and not s[left].isalnum():
            left += 1

        # Skip non-alphanumeric characters from the right
        while left < right and not s[right].isalnum():
            right -= 1

        # Compare characters (case-insensitive)
        if s[left].lower() != s[right].lower():
            return False

        # Move pointers towards center
        left += 1
        right -= 1

    return True


if __name__ == "__main__":
    # Test case 1: Valid palindrome with mixed case and punctuation
    s1 = "A man, a plan, a canal: Panama"
    result1 = isPalindrome(s1)
    print(f"isPalindrome('{s1}') = {result1}")

    # Test case 2: Invalid palindrome
    s2 = "race a car"
    result2 = isPalindrome(s2)
    print(f"isPalindrome('{s2}') = {result2}")

    # Test case 3: Simple palindrome
    s3 = "abba"
    result3 = isPalindrome(s3)
    print(f"isPalindrome('{s3}') = {result3}")

    # Test case 4: Empty string
    s4 = ""
    result4 = isPalindrome(s4)
    print(f"isPalindrome('{s4}') = {result4}")

    # Test case 5: Single character
    s5 = "a"
    result5 = isPalindrome(s5)
    print(f"isPalindrome('{s5}') = {result5}")

