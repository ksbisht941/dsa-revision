from typing import List


def max_profit(prices: List[int]) -> int:
    """
    Compute the maximum profit from a single buy and sell transaction.

    This scans the price list once while tracking the lowest purchase price seen
    so far, and updates the maximum profit whenever a higher selling profit is found.

    Args:
        prices (List[int]): Daily stock prices

    Returns:
        int: Maximum profit achievable with one buy and one sell

    Time Complexity: O(n)
    Space Complexity: O(1)
    """

    if not prices:
        return 0

    max_profit_value = 0
    min_price = prices[0]

    for price in prices:
        if price < min_price:
            min_price = price
            continue

        max_profit_value = max(max_profit_value, price - min_price)

    return max_profit_value


if __name__ == "__main__":
    test_cases = [
        [7, 1, 5, 3, 6, 4],
        [7, 6, 4, 3, 1],
        [1, 2, 3, 4, 5],
        [2, 1, 2, 1, 0, 1, 2],
    ]

    for prices in test_cases:
        print(f"max_profit({prices}) = {max_profit(prices)}")
