# https://leetcode.com/problems/encode-and-decode-strings/
from typing import List


class Codec:
    """
    Codec class for encoding a list of strings into a single string and decoding it back.

    The encoding uses a length-prefixed format: "length#string" for each string.
    This ensures we can properly decode even when strings contain special characters.
    """

    def encode(self, strs: List[str]) -> str:
        """
        Encode a list of strings into a single string.

        Each string is prefixed with its length followed by a '#' delimiter.
        For example: ["hello", "world"] -> "5#hello5#world"

        Args:
            strs (List[str]): List of strings to encode

        Returns:
            str: Encoded string
        """
        result = ""

        for s in strs:
            # Prefix each string with its length and a delimiter
            result += str(len(s)) + "#" + s

        return result

    def decode(self, s: str) -> List[str]:
        """
        Decode a single string back into a list of strings.

        Uses the length prefix to know how many characters to read for each string.

        Args:
            s (str): Encoded string to decode

        Returns:
            List[str]: Decoded list of strings
        """
        result = []
        i = 0

        while i < len(s):
            # Find the position of the '#' delimiter
            j = i
            while s[j] != "#":
                j += 1

            # Extract the length of the next string
            length = int(s[i:j])

            # Extract the string using the length
            word = s[j + 1 : j + 1 + length]
            result.append(word)

            # Move to the start of the next encoded string
            i = j + 1 + length

        return result


if __name__ == "__main__":
    codec = Codec()

    # Test case 1: Basic strings
    strs1 = ["hello", "world"]
    encoded1 = codec.encode(strs1)
    decoded1 = codec.decode(encoded1)
    print(f"Original: {strs1}")
    print(f"Encoded: '{encoded1}'")
    print(f"Decoded: {decoded1}")
    print(f"Round-trip successful: {strs1 == decoded1}")
    print()

    # Test case 2: Empty strings
    strs2 = ["", "test", ""]
    encoded2 = codec.encode(strs2)
    decoded2 = codec.decode(encoded2)
    print(f"Original: {strs2}")
    print(f"Encoded: '{encoded2}'")
    print(f"Decoded: {decoded2}")
    print(f"Round-trip successful: {strs2 == decoded2}")
    print()

    # Test case 3: Strings with special characters
    strs3 = ["we#are", "coding", "now!"]
    encoded3 = codec.encode(strs3)
    decoded3 = codec.decode(encoded3)
    print(f"Original: {strs3}")
    print(f"Encoded: '{encoded3}'")
    print(f"Decoded: {decoded3}")
    print(f"Round-trip successful: {strs3 == decoded3}")
