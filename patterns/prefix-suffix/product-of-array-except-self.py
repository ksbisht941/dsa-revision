# https://leetcode.com/problems/product-of-array-except-self/
from typing import List

def productExceptSelf(nums: List[int]) -> List[int]:
    """
    Return an array where each element is the product of all other elements.

    This implementation uses prefix and postfix products to compute the result
    in O(n) time without using division.

    Args:
        nums (List[int]): Input list of numbers

    Returns:
        List[int]: Product array where each position contains the product of every
                   input element except the one at that position.
    """

    # Initialize result array with 1s, which will accumulate prefix and postfix products.
    result = [1] * len(nums)

    # Compute prefix products and store them in result.
    prefix = 1
    for i in range(len(nums)):
        result[i] = prefix
        prefix *= nums[i]

    # Compute postfix products and multiply with the stored prefix values.
    postfix = 1
    for i in range(len(nums) - 1, -1, -1):
        result[i] *= postfix
        postfix *= nums[i]

    return result


if __name__ == "__main__":
    # Example data for verification
    nums = [1, 2, 3, 4]
    print("Input:", nums)

    result = productExceptSelf(nums)
    print("Output:", result)
